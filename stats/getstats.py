import os
import json
import io
import numpy as np
from collections import defaultdict
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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

	d = {}
	for i in range(1,26):
		f = open(path+"part"+str(i)+".txt",'r')	
		dic = json.loads(f.read())
		for each in dic:
			# filtered_words = 0

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

			# print day_10,day_20,day_30

			num_words10 = 0
			num_words20 = 0
			num_words30 = 0
			for every in dic[each]:	
				tweet = every['text'].split(" ")
				time = every['created_at']

				if time > day_30:
					continue
				if time < day_10:
					num_words10+= 2*(len(tweet))+1
				if time < day_20:
					num_words20+= 2*(len(tweet))+1
				if time < day_30:
					num_words30+= 2*(len(tweet))+1
			d[each] = [num_words10,num_words20,num_words30]		
			
		print i,"done"
	
	f2 = open("stats.txt",'wb')
	f2.write(json.dumps(d))

main("../../8months/")

