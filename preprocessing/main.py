import os
import json
import io
from collections import defaultdict
import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
srv = pysftp.Connection(host="10.5.18.104",username="14CS30022",password="dual14",cnopts=cnopts)
srv.chdir("dataset")

months = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}

def write_tweets_to_files(dict_path8, dict_path4):
	cnt = 0
	factor = 0
	overall_dict = {}
	half_dict = {}

	dirs = open("dirs.txt",'r')
	dirs = dirs.read();
	dirs = dirs.split("\n")

	presume = 0
	factor = 11
	for filename in dirs:
		presume += 1
		if presume <= 55000:
			continue

		if filename == "":
			continue
		if cnt == numtweets:
			factor += 1
			with io.open(dict_path8+"part"+str(factor)+".txt", "w", encoding="utf8") as ft:
				ft.write(unicode(json.dumps(overall_dict,indent=4,ensure_ascii=False,sort_keys=True)))
			with io.open(dict_path4+"part"+str(factor)+".txt", "w", encoding="utf8") as ft:
				ft.write(unicode(json.dumps(half_dict,indent=4,ensure_ascii=False,sort_keys=True)))
			overall_dict = {}
			half_dict = {}
			cnt = 0

		f = srv.get(filename)
		f = open(filename,'r')
		text = f.read()
		text = text.split("\n")
		# print len(text)
		check1 = 0
		tweet_dict_8 = []
		tweet_dict_4 = []
		
		onow = 0
		for each in text:
			try:
				check1+=1
				tweet_data = json.loads(each)
				temp = {}
				cat = (tweet_data["created_at"]).split(" ")
				#"Tue Jul 30 16:42:48 +0000 2013"
				s = cat[5]+"-"+months[cat[1]]+"-"+cat[2]
				if cat[5] != "2013":
					continue
				if int(months[cat[1]]) > 8:
					continue
				temp["created_at"] = s
				temp["text"] = tweet_data["text"]
				tweet_dict_8.append(temp)
				if int(months[cat[1]]) <= 4:
					tweet_dict_4.append(temp)

			except Exception as e:
				#print "My Error:",e
				ign = 0
				onow+=1

		if onow > 1:
			print "oops some problem",filename

		overall_dict[filename] = tweet_dict_8
		half_dict[filename] = tweet_dict_4
		cnt += 1
		
		os.remove(filename)
		print cnt+numtweets*factor #for user
	
	factor += 1
	with io.open(dict_path8+"part"+str(factor)+".txt", "w", encoding="utf8") as ft:
		ft.write(unicode(json.dumps(overall_dict,indent=4,ensure_ascii=False,sort_keys=True)))
	with io.open(dict_path4+"part"+str(factor)+".txt", "w", encoding="utf8") as ft:
		ft.write(unicode(json.dumps(half_dict,indent=4,ensure_ascii=False,sort_keys=True)))
	#print "Tweets cnt ",cnt
	print "job done"



dict_path8 = "../8months/"
dict_path4 = "../4months/"

numtweets = 5000
write_tweets_to_files(dict_path8,dict_path4)
