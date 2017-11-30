import os
import json
import io
import numpy as np
from collections import defaultdict
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


notfound = "__dummy__"
user_del = "--;;;;--"

def add_10(mini):
	mon = int(mini.split("-")[1]) 
	day = int(mini.split("-")[2]) 
	yr = int(mini.split("-")[0]) 

	day += 10

	if day > 30:
		day = day%30
		mon += 1
		if mon > 12:
			yr += 1
			mon = 1

	mini = str(yr) + "-"
	if mon<10:
		mini += "0"
	mini += str(mon)+"-"
	if day < 10:
		mini += "0"
	mini += str(day)

	return mini


def main(path):

	f1 = open("words_indices.txt",'r')
	words = json.loads(f1.read())
	f1.close()

	X = []
	Y = []
	# X_20 = []
	# Y_20 = []

	for i in range(1,26):
		f = open(path+"part"+str(i)+".txt",'r')	
		dic = json.loads(f.read())
		for each in dic:
			temp = []
			pop = 0

			mini = "2020-12-31"
			# maxi = "1990-01-01"

			for every in dic[each]:
				tweet = every['text']
				s = every['created_at']
				#"Tue Jul 30 16:42:48 +0000 2013"
				if mini > s:
					mini = s

			day_10 = add_10(mini)
			day_20 = add_10(day_10)
			day_30 = add_10(day_20)
			day_40 = add_10(day_30)
			day_50 = add_10(day_40)

			for every in dic[each]:
				tweet = every['text']
				time = every['created_at']

				if time <= day_10:
					tweet = tweet.split(" ")
					for tok in tweet:
						if (tok in words):
							temp.append(words[tok])
						elif tok != "":
							temp.append(words[notfound])
						temp.append(words[notfound])

					temp.append(words[user_del])
					pop+=1

				elif time <= day_40:
					pop += 1
			# print "pop is ",pop
			X.append(temp)
			Y.append(pop)
		print i,"done"

	X = np.array(X)
	Y = np.array(Y)
	np.save("Xtrain_10_30.npy",X)
	np.save("Ytrain_10_30.npy",Y)

main("../../8months/")

