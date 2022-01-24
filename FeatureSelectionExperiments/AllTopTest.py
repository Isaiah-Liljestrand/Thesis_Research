import os, sys

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from numpy.random import randint

def RunNeuralNet(df, namelist, Y)
    smalldf = df.copy()
    smalldf = smalldf.reindex(columns=namelist)

    X_train, X_test, Y_train, Y_test = train_test_split(smalldf, Y, test_size = 0.2)

    model = Sequential()
    model.add(Dense(1024, activation="relu", input_dim = X_train.shape[1]))
    model.add(Dense(512, activation="relu"))
    model.add(Dense(200, activation="relu"))
    model.add(Dense(Y_train.shape[1], activation="softmax"))

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=['categorical_crossentropy','accuracy'])

    model.fit(X_train, Y_train, validation_data=(X_test, Y_test), verbose=1, epochs=25, shuffle=True)

    predicted = np.argmax(model.predict(X_test), axis=1)
    valid = np.argmax(Y_test, axis=1)
    accuracy = 0
    test_range = len(valid)
    for k in range(test_range):
        if predicted[k] == valid[k]:
            accuracy += 1

    return accuracy / test_range


df = pd.read_csv("data/exToptimized.csv")
inddf = pd.read_csv("data/One-vs-allInformationGain.csv")
igdf = pd.read_csv("data/InformationGain.csv")
pairdf = pd.read_csv("data/PairInfoGainValues.csv")

print("Initialized dataframes")

IGlength = len(inddf[inddf.columns[0]])

sumlist = [0] * IGlength

for j in range(len(inddf.columns) - 1):
    copylist = inddf[inddf.columns[j + 1]].copy()
    for i in range(IGlength):
        sumlist[i] += copylist[i]
print("Finished sum list")

pairsumlist = [0] * IGlength

for j in range(len(pairdf.columns) - 1):
    copylist = pairdf[pairdf.columns[j + 1]].copy()
    for i in range(IGlength):
        pairsumlist[i] += copylist[i]
print("Finished pair sum list")

Y = df.pop('labels')
Y = to_categorical(Y)
scaler = StandardScaler()

indacc = list()
indsumacc = list()
igacc = list()
randacc = list()
pairsumacc = list()
counter = 0
kvalue = 10
testquantity = 5

for i in range(kvalue):
    tmpindacc = 0
    tmpindsumacc = 0
    tmpigacc = 0
    tmprandacc = 0
    tmppairsumacc = 0
    for j in range(testquantity):

        #Individual Selection
        namelist = list()
        for k in range(len(inddf.columns) - 1):
            editlist = list(inddf[inddf.columns[k + 1]].copy())
            max = 0
            maxindex = -1
            for n in range(i + 1):
                max = 0
                maxindex = -1
                for l in range(len(editlist)):
                    if editlist[l] > max:
                        maxindex = l
                        max = editlist[l]
                editlist[maxindex] = 0
                while inddf[inddf.columns[0]][maxindex] in namelist:
                    print("Found duplicate, k = ", k)
                    max = 0
                    maxindex = -1
                    for l in range(len(editlist)):
                        if editlist[l] > max:
                            maxindex = l
                            max = editlist[l]
                    editlist[maxindex] = 0
                namelist.append(inddf[inddf.columns[0]][maxindex])


        tmpindacc += RunNeuralNet(df, namelist, Y)
        print("Individual accuracy = ", accuracy / test_range)
        print("Number of features in use = ", (i + 1) * 23)

        counter += 1
        print("Progress:", counter, " / 250")




        #Random Selection
        namelist = list()
        for k in range((i + 1) * 23):
            name = df.columns[randint(len(df.columns))]
            while name in namelist:
                name = df.columns[randint(len(df.columns))]
            namelist.append(name)

        tmprandacc += RunNeuralNet(df, namelist, Y)
        print("Random accuracy = ", accuracy / test_range)
        print("Number of features in use = ", (i + 1) * 23)

        counter += 1
        print("Progress:", counter, " / 250")



        #Individual Sum Selection
        namelist = list()
        editlist = sumlist.copy()
        for k in range((i + 1) * 23):
            max = 0
            maxindex = -1
            for n in range(IGlength):
                if editlist[n] > max:
                    max = editlist[n]
                    maxindex = n
            editlist[maxindex] = -1
            namelist.append(inddf['Features'][maxindex])

        tmpindsumacc += RunNeuralNet(df, namelist, Y)
        print("Individual sum accuracy = ", accuracy / test_range)
        print("Number of features in use = ", (i + 1) * 23)

        counter += 1
        print("Progress:", counter, " / 250")


        #Information Gain Selection
        namelist = list()
        editlist = list(igdf['InformationGain'].copy())
        for k in range((i + 1) * 23):
            max = 0
            maxindex = -1
            for n in range(IGlength):
                if editlist[n] > max:
                    max = editlist[n]
                    maxindex = n
            editlist[maxindex] = -1
            namelist.append(igdf['Features'][maxindex])

        tmpigacc += RunNeuralNet(df, namelist, Y)
        print("Information gain accuracy = ", accuracy / test_range)
        print("Number of features in use = ", (i + 1) * 23)

        counter += 1
        print("Progress:", counter, " / 250")



        #Pair Sum Selection
        namelist = list()
        editlist = pairsumlist.copy()
        for k in range((i + 1) * 23):
            max = 0
            maxindex = -1
            for n in range(IGlength):
                if editlist[n] > max:
                    max = editlist[n]
                    maxindex = n
            editlist[maxindex] = -1
            namelist.append(pairdf['Features'][maxindex])

        tmppairsumacc += RunNeuralNet(df, namelist, Y)
        print("Pair sum accuracy = ", accuracy / test_range)
        print("Number of features in use = ", (i + 1) * 23)

        counter += 1
        print("Progress:", counter, " / 250")

    igacc.append(tmpigacc / testquantity)
    indsumacc.append(tmpindsumacc / testquantity)
    indacc.append(tmpindacc / testquantity)
    randacc.append(tmprandacc / testquantity)
    pairsumacc.append(tmppairsumacc / testquantity)

