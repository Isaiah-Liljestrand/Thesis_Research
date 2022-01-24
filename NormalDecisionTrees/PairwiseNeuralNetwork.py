import os
import pandas as pd
import numpy as np
from numpy.random import randint
from sklearn.tree import DecisionTreeClassifier
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn import metrics
from sklearn import tree

#Creates a pairwise classification tree and returns the predictions from both training and testing sets
def PairwiseTree(originaltraindf, originaltestdf, target1, target2):

    print("Starting tree ", target1, " ", target2)
    traindf = originaltraindf.copy()

    elimlist = list()
    trainlabels = list(traindf['labels'])
    for i in range(len(trainlabels)):
        if trainlabels[i] != target1 and trainlabels[i] != target2:
            elimlist.append(i)
    traindf.drop(elimlist, inplace=True)
    traindf.reset_index(drop = True, inplace = True)

    feature_cols = list(traindf.columns)
    feature_cols.remove('labels')

    x_train = traindf[feature_cols].to_numpy()
    y_train = to_categorical(traindf['labels'].to_numpy())

    testdf = originaltestdf.copy()

    elimlist = list()
    testlabels = list(testdf['labels'])
    for i in range(len(testlabels)):
        if testlabels[i] != target1 and testlabels[i] != target2:
            elimlist.append(i)
    testdf.drop(elimlist, inplace=True)
    testdf.reset_index(drop = True, inplace = True)

    feature_cols = list(testdf.columns)
    feature_cols.remove('labels')

    x_test = testdf[feature_cols].to_numpy()
    y_test = to_categorical(testdf['labels'].to_numpy())


    model = Sequential()
    model.add(Dense(200, activation="relu", input_dim = x_train.shape[1]))
    model.add(Dense(100, activation="relu"))
    model.add(Dense(30, activation="relu"))
    model.add(Dense(y_train.shape[1], activation="softmax"))

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=['categorical_crossentropy','accuracy'])

    model.fit(x_train, y_train, validation_data=(x_test, y_test), verbose=1, epochs=20, shuffle=True)

    predicted = np.argmax(model.predict(x_test), axis=1)
    valid = np.argmax(y_test, axis=1)


    x_o_train = originaltraindf[feature_cols].to_numpy()
    x_o_test = originaltestdf[feature_cols].to_numpy()

    y_pred_train = np.argmax(model.predict(x_o_train), axis=1)


    for i in range(len(y_pred_train)):
        if y_pred_train[i] == target1:
            y_pred_train[i] = 1
        elif y_pred_train[i] == target2:
            y_pred_train[i] = -1
        else:
            if randint(2) == 1:
                y_pred_train[i] = 1
            else:
                y_pred_train[i] = -1

    y_pred_test = np.argmax(model.predict(x_o_test), axis=1)

    for i in range(len(y_pred_test)):
        if y_pred_test[i] == target1:
            y_pred_test[i] = 1
        elif y_pred_test[i] == target2:
            y_pred_test[i] = -1
        else:
            if randint(2) == 1:
                y_pred_test[i] = 1
            else:
                y_pred_test[i] = -1

    return y_pred_train, y_pred_test


def PopulateResults(traindf, testdf):

    trainresultdf = pd.DataFrame()
    testresultdf = pd.DataFrame()

    trainresultdf['labels'] = traindf['labels']
    testresultdf['labels'] = testdf['labels']

    for label1 in range(23):
        for label2 in range(label1 + 1, 23):
            pairname = str(label1) + " " + str(label2)
            print("Processing ", pairname)
            tmptrain, tmptest = PairwiseTree(traindf, testdf, label1, label2)
            trainresultdf[pairname] = tmptrain
            testresultdf[pairname] = tmptest
    return trainresultdf, testresultdf



