import numpy as np 

# fullx = np.load("Xtrain_cum.npy")
fully = np.load("Ytrain_cum.npy")

# lisx = []
# lisy = []

size = fully.shape[0]

# for x in range(size):
# 	if fully[x] > 10 :
# 		lisx.append(fullx[x])
# 		lisy.append(fully[x])

# newX = np.array(lisx)
# newY = np.array(lisy)

# np.save("newXtrain4_cum_Gr10.npy", newX)
# np.save("newYtrain4_cum_Gr10.npy", newY)

# print newX.shape
# print newY.shape





























zero = 0
onefifty = 0
fiftyhun = 0
hunfivehun = 0
fivehunthou = 0
gthou = 0

for x in range(size):
	if fully[x] == 0 :
		zero += 1
	elif fully[x] > 0 and fully[x] <= 50 :
		onefifty += 1
	elif fully[x] > 50 and fully[x] <= 100 :
		fiftyhun += 1
	elif fully[x] > 100 and fully[x] <= 500 :
		hunfivehun += 1
	elif fully[x] > 500 and fully[x] <= 1000 :
		fivehunthou += 1
	else :
		gthou += 1

print "\n"

print "0        : " + str(zero) + "\n"
print "1-50     : " + str(onefifty) + "\n"
print "50-100   : " + str(fiftyhun) + "\n"
print "100-500  : " + str(hunfivehun) + "\n"
print "500-1000 : " + str(fivehunthou) + "\n"
print "1000 -   : " + str(gthou) + "\n" 

		