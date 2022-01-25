import os, sys

import pandas as pd

import numpy as np
from math import isnan
from math import trunc
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from numpy.random import randint


#Read in data and format labels
df = pd.read_csv("data/TCGA.NMJ123.log.csv")
df.set_index('X',inplace=True)
df = df.T

df.reset_index(inplace=True)
df = df.rename(columns={df.columns[0]:'labels'})
print(df)
df['labels'] = df['labels'].apply(lambda x: x.split(".")[0])

df.index.rename(' ', inplace=True)

#Transforming labels into integers
df['labels'] = LabelEncoder().fit_transform(df['labels'])
print(df)

#Mapping genes to integers
columnnum = len(df.columns) - 1
integerlist = list(range(1, columnnum + 1))
recordlist = list()
recordlist.append('labels')
for i in range(columnnum):
    if i % 20 == 0:
        print(i)
    r = randint(len(integerlist))
    n = integerlist[r]
    recordlist.append(n)
    del integerlist[r]
    df = df.rename(columns={df.columns[i + 1]: str(n)})
print(df)

recorddf = pd.DataFrame()
recorddf['record'] = recordlist
recorddf.to_csv("data/featuremappings.csv")

testdfindices = list()

#Start testing training split here
print("Starting to split data into training and testing sets")
labellist = list(df['labels'])
for i in range(len(np.unique(list(df['labels'])))):
    indexlist = list()
    for j in range(len(labellist)):
        if labellist[j] == i:
            indexlist.append(j)
    testcount = trunc(0.2 * len(indexlist))
    for j in range(testcount):
        randomindex = randint(len(indexlist))
        testdfindices.append(indexlist[randomindex])
        indexlist.remove(indexlist[randomindex])
testdf = df.copy()

df.drop(testdfindices, inplace=True)
df.reset_index(drop = True, inplace=True)

totalindices = list(range(len(testdf['labels'])))
for i in testdfindices:
    totalindices.remove(i)
testdf.drop(totalindices, inplace=True)
testdf.reset_index(drop = True, inplace=True)

print("Testdfindices:")
print(testdfindices)

print("\n\n\nTraining")
print(df)
print("\n\n\nTesting")
print(testdf)




#Handle X binning
print("Starting binning")
bindf = df.copy()
print("Finished copying dataframe")
for col in range(1, len(bindf.columns)):

    #Simply use cut function for equal width binning.
    bindf[bindf.columns[col]], bins = pd.cut(list(df[df.columns[col]]), bins = 20, retbins = True, labels = False, duplicates = 'drop')
    print("Binning:", col)




print("Starting to write exToptimized.csv")
df.to_csv('data/exToptimizedtrain.csv', index = False)
print("Starting to write bindata.csv")
bindf.to_csv('data/trainbindata.csv', index = False)
print("Starting to write exToptimizedtest.csv")
testdf.to_csv('data/exToptimizedtest.csv', index = False)
print("Done writing")
print("Again, test indices:")
print(testdfindices)
