import os
import json
import io
import numpy as np
from collections import defaultdict
import numpy as np

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

notfound = [0.5]*50

def main():

	f1 = open("../vectors_dict.txt",'r')
	words = json.loads(f1.read())
	f1.close()

	out = {}
	cnt = 0
	embed = []
	for each in words:
		out[each] = cnt
		cnt+=1
		if len(words[each]) != 50:
			embed.append(notfound)
		else:
			embed.append(words[each])

	
	out["__dummy__"] = cnt
	embed.append(notfound)
	cnt += 1

	f = open("words_indices.txt",'w')
	f.write(json.dumps(out))

	embed = np.array(embed)
	np.save("embed.npy",embed)
	
	print "Size of vocabulary ",cnt	
main()