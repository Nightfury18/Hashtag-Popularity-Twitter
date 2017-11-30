import numpy as np
import scipy.stats.stats
import math
# from scipy.stats import pearson
# from scipy.stats import linregress

preds = np.load("preds_cum_Gr10_log_Dr0.3.npy")

y_train = np.load("newYtrain4_cum_Gr10.npy")

for x in range(y_train.shape[0]):
	y_train[x] = math.log(y_train[x])

ll = y_train.shape[0]
ll = (ll*9)/10

ytest=y_train[ll+1:]

size = preds.shape[0]

pre = np.zeros(size)

for x in range(size):
	pre[x] = preds[x]

print "Shape : " + str(pre.shape) + "\n"
print "Shape : " + str(ytest.shape) + "\n"

# for x in range(size):
# 	print str(y_test[x]) + "	" + str(preds[x])


# RMSE

rmse = np.sqrt(((preds - ytest) ** 2).mean())

print "Root Means Square Error : " + str(rmse) + "\n"

rmse = rmse / (np.amax(ytest) - np.amin(ytest))

print "Data Min : " + str(np.amin(ytest)) + ", Data Max : " + str(np.amax(ytest)) + "\n"

print "Normalized Root Means Square Error : " + str(rmse) + "\n"
	

# Pearson's Correlation Coeff

pear = np.corrcoef(pre, ytest)[0, 1]

# pear = scipy.stats.stats.pearsonr(preds, y_test)

print "Pearson Correlation Coefficient : " + str(pear) + "\n"


#R^2 

slope, intercept, r_value, p_value, std_err = scipy.stats.stats.linregress(pre, ytest)

print "R^2 : " + str(r_value**2) + "\n"
