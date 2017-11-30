import json

d = {}
f = open("vectors_dict.txt",'r')
d = json.loads(f.read())
f.close()

print "dict loaded"

while True:
	s = raw_input()
	if s not in d:
		print s,"not present"
	else:
		print s,"present"