import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

f = open("process_dump.txt",'r')
text = f.read()
# text.replace('\n',' ')
words = text.split(" ")
f.close()

f = open("vectors_dict.txt",'r')
d = json.loads(f.read())
f.close()

cnt = 0
uscnt = 0

out = " "

for each in words:
	uscnt += 1
	#print uscnt,"/",len(words)
	if (each not in d) and (each.encode("utf8")) not in d:
		cnt+=1
		out += each + " "
	if uscnt%10000000 == 0:
		print uscnt

f = open("false_words.txt",'w')
f.write(out)

print "Total false pairs: ",cnt