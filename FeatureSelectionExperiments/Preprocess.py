import os, sys

import pandas as pd

import numpy as np
from math import isnan
from math import trunc
from keras.utils import to_categorical
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from numpy.random import randint


#Read in data and format labels
df = pd.read_csv("../data/exT.csv")
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


#print("Applying normalization")
#column_names = df.columns[1:]
#features = df[column_names]
#newfeatures = StandardScaler().fit_transform(features.values)
#df[column_names] = newfeatures
#print("Finished nomalization")


#Handle binning
print("Starting binning")
bindf = df.copy()
print("Finished copying dataframe")
for col in range(1, len(bindf.columns)):

    #Simply use cut function for equal width binning.
    bindf[bindf.columns[col]], bins = pd.cut(list(df[df.columns[col]]), bins = 20, retbins = True, labels = False, duplicates = 'drop')
    print("Binning:", col)


print(bindf)
print("Starting to write")
df.to_csv('data/exToptimized.csv', index = False)
print("Between writing")
bindf.to_csv('data/bindata.csv', index = False)
print("Done writing")
