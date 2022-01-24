import os, sys

import struct
import pandas as pd
import numpy as np
from math import log2
from math import isnan
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import csv


def runner(df, label, pipe):
    print("Starting to process label ", label)
    classlist = list()
    for i in range(len(df['labels'])):
        if df['labels'].values[i] == label:
            classlist.append(1)
        else:
            classlist.append(0)
    classnum = 2
    classprob = [0] * classnum
    for l in classlist:
        classprob[l] += 1
    classentropy = 0
    for i in range(classnum):
        classprob[i] = classprob[i] / len(df['labels'])
        classentropy -= classprob[i] * log2(classprob[i])

    IGlist = list()
    #Get list of SU values between each feature and classification

    for i in range(1, len(df.columns)):
        IGlist.append(InfoGain(list(LabelEncoder().fit_transform(df[df.columns[i]])), classlist, classentropy))
        print("label = ", label, "  \ti =", i - 1, "\tIG =", IGlist[i - 1])
    IGlist.append(-1.1)
    for i in range(len(IGlist)):
        os.write(pipe, bytearray(struct.pack("f", IGlist[i])))
    print("Child ", label, " finished writing ", IGlist)
    os._exit(0)

def InfoGain(featurelist, classlist, classentropy):
    featurenum = len(np.unique(featurelist))
    classnum = len(np.unique(classlist))
    length = len(featurelist)

    entropy = 0
    for i in range(featurenum):
        featurecount = 0
        for j in range(length):
            if featurelist[j] == i:
                featurecount += 1
        for c in range(classnum):
            cellentropy = 0
            count = 0
            for j in range(length):
                if (featurelist[j] == i) and (classlist[j] == c):
                    count += 1
            if count != 0:
                ratio = count / featurecount
                cellentropy -= ratio * log2(ratio)
                entropy += cellentropy * (featurecount / length)
    return classentropy - entropy

df = pd.read_csv("data/bindata.csv")

print("starting")
all_labels = np.unique(df['labels'])

IGdf = pd.DataFrame()

rowNum = len(df['labels'])

rec_pipe = [0] * len(all_labels)
send_pipe = [0] * len(all_labels)
i = 0

for l in all_labels:
    rec_pipe[i], send_pipe[i] = os.pipe()

    if os.fork() == 0:
        for j in range(i + 1):
            os.close(rec_pipe[j])
        runner(df, l, send_pipe[i])
    else:
        os.close(send_pipe[i])
    i += 1



print("All children created")

i = 0

IGdf['Features'] = df.columns[1:]

print(IGdf)
print(df)

print("Parent passed")
#copy IG lists from children
for l in all_labels:
    IGlist = list()
    while True:
        tmp = struct.unpack("f", os.read(rec_pipe[i], 4))[0]
        print("Parent recieved IG ", tmp)
        if tmp < 0:
            break
        else:
            IGlist.append(tmp)
    IGdf[l] = IGlist
    i += 1



print("Starting to write Information Gain to file")
IGdf.to_csv("data/One-vs-allInformationGain.csv", index = False)
print("Finished writing features to file - Starting overall IG calculation")


#calculate class properties for Information Gain
classlength = len(df['labels'])
classnum = len(np.unique(df['labels']))
classprob = [0] * classnum
for i in df['labels']:
    classprob[i] += 1
classentropy = 0
for i in range(classnum):
    classprob[i] = classprob[i] / classlength
    classentropy -= classprob[i] * log2(classprob[i])

#Get list of IG values between each feature and classification
IGlist = [0] * len(IGdf['Features'])
for i in range(len(IGdf['Features'])):
    IGlist[i] = InfoGain(list(LabelEncoder().fit_transform(df[df.columns[i + 1]])), list(df['labels']), classentropy)
    print(i)
overallIGdf = pd.DataFrame()
overallIGdf['Features'] = IGdf['Features'].copy()
overallIGdf['InformationGain'] = IGlist.copy()
overallIGdf.to_csv("data/InformationGain.csv", index = False)
