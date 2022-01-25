import os
import pandas as pd
from numpy.random import randint
from PairFunctions import Test
from PairFunctions import Aggregate
import time

CLASSNUM = 19


def Classify(df, method, index):

    #Class Voting
    if method == 1:
        labelvalues = [0] * CLASSNUM
        indices = list(range(len(df['labels'])))
        indices.remove(index)
        tmpdf = df.copy()
        tmpdf.drop(indices, inplace=True)
        tmpdf.reset_index(drop = True, inplace=True)
        for j in range(CLASSNUM):
            for k in range(CLASSNUM):
                if j < k:
                    result = Test(j, k, tmpdf, 0)
                    if result == 0.5 or result == -0.5:
                        labelvalues[j] += 1
                        labelvalues[k] += 1
                    else:
                        labelvalues[j] += result
                        labelvalues[k] -= result
        result = list()
        max = 0
        for j in range(CLASSNUM):
            if max < labelvalues[j]:
                max = labelvalues[j]
        for j in range(CLASSNUM):
            if max == labelvalues[j]:
                result.append(j);
        if len(result) == 2:
            tmpresult = Test(result[0], result[1], df, index)
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
                        tmpresult = Test(result[i], result[j], df, index)
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
        return result

    #Eliminate Weakest
    if method == 2:
        indices = list(range(len(df['labels'])))
        indices.remove(index)
        tmpdf = df.copy()
        tmpdf.drop(indices, inplace=True)
        tmpdf.reset_index(drop = True, inplace=True)
        labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        for n in range(17):
            labelvalues = [0] * CLASSNUM
            for j in labels:
                for k in labels:
                    if j < k:
                        result = Test(j, k, tmpdf, 0)
                        if result == 0.5 or result == -0.5:
                            labelvalues[j] += 1
                            labelvalues[k] += 1
                        else:
                            labelvalues[j] += result
                            labelvalues[k] -= result
            min = 50
            minindex = 0
            for j in labels:
                if labelvalues[j] < min:
                    min = labelvalues[j]
                    minindex = j
            removelist = list()
            for j in labels:
                if labelvalues[j] == min:
                    removelist.append(j)
            if len(removelist) == len(labels):
                break;
            labels.remove(minindex)
        result = labels
        if len(result) == 2:
            tmpresult = Test(result[0], result[1], df, index)
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
                        tmpresult = Test(result[i], result[j], df, index)
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
        return result

    #Tourney
    if method == 3:
        repeatflag = 0
        labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        labelsize = len(labels)
        indices = list(range(len(df['labels'])))
        indices.remove(index)
        tmpdf = df.copy()
        tmpdf.drop(indices, inplace=True)
        tmpdf.reset_index(drop = True, inplace=True)
        while 1:
            if len(labels) == 1:
                break

            if labelsize > len(labels):
                repeatflag = 0
            if labelsize == len(labels):
                repeatflag += 1
            if labelsize == len(labels) and repeatflag == 5:
                break

            labelsize = len(labels)
            nextlabels = list()

            #Randomize labels in tourney
            for j in range(labelsize):
                r = randint(len(labels))
                nextlabels.append(labels[r])
                del labels[r]
            while len(nextlabels) > 1:
                if nextlabels[0] > nextlabels[1]:
                    tmp = nextlabels[0]
                    nextlabels[0] = nextlabels[1]
                    nextlabels[1] = tmp
                result = Test(nextlabels[0], nextlabels[1], tmpdf, 0)
                if result == 0 or result == -0.5 or result == 0.5:
                    labels.append(nextlabels[0])
                    labels.append(nextlabels[1])
                elif result == 1:
                    labels.append(nextlabels[0])
                elif result == -1:
                    labels.append(nextlabels[1])
                del nextlabels[0]
                del nextlabels[0]
            if len(nextlabels) == 1:
                labels.append(nextlabels[0])
        result = labels
        if len(result) > 2:
            result.sort()
            tmplength = len(result) + 1
            breakout = False
            while len(result) > 1:
                if tmplength == len(result):
                    break
                tmplength = len(result)
                for i in range(len(result) - 1):
                    for j in range(i + 1, len(result)):
                        tmpresult = Test(result[i], result[j], df, index)
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
        return result

    #Hybrid
    if method == 4:
        labelvalues = [0] * CLASSNUM
        indices = list(range(len(df['labels'])))
        indices.remove(index)
        tmpdf = df.copy()
        tmpdf.drop(indices, inplace=True)
        tmpdf.reset_index(drop = True, inplace=True)
        for j in range(CLASSNUM):
            for k in range(CLASSNUM):
                if j < k:
                    result = Test(j, k, tmpdf, 0)
                    if result == 0.5 or result == -0.5:
                        labelvalues[j] += 1
                        labelvalues[k] += 1
                    else:
                        labelvalues[j] += result
                        labelvalues[k] -= result
        labels = list()
        for k in range(5):
            result = 0
            max = 0
            for j in range(CLASSNUM):
                if max < labelvalues[j]:
                    result = j
                    max = labelvalues[j]
            labelvalues[result] = -22
            labels.append(result)

        labelsize = len(labels)
        repeatflag = 0
        while 1:
            if len(labels) == 1:
                break
            #Randomize labels in tourney
            if labelsize > len(labels):
                repeatflag = 0
            if labelsize == len(labels):
                repeatflag += 1
            if labelsize == len(labels) and repeatflag == 5:
                break
            labelsize = len(labels)
            nextlabels = list()
            for j in range(labelsize):
                r = randint(len(labels))
                nextlabels.append(labels[r])
                del labels[r]
            while len(nextlabels) > 1:
                if nextlabels[0] > nextlabels[1]:
                    tmp = nextlabels[0]
                    nextlabels[0] = nextlabels[1]
                    nextlabels[1] = tmp
                result = Test(nextlabels[0], nextlabels[1], tmpdf, 0)
                if result == 0 or result == -0.5 or result == 0.5:
                    labels.append(nextlabels[0])
                    labels.append(nextlabels[1])
                elif result == 1:
                    labels.append(nextlabels[0])
                elif result == -1:
                    labels.append(nextlabels[1])
                del nextlabels[0]
                del nextlabels[0]
            if len(nextlabels) == 1:
                labels.append(nextlabels[0])
        result = labels
        if len(result) > 2:
            result.sort()
            tmplength = len(result) + 1
            breakout = False
            while len(result) > 1:
                if tmplength == len(result):
                    break
                tmplength = len(result)
                for i in range(len(result) - 1):
                    for j in range(i + 1, len(result)):
                        tmpresult = Test(result[i], result[j], df, index)
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
        return result

