import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM,GRU
from keras.layers.embeddings import Embedding
from keras.layers import Bidirectional 
from keras.preprocessing import sequence

np.random.seed(7)
top_words = 935608

embedding_vector_length = 50

X_train=np.load("Xtrain4.npy")
y_train=np.load("Ytrain4.npy")

embed=np.load("embed1.npy")

embed_matrix = np.zeros((top_words+1, embedding_vector_length))
i = 0
for each in embed :
	embedding_vector = each
	if embedding_vector is not None :
		embed_matrix[i] = embedding_vector
	i = i + 1

print embed.shape
print embed_matrix.shape


max_review_length = 1000
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
model.add(Bidirectional(LSTM(100, dropout=0.2, recurrent_dropout=0.2)))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='mean_squared_error', optimizer='adam')
print(model.summary())
model.fit(Xtrain, Ytrain, epochs=1, batch_size=64)
# # Final evaluation of the model
# make predictions

trainPredict = model.predict(Xtrain)
testPredict = model.predict(Xtest)
# invert predictions
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([Ytrain])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([Ytest])
# calculate root mean squared error
trainScore = math.sqrt(mean_squared_error(Ytrain[0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))
