import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical


traindf = pd.read_csv("data/exToptimizedtrain.csv")
testdf = pd.read_csv("data/exToptimizedtest.csv")

feature_cols = list(traindf.columns)
feature_cols.remove('labels')

x_train = traindf[feature_cols].to_numpy()
y_train = to_categorical(traindf['labels'].to_numpy())

x_test = testdf[feature_cols].to_numpy()
y_test = to_categorical(testdf['labels'].to_numpy())

accuracylist = list()
for i in range(5):
    model = Sequential()
    model.add(Dense(1024, activation="relu", input_dim = x_train.shape[1]))
    model.add(Dense(512, activation="relu"))
    model.add(Dense(200, activation="relu"))
    model.add(Dense(y_train.shape[1], activation="softmax"))

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=['categorical_crossentropy','accuracy'])

    model.fit(x_train, y_train, validation_data=(x_test, y_test), verbose=1, epochs=25, shuffle=True)

    predicted = np.argmax(model.predict(x_test), axis=1)
    valid = np.argmax(y_test, axis=1)
    accuracy = 0
    test_range = len(valid)
    for k in range(test_range):
        if predicted[k] == valid[k]:
            accuracy += 1

    print("Accuracy = ", accuracy / test_range)
    accuracylist.append(accuracy / test_range)
print(accuracylist)