def Classify(method, index, oresultdf):

    resultdf = oresultdf.copy()

    indices = list(range(len(resultdf['0 1'])))
    indices.remove(index)
    resultdf.drop(indices, inplace=True)
    resultdf.reset_index(drop = True, inplace=True)




    #Class Voting
    if method == 1:
        labelvalues = [0] * 23
        for j in range(23):
            for k in range(23):
                if j < k:
                    pairname = str(j) + " " + str(k)
                    result = list(resultdf[pairname])[0]
                    labelvalues[j] += result
                    labelvalues[k] -= result
        result = list()
        max = 0
        for j in range(23):
            if max < labelvalues[j]:
                max = labelvalues[j]
        for j in range(23):
            if max == labelvalues[j]:
                result.append(j);
        if len(result) == 2:
            pairname = str(result[0]) + " " + str(result[1])
            tmpresult = list(resultdf[pairname])[0]
            if tmpresult == 1:
                result = [result[0]]
            elif tmpresult == -1:
                result = [result[1]]
        elif len(result) > 2:
            tmplength = len(result) + 1
            breakout = False
            while len(result) > 1:
                if tmplength == len(result):
                    break
                tmplength = len(result)
                for i in range(len(result) - 1):
                    for j in range(i + 1, len(result)):
                        pairname = str(result[i]) + " " + str(result[j])
                        tmpresult = list(resultdf[pairname])[0]
                        if tmpresult == 1:
                            del result[j]
                            breakout = True
                        if tmpresult == -1:
                            del result[i]
                            breakout = True
                        if breakout:
                            break
                    if breakout:
                        break
                breakout = False
        return result[0]




    #Eliminate Weakest
    if method == 2:
        labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        while len(labels) > 1:
            labelvalues = [0] * 23
            for j in labels:
                for k in labels:
                    if j < k:
                        pairname = str(j) + " " + str(k)
                        result = list(resultdf[pairname])[0]
                        labelvalues[j] += result
                        labelvalues[k] -= result
            min = 50
            minindex = 0
            for j in labels:
                if labelvalues[j] < min:
                    min = labelvalues[j]
                    minindex = j
            labels.remove(minindex)
        return labels[0]




    #Tourney
    if method == 3:
        labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        labelsize = len(labels)
        while 1:
            if len(labels) == 1:
                break
            nextlabels = list()

            #Randomize labels in tourney
            for j in range(len(labels)):
                r = randint(len(labels))
                nextlabels.append(labels[r])
                del labels[r]
            while len(nextlabels) > 1:
                if nextlabels[0] > nextlabels[1]:
                    tmp = nextlabels[0]
                    nextlabels[0] = nextlabels[1]
                    nextlabels[1] = tmp
                pairname = str(nextlabels[0]) + " " + str(nextlabels[1])
                result = list(resultdf[pairname])[0]
                if result == 1:
                    labels.append(nextlabels[0])
                elif result == -1:
                    labels.append(nextlabels[1])
                del nextlabels[0]
                del nextlabels[0]
            if len(nextlabels) == 1:
                labels.append(nextlabels[0])
        return labels[0]





    #Hybrid - k = 5
    if method == 4:
        labelvalues = [0] * 23
        for j in range(23):
            for k in range(j + 1, 23):
                pairname = str(j) + " " + str(k)
                result = list(resultdf[pairname])[0]
                labelvalues[j] += result
                labelvalues[k] -= result
        labels = list()
        for k in range(5):
            result = 0
            max = 0
            for j in range(23):
                if max < labelvalues[j]:
                    result = j
                    max = labelvalues[j]
            labelvalues[result] = -22
            labels.append(result)

        labelsize = len(labels)
        while 1:
            if len(labels) == 1:
                break
            #Randomize labels in tourney
            nextlabels = list()
            for j in range(len(labels)):
                r = randint(len(labels))
                nextlabels.append(labels[r])
                del labels[r]
            while len(nextlabels) > 1:
                if nextlabels[0] > nextlabels[1]:
                    tmp = nextlabels[0]
                    nextlabels[0] = nextlabels[1]
                    nextlabels[1] = tmp
                pairname = str(nextlabels[0]) + " " + str(nextlabels[1])
                result = list(resultdf[pairname])[0]
                if result == 1:
                    labels.append(nextlabels[0])
                elif result == -1:
                    labels.append(nextlabels[1])
                del nextlabels[0]
                del nextlabels[0]
            if len(nextlabels) == 1:
                labels.append(nextlabels[0])
        return labels[0]


def RunClassifier(df, method):
    labellist = list(df['labels'])
    success = 0
    multiclass = 0

    for i in range(len(labellist)):
        if (i % 5000) == 0:
            print("ticks: ", i)
        result = Classify(method, i, df)
        answer = labellist[i]

        if answer == result:
            success += 1
    accuracy = (success / len(labellist)) * 100
    multiclass = (multiclass / len(labellist)) * 100
    print("Accuracy:", accuracy)
    print("Multi:", multiclass)

traindf = pd.read_csv("data/exToptimizedtrain.csv")
testdf = pd.read_csv("data/exToptimizedtest.csv")

print("Finished reading in data")

print("Starting to populate results")
trainresultdf, testresultdf = PopulateResults(traindf, testdf)
print("Finished populating results")

print("\n\n")
print("Class Voting")
print("Training:")
RunClassifier(trainresultdf, 1)
print("\n")
print("Testing:")
RunClassifier(testresultdf, 1)

print("\n\n")
print("Victim Elimination")
print("Training:")
RunClassifier(trainresultdf, 2)
print("\n")
print("Testing:")
RunClassifier(testresultdf, 2)

print("\n\n")
print("Tourney")
print("Training:")
RunClassifier(trainresultdf, 3)
print("\n")
print("Testing:")
RunClassifier(testresultdf, 3)

print("\n\n")
print("Hybrid")
print("Training:")
RunClassifier(trainresultdf, 4)
print("\n")
print("Testing:")
RunClassifier(testresultdf, 4)
