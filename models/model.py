import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM,GRU
from keras.layers.embeddings import Embedding
from keras.layers import Bidirectional 
from keras.preprocessing import sequence
from keras.models import model_from_json
from keras.layers import Dropout
import math


np.random.seed(7)
top_words = 1423098
# No of words = 1423098

#No of Training Examples with hashtag frequency > 50: 4927
#No of Training Examples with hashtag frequency > 10: 16286
#No of Training Examples with cumulative hashtag frequency > 10: 55006

embedding_vector_length = 50

X_train = np.load("newXtrain4_cum_Gr10.npy")
y_train = np.load("newYtrain4_cum_Gr10.npy")
embed = np.load("embed.npy")


for x in range(y_train.shape[0]):
	y_train[x] = math.log(y_train[x])

print "No of Training examples :" + str(len(X_train)) + "\n"

embed_matrix = np.zeros((top_words+1, embedding_vector_length))

i = 0
for each in embed :
	if each is not None :
		embed_matrix[i] = each
	i = i + 1

print embed.shape
print embed_matrix.shape


max_review_length = 500
#13694168
X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
ll = len(X_train)
ll = (ll*9)/10
Xtrain=X_train[:ll+1]
Ytrain=y_train[:ll+1]
Xtest=X_train[ll+1:]
Ytest=y_train[ll+1:]
Xtest = sequence.pad_sequences(Xtest, maxlen=max_review_length)


model = Sequential()

model.add(Embedding(top_words+1, embedding_vector_length,weights=[embed_matrix], input_length=max_review_length, trainable=False))
# model.add(Bidirectional(LSTM(100, dropout=0.2, recurrent_dropout=0.2)))
model.add(Bidirectional(GRU(1000, dropout=0.1, recurrent_dropout=0.1)))
model.add(Dense(32))
model.add(Dropout(0.1))
model.add(Dense(8))
model.add(Dropout(0.1))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_squared_error', 'mean_absolute_error', 'mean_absolute_percentage_error'])
print(model.summary())
model.fit(Xtrain, Ytrain, epochs=12, batch_size=32)

scores = model.evaluate(Xtest, Ytest, verbose=0)

print "\n\nScores : "
print scores
print "\n\n"

preds = model.predict(Xtest, batch_size=64, verbose=0)

np.save("preds_cum_Gr10_log_Dr0.1.npy", preds)

print "\n\n\Done !!\n\n"