print("All done. Printing data")
print("Individual Accuracy:", indacc)
print("Individual Sum Accuracy:", indsumacc)
print("Random Accuracy:", randacc)
print("Information Gain Accuracy:", igacc)
print("Pair Sum Accuracy:", pairsumacc)

outputdf = pd.DataFrame()
outputdf['Individual'] = indacc
outputdf['Random'] = randacc
outputdf['IndividualSum'] = indsumacc
outputdf['InformationGain'] = igacc
outputdf['PairSum'] = pairsumacc
outputdf.to_csv("Results/TopTestResults.csv", index = False)

#old results using SU
#Individual Accuracy: [0.719333768778576, 0.8534291312867406, 0.8943827563683866, 0.9094709340300458, 0.9214239059438276, 0.9242325277596342, 0.934944480731548, 0.9367733507511431, 0.9442194644023513, 0.94101894186806]
#Random Accuracy: [0.7983017635532332, 0.8765512736773351, 0.9077073807968647, 0.9174395819725669, 0.9207707380796866, 0.9312214239059438, 0.9354016982364468, 0.9418680600914435, 0.9377531025473547, 0.9411495754408883]
#Sum Accuracy: [0.8574134552580013, 0.8977792292619202, 0.9188765512736772, 0.927694317439582, 0.9293925538863487, 0.9440888308295232, 0.9444154147615936, 0.9459830176355324, 0.9455911169170477, 0.9495754408883084]
#Regular Accuracy: [0.862050947093403, 0.9062704114957544, 0.9249510124101894, 0.9344219464402352, 0.9292619203135206, 0.9329849771391248, 0.9435009797517961, 0.9466361854996734, 0.9468321358589158, 0.946374918354017]


#New Results
#Individual Accuracy: [0.9137818419333769, 0.9365774003919007, 0.9465708687132592, 0.95532331809275, 0.9597648595689092, 0.9531678641410842, 0.959046374918354, 0.9591116917047682, 0.9604180274330503, 0.9619856303069889]
#Individual Sum Accuracy: [0.8902677988242977, 0.9278902677988243, 0.9397779229261921, 0.9425212279555846, 0.94689745264533, 0.9478118876551275, 0.9497060744611365, 0.9541476159372959, 0.9546048334421947, 0.9558458523840626]
#Random Accuracy: [0.8166557805355976, 0.8916394513389942, 0.9166557805355977, 0.9318745917700848, 0.9337687785760942, 0.9329849771391248, 0.943370346178968, 0.9471587197909862, 0.9465708687132594, 0.9523840627041149]
#Information Gain Accuracy: [0.8925538863487915, 0.9242978445460484, 0.9310907903331156, 0.9417374265186153, 0.9481384715871979, 0.9465708687132592, 0.9463096015676029, 0.9491835401698238, 0.9533638145003266, 0.9540169823644676]
#Pair Sum Accuracy: [0.8798824297844547, 0.9135858915741345, 0.9293272370999347, 0.9316786414108427, 0.9407576747224036, 0.9452645329849771, 0.9518615284128021, 0.9480731548007839, 0.952449379490529, 0.9518615284128021]


#Newest Results
#Individual Accuracy: [0.9080339647289353, 0.9331156107119529, 0.9433050293925538, 0.9480731548007839, 0.9541476159372959, 0.9593729588504246, 0.9600261267145657, 0.962704114957544, 0.9603527106466363, 0.9614630960156761]
#Individual Sum Accuracy: [0.8913781841933377, 0.9198563030698889, 0.9333115610711953, 0.9340300457217505, 0.9426518615284127, 0.9450032658393207, 0.9459177008491182, 0.9534291312867407, 0.9527106466361855, 0.953690398432397]
#Random Accuracy: [0.8243631613324623, 0.9015022860875245, 0.9151534944480731, 0.9272370999346832, 0.9359895493141737, 0.9410842586544742, 0.9439581972566948, 0.9418027433050293, 0.946440235140431, 0.9494448073154802]
#Information Gain Accuracy: [0.8824951012410189, 0.9220770738079687, 0.934879163945134, 0.9333768778576095, 0.9468974526453298, 0.9478118876551275, 0.9481384715871979, 0.9495754408883084, 0.949967341606793, 0.947615937295885]
#Pair Sum Accuracy: [0.8745264532984978, 0.9129327237099936, 0.9290006531678641, 0.9391900718484651, 0.9367080339647289, 0.943305029392554, 0.9416067929457871, 0.9493141737426518, 0.9496407576747223, 0.9449379490529066]
