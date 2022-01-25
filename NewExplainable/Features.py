import pandas as pd
#Counts and prints the number of features used in the pairwise classifier

featurelist = list()

originaldf = pd.read_csv("data/TCGA.NMJ123.log.csv")
originalfeatures = list(originaldf[originaldf.columns[0]])

mappingdf = pd.read_csv("data/featuremappings.csv")
maplist = list(mappingdf['record'])
del maplist[0]

def Translate(numstring):
    for i in range(len(maplist)):
        if numstring == maplist[i]:
            return originalfeatures[i]
    print("never caught feature")


#First run does not remove duplicates, just adds all features
tmpstring = ''
flag = 0
file = open('PairFunctions.py', 'r')
for line in file.readlines():
    for c in line:
        if c == '\'' and flag == 1:
            flag = 0
            featurelist.append(Translate(tmpstring))
            tmpstring = ''
            continue
        if c == '\'' and flag == 0:
            flag = 1
            continue
        if flag:
            tmpstring += c
#print(featurelist)
print("Number of Features without removing duplicates:", len(featurelist))
print("Average number of features:", len(featurelist) / 253)

#Second run removes duplicates
elimnum = 0
newfeaturelist = list()
bestfeaturelist = list()
bestfeaturecounts = list()
length = len(featurelist)
for i in range(len(featurelist)):
    if featurelist[i] in newfeaturelist:
        flag = 0
        for j in range(len(bestfeaturelist)):
            if bestfeaturelist[j] == featurelist[i]:
                bestfeaturecounts[j] += 1
                flag = 1
                break
        if not flag:
            bestfeaturelist.append(featurelist[i])
            bestfeaturecounts.append(2)
        continue
    newfeaturelist.append(featurelist[i])

featuredf = pd.DataFrame()
featuredf['Features'] = newfeaturelist
featuredf.to_csv("FeatureOutput/Total_features_no_duplicates.csv")
print("List of non-duplicating features\n")
print(newfeaturelist)
print("Number of non-duplicating Features:", len(newfeaturelist))

topfeaturesdf = pd.read_csv("../Top Feature Analysis/Top.genes.new.csv", index_col = False)

toplist = list(topfeaturesdf['gene'])
overlap = list()
for i in range(len(toplist)):
    if toplist[i] in newfeaturelist:
        overlap.append(toplist[i])
print(overlap)
print(len(overlap))



for i in range(19):
    validtree = 0
    featurelist = list()
    file = open('PairFunctions.py', 'r')
    for line in file.readlines():

        #check if this is a tree start
        treestart = 0
        flag = 0
        for c in line:
            if c == 'i':
                flag = 1
                tmpstring = ''
            if flag == 1:
                tmpstring += c
                if tmpstring == 'if l1 ==':
                    treestart = 1
                    break
                if len(tmpstring) > 8:
                    break

        #check if the tree involves target label
        if treestart:
            tmpstring = ' ' + str(i) + ' '
            tmpstring2 = ' ' + str(i) + ':'
            if tmpstring in line or tmpstring2 in line:
                validtree = 1
            else:
                validtree = 0
            continue

        #record features
        if validtree:
            flag = 0
            for c in line:
                if c == '\'' and flag == 0:
                    tmpstring = ''
                    flag = 1
                    continue
                if c == '\'' and flag == 1:
                    flag = 0
                    featurelist.append(Translate(tmpstring))
                    continue
                if flag:
                    tmpstring += c

    newfeaturelist = list()
    for j in range(len(featurelist)):
        if featurelist[j] not in newfeaturelist:
            newfeaturelist.append(featurelist[j])
    featurelist = newfeaturelist


    print("\n\nFeatures used for label ", i)
    print(featurelist)
    print("Number of features: " + str(len(featurelist)))
    featuredf = pd.DataFrame()
    featuredf['Features'] = featurelist

    #for top in toplist:
    #    if top in featurelist:
    #        print("Found here:", top)
    featuredf.to_csv("FeatureOutput/Features_used_for_" + str(i) + ".csv")
