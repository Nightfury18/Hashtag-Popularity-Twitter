

# LSTM with dropout for sequence classification in the IMDB dataset
import numpy as np
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM,GRU
from keras.layers.embeddings import Embedding
from keras.layers import Bidirectional 
from keras.preprocessing import sequence
# fix random seed for reproducibility
np.random.seed(7)
# load the dataset but only keep the top n words, zero the rest
top_words = 65716
# (X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)
X_train=np.load("Xtrain.npy")
y_train=np.load("Ytrain.npy")

embed=np.load("embed.npy")
print embed.shape
# truncate and pad input sequences
max_review_length = 70
X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
Xtrain=X_train[:300000]
Ytrain=y_train[:300000]
Xtest=X_train[300000:]
Ytest=y_train[300000:]
# X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)
# # create the model

embedding_vector_length = 100
model = Sequential()

model.add(Embedding(top_words, embedding_vector_length,weights=[embed], input_length=max_review_length))
# model.layers[1].trainable=False
model.add(Bidirectional(GRU(100, dropout=0.2, recurrent_dropout=0.2)))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(Xtrain, Ytrain, epochs=1, batch_size=64)
# # Final evaluation of the model

scores = model.evaluate(Xtest, Ytest, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))
