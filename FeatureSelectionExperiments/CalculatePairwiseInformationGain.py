#import os, sys

import struct
import pandas as pd
import numpy as np
from math import log2
from math import isnan
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import csv


def PairHandler(df, label, label2):
    print("Starting to process pair ", label, " ", label2)
    classlist = list()
    tmplabel = list(df['labels'])

    for i in range(len(tmplabel)):
        if tmplabel[i] == label:
            classlist.append(1)
        elif tmplabel[i] == label2:
            classlist.append(0)
    classnum = 2
    classprob = [0] * classnum
    for l in classlist:
        classprob[l] += 1
    classentropy = 0
    for i in range(classnum):
        classprob[i] = classprob[i] / len(classlist)
        classentropy -= classprob[i] * log2(classprob[i])
    infoGainlist = list()
    #Get list of SU values between each feature and classification
    for i in range(1, len(df.columns)):
        featurelist = list()
        tmpfeature = list(df[df.columns[i]])
        for k in range(len(tmplabel)):
            if (tmplabel[k] == label) or (tmplabel[k] == label2):
                featurelist.append(tmpfeature[k])
        infoGainlist.append(InfoGain(list(LabelEncoder().fit_transform(featurelist)), classlist, classentropy))
        print("label1 = ", label, " \tlabel2 = ", label2, "\ti =", i - 1, "\tInfoGain = ", infoGainlist[i - 1])
    return infoGainlist

def InfoGain(feature, classlist, classentropy):
    featurenum = len(np.unique(feature))
    classnum = len(np.unique(classlist))
    length = len(feature)

    entropy = 0
    for i in range(featurenum):
        featurecount = 0
        for j in range(length):
            if feature[j] == i:
                featurecount += 1
        for c in range(classnum):
            cellentropy = 0
            count = 0
            for j in range(length):
                if (feature[j] == i) and (classlist[j] == c):
                    count += 1
            if count != 0:
                ratio = count / featurecount
                cellentropy -= ratio * log2(ratio)
                entropy += cellentropy * (featurecount / length)
    return classentropy - entropy

df = pd.read_csv("data/bindata.csv")

print("starting")
num_labels = len(np.unique(df['labels']))


pairsdf = pd.DataFrame()
pairsdf['Features'] = df.columns[1:]

i = 0

for l in range(num_labels):
    for k in range(num_labels):
        if k > l:
            pairsdf[str(i)] = PairHandler(df, l, k).copy()
            i += 1

print(pairsdf)


print("Starting to write infoGain to file")
pairsdf.to_csv("data/PairInfoGainValues.csv", index = False)