def RunClassifier(df, method):
    labellist = list(df['labels'])
    success = 0
    multiclass = 0

    for i in range(len(labellist)):
        if (i % 2000) == 0:
            print("ticks: ", i)
        result = Classify(df, method, i)
        answer = labellist[i]

        if answer in result:
            success += 1
        if len(result) > 1:
            multiclass += 1
    accuracy = (success / len(labellist)) * 100
    multiclass = (multiclass / len(labellist)) * 100
    print("Accuracy:", accuracy)
    print("Multi:", multiclass)


traindf = pd.read_csv("data/exToptimizedtrain.csv")
testdf = pd.read_csv("data/exToptimizedtest.csv")

print("Finished reading in data")

#Update validfeatures with new featurelist
validfeatures = ['labels', '2654', '4366', '5979', '11658', '8543', '3066', '8177', '3076', '6598', '2901', '6075', '11405', '9186', '4929', '12127', '8061', '12181', '1314', '10572', '6762', '6908', '668', '12385', '6431', '2975', '10602', '5681', '3463', '5503', '11059', '923', '5703', '2625', '11019', '2981', '9935', '13300', '12868', '1742', '9131', '5522', '4401', '11003', '13621', '8893', '2797', '8956', '2638', '6566', '8173', '9804', '1543', '4223', '11450', '2090', '5384', '1780', '10439', '3578', '268', '2215', '12071', '9272', '13328', '7758', '6931', '3800', '540', '11582', '9254', '8973', '2745', '11864', '13255', '8091', '2600', '10002', '3387', '11347', '6735', '2604', '7134', '6629', '12160', '5547', '1226', '3161', '7213', '4848', '11311', '4322', '200', '4505', '9384', '9547', '1656', '8720', '2929', '4239', '12936', '7930', '1157', '3489', '6061', '13559', '9567', '9754', '5778', '212', '3363', '9530', '846', '7113', '2597', '3873', '10631', '11177', '5271', '1646', '12257', '9802', '8484', '13634', '12294', '6438', '12489', '12766', '4011', '8721', '8943', '1946', '5159', '7161', '8408', '6794', '11958', '5232', '2752', '5486', '6296', '179', '274', '4359', '5201', '8078', '13477', '7267', '4419', '12704', '13336', '13519', '3745', '1106', '13470', '9592', '10376', '9908', '9929', '9792', '5891', '1864', '801', '4847', '5999', '2821', '13397', '13237', '2874', '960', '1564', '3881', '6712', '8444', '3093', '5759', '13076', '4979', '6502', '977', '12925', '6367', '10391', '9856', '10683', '13199', '618', '2642', '93', '7460', '5651', '12801', '2661', '1980', '4734', '3983', '187', '5487', '4151', '1991', '11117', '9277', '1004', '13539', '5742', '6597', '10741', '2245', '5495', '4584', '4102', '6366', '4218', '28', '13028', '443', '1497', '240', '13088', '11532', '5718', '1200', '5076', '4440', '1732', '7721', '408', '11760', '966', '12122', '13082', '9408', '2118', '5443', '4482', '6118', '2137', '9822', '3254', '11928', '8510', '12662', '6136', '5335', '7494', '5093', '11932', '5183', '1112', '7749', '9534', '11271', '6775', '5780', '7729', '3405', '13556', '9162', '8490', '7964', '11681', '3853', '7708', '3847', '3597', '8723', '7179', '1358', '3234', '4812', '1394', '3353', '5497', '12171', '1600', '8962', '5791', '4317', '4224', '9578', '3692', '10045', '178', '10160', '13196', '1862', '6288', '8489', '2266', '2139', '7756', '1500', '9274', '8661', '9884', '1058', '8289', '584', '4085', '8285', '5843', '4197', '7414']


traindf = traindf.reindex(columns=validfeatures)
testdf = testdf.reindex(columns=validfeatures)


print("\n\n")
print("Class Voting")
print("Training:")
RunClassifier(traindf, 1)
print("\n")
print("Testing:")
RunClassifier(testdf, 1)

print("\n\n")
print("Victim Elimination")
print("Training:")
RunClassifier(traindf, 2)
print("\n")
print("Testing:")
RunClassifier(testdf, 2)

print("\n\n")
print("Tourney")
print("Training:")
RunClassifier(traindf, 3)
print("\n")
print("Testing:")
RunClassifier(testdf, 3)

print("\n\n")
print("Hybrid")
print("Training:")
RunClassifier(traindf, 4)
print("\n")
print("Testing:")
RunClassifier(testdf, 4)
