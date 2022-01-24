import os, sys

import pandas as pd

import numpy as np
from math import isnan
from math import trunc
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from numpy.random import randint


#Read in data and format labels
df = pd.read_csv("../../data/exT.csv")
df = df.rename(columns={'Unnamed: 0':'labels'})
df['labels'] = df['labels'].apply(lambda x: x.split(".")[0])

#labels that will be eliminated due to insufficient quantitities.
elimlabels = ['Pelvis', 'Nervous', 'Fallopian', 'Mediastinum', 'Bile', 'Ocular', 'Pleura', 'Bone', 'Thymus', 'Rectum', 'none']

#Number of rows
length = df.shape[0]

#Eliminating rows
elimlist = list()
for l in elimlabels:
    print("Eliminating ", l)
    for i in range(length):
        if df['labels'].values[i] == l:
            elimlist.append(i)
print("Rows to be eliminated:", elimlist)
df.drop(elimlist, inplace=True)
print("Resulting dataframe:")
print(df)
df.reset_index(drop = True, inplace=True)

#Transforming labels into integers
df['labels'] = LabelEncoder().fit_transform(df['labels'])


#Removing pointless columns
print("removing columns with all 0")
k = 0
for i in range(1, len(df.columns)):
    k += 1
    columnlist = list(df[df.columns[k]])
    flag = 1
    print(k)
    for j in range(len(columnlist)):
        if columnlist[j] != 0:
            flag = 0
            break
    if flag:
        print("Removing column ", k)
        df.drop(df.columns[k], axis = 1, inplace = True)
        k -= 1


k = 0
print("Applying log2 to all values")
for l in df.columns:
    if l == 'labels':
        continue
    editlist = list(df[l].copy())
    for i in range(len(editlist)):
        editlist[i] = np.log2(editlist[i] + 0.1)
    df[l] = editlist.copy()
    print("log progress:", k)
    k += 1

print("Finished applying log2")



#Start testing training split here
print("Starting to split data into training and testing sets")
testdfindices = list()
labellist = list(df['labels'])
for i in range(23):
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



#print("Applying normalization")
#column_names = df.columns[1:]
#trainfeatures = df[column_names]
#testfeatures = testdf[column_names]
#scaler = StandardScaler()
#newtrainfeatures = scaler.fit_transform(trainfeatures.values)
#newtestfeatures = scaler.transform(testfeatures.values)
#df[column_names] = newtrainfeatures
#testdf[column_names] = newtestfeatures
#print("Normalization complete")



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
