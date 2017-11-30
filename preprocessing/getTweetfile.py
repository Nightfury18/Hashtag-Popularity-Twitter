import os
import json
import io
from collections import defaultdict
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

user_del = " --;;;;-- "
def main(path):
	
	s = ""
	cnt = 0
	f1 = open("dump.txt",'wb')
	for i in range(1,26):
		f = open(path+"part"+str(i)+".txt",'r')	
		dic = json.loads(f.read())
		for each in dic:
			for every in dic[each]:
				cnt+=1
				s = every['text'] + user_del

				f1.write(s.encode("utf-8"))
		print cnt,"10668209"
	
	# f1.wtite(s)

main("../n8months/")
