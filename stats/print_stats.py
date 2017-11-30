import json
import io

f = open("stats.txt",'r')
d = json.loads(f.read())
f.close()

# 1-10
#      10-20
#      20-30
#      30-50
#      50-100
#     100-150
#     150-200
#      >200

num = [[0]*8,[0]*8,[0]*8]

for each in d:
	l = d[each]
	for i in range(3):
		if l[i] <= 10 and l[i] > 0:
			num[i][0] += 1
		
		if l[i] >= 11 and l[i] <= 20:
			num[i][1] += 1

		if l[i] >= 21 and l[i] <= 30:
			num[i][2] += 1

		if l[i] >= 31 and l[i] <= 50:
			num[i][3] += 1

		if l[i] >= 51 and l[i] <= 100:
			num[i][4] += 1

		if l[i] >= 101 and l[i] <= 150:
			num[i][5] += 1

		if l[i] >= 151 and l[i] <= 200:
			num[i][6] += 1
		
		if l[i] >= 201:
			num[i][7] += 1	

print num
