import os
import json
import io
from collections import defaultdict
import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
srv = pysftp.Connection(host="10.5.18.104",username="14CS30022",password="dual14",cnopts=cnopts)
srv.chdir("dataset")
dirs = srv.listdir()

text = ""
for filename in dirs:
	text += filename + "\n"

f = open("dirs.txt",'w')
f.write(text)