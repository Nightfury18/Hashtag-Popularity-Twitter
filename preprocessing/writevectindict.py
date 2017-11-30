import json
import io

f = open("vectors.txt",'r')
load = f.read()
f.close()
load = load.split("\n")
dic = {}
for each in load:
	try:
		l = []
		now = each.split(" ")
		for i in range(1,len(now)):
			l.append(float(now[i]))
		dic[now[0]] = l
	except:
		print "Last index?"

f = open("vectors_dict.txt",'w')
f.write(json.dumps(dic))
# with io.open("vectors_dict.txt", "w", encoding="utf8") as ft:
# 	ft.write(json.dumps(dic,indent=4,ensure_ascii=False,sort_keys=True))