import os
import pandas as pd
from numpy.random import randint
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import tree

#Creates a pairwise classification tree and returns the predictions from both training and testing sets
def PairwiseTree(originaltraindf, originaltestdf, target1, target2):

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
    y_train = traindf['labels'].to_numpy()

    clf = DecisionTreeClassifier()
    clf = clf.fit(x_train,y_train)

    print(tree.export_text(clf))

    x_o_train = originaltraindf[feature_cols].to_numpy()
    x_o_test = originaltestdf[feature_cols].to_numpy()

    y_pred_train = clf.predict(x_o_train)
    y_pred_test = clf.predict(x_o_test)

    for i in range(len(y_pred_test)):
        if y_pred_test[i] == target1:
            y_pred_test[i] = 1
        elif y_pred_test[i] == target2:
            y_pred_test[i] = -1
        else:
            print("Error, unexpected return value")

    for i in range(len(y_pred_train)):
        if y_pred_train[i] == target1:
            y_pred_train[i] = 1
        elif y_pred_train[i] == target2:
            y_pred_train[i] = -1
        else:
            print("Error, unexpected return value")

    return y_pred_train, y_pred_test


def PopulateResults(traindf, testdf):

    trainresultdf = pd.DataFrame()
    testresultdf = pd.DataFrame()

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
        indices = list(range(len(df['labels'])))
        indices.remove(index)
        tmpdf = df.copy()
        tmpdf.drop(indices, inplace=True)
        tmpdf.reset_index(drop = True, inplace=True)
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
        for n in range(len(labels) - 1):
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




traindf = pd.read_csv("data/exToptimizedtrain.csv")
testdf = pd.read_csv("data/exToptimizedtest.csv")

print("Finished reading in data")

print("Starting to populate results")
trainresultdf, testresultdf = PopulateResults(traindf, testdf)
print("Finished populating results")

#Method 1
method = 1
df = traindf
resultdf = trainresultdf
labellist = list(df['labels'])
success = 0

#for i in range(len(labellist)):
#    if (i % 100) == 0:
#        print("1/8: ", i)
#    result = Classify(method, i, resultdf)
#    answer = labellist[i]

#    if answer == result:
#        success += 1
accuracy = (success / len(labellist)) * 100
print("\nMethod ", method, ", Training Accuracy:", accuracy)
acc1 = accuracy

df = testdf
resultdf = testresultdf
labellist = list(df['labels'])
success = 0

for i in range(len(labellist)):
    if (i % 100) == 0:
        print("2/8: ", i)
    result = Classify(method, i, resultdf)
    answer = labellist[i]

    if answer == result:
        success += 1
accuracy = (success / len(labellist)) * 100
print("Method ", method, ", Testing Accuracy:", accuracy)
acc2 = accuracy


#Method 2
method = 2
df = traindf
resultdf = trainresultdf
labellist = list(df['labels'])
success = 0

#for i in range(len(labellist)):
#    if (i % 100) == 0:
#        print("3/8: ", i)
#    result = Classify(method, i, resultdf)
#    answer = labellist[i]

#    if answer == result:
#        success += 1
accuracy = (success / len(labellist)) * 100
print("\nMethod ", method, ", Training Accuracy:", accuracy)
acc3 = accuracy

df = testdf
resultdf = testresultdf
labellist = list(df['labels'])
success = 0

for i in range(len(labellist)):
    if (i % 100) == 0:
        print("4/8: ", i)
    result = Classify(method, i, resultdf)
    answer = labellist[i]

    if answer == result:
        success += 1
accuracy = (success / len(labellist)) * 100
print("Method ", method, ", Testing Accuracy:", accuracy)
acc4 = accuracy



#Method 3
method = 3
df = traindf
resultdf = trainresultdf
labellist = list(df['labels'])
success = 0

#for i in range(len(labellist)):
#    if (i % 100) == 0:
#        print("5/8: ", i)
#    result = Classify(method, i, resultdf)
#    answer = labellist[i]
#
#    if answer == result:
#        success += 1
accuracy = (success / len(labellist)) * 100
print("\nMethod ", method, ", Training Accuracy:", accuracy)
acc5 = accuracy

df = testdf
resultdf = testresultdf
labellist = list(df['labels'])
success = 0

for i in range(len(labellist)):
    if (i % 100) == 0:
        print("6/8: ", i)
    result = Classify(method, i, resultdf)
    answer = labellist[i]

    if answer == result:
        success += 1
accuracy = (success / len(labellist)) * 100
print("Method ", method, ", Testing Accuracy:", accuracy)
acc6 = accuracy

#Method 4
method = 4
df = traindf
resultdf = trainresultdf
labellist = list(df['labels'])
success = 0

#for i in range(len(labellist)):
#    if (i % 100) == 0:
#        print("7/8: ", i)
#    result = Classify(method, i, resultdf)
#    answer = labellist[i]

#    if answer == result:
#        success += 1
accuracy = (success / len(labellist)) * 100
print("\nMethod ", method, ", Training Accuracy:", accuracy)
acc7 = accuracy

df = testdf
resultdf = testresultdf
labellist = list(df['labels'])
success = 0

for i in range(len(labellist)):
    if (i % 100) == 0:
        print("8/8: ", i)
    result = Classify(method, i, resultdf)
    answer = labellist[i]

    if answer == result:
        success += 1
accuracy = (success / len(labellist)) * 100
print("Method ", method, ", Testing Accuracy:", accuracy)
acc8 = accuracy

print("\n\nFinished running everything\n\n")

print("Method 1 Training:\n", acc1, "\n")

print("Method 1 Testing:\n", acc2, "\n")

print("Method 2 Training:\n", acc3, "\n")

print("Method 2 Testing:\n", acc4, "\n")

print("Method 3 Training:\n", acc5, "\n")

print("Method 3 Testing:\n", acc6, "\n")

print("Method 4 Training:\n", acc7, "\n")

print("Method 4 Testing:\n", acc8, "\n")

print("Done")



#Method 1 Training:
 #100.0

#Method 1 Testing:
 #94.62823452341958

#Method 2 Training:
 #100.0

#Method 2 Testing:
 #91.87684245004914

#Method 3 Training:
 #100.0

#Method 3 Testing:
 #91.97510645266951

#Method 4 Training:
 #100.0

#Method 4 Testing:
 #92.46642646577136
