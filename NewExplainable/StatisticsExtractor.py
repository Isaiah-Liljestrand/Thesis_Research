import os
import pandas as pd
from numpy.random import randint
from PairFunctions import Test
from PairFunctions import Aggregate

def Classify(df, method, index):

    #Class Voting
    if method == 1:
        indices = list(range(len(df['labels'])))
        indices.remove(index)
        tmpdf = df.copy()
        tmpdf.drop(indices, inplace=True)
        tmpdf.reset_index(drop = True, inplace=True)
        tmp = list(tmpdf['labels'])[0]
        for j in range(23):
            for k in range(23):
                if j == tmp or k == tmp:
                    if j < k:
                        result = Test(j, k, tmpdf, 0)
                        if result == 0.5 or result == -0.5:
                            return True
        return False


#traindf = pd.read_csv("data/exToptimizedtrain.csv")
testdf = pd.read_csv("data/exToptimizedtest.csv")

print("Finished reading in data")

validfeatures = ['labels', '2654', '4366', '5979', '11658', '8543', '3066', '8177', '3076', '6598', '2901', '6075', '11405', '9186', '4929', '12127', '8061', '12181', '1314', '10572', '6762', '6908', '668', '12385', '6431', '2975', '10602', '5681', '3463', '5503', '11059', '923', '5703', '2625', '11019', '2981', '9935', '13300', '12868', '1742', '9131', '5522', '4401', '11003', '13621', '8893', '2797', '8956', '2638', '6566', '8173', '9804', '1543', '4223', '11450', '2090', '5384', '1780', '10439', '3578', '268', '2215', '12071', '9272', '13328', '7758', '6931', '3800', '540', '11582', '9254', '8973', '2745', '11864', '13255', '8091', '2600', '10002', '3387', '11347', '6735', '2604', '7134', '6629', '12160', '5547', '1226', '3161', '7213', '4848', '11311', '4322', '200', '4505', '9384', '9547', '1656', '8720', '2929', '4239', '12936', '7930', '1157', '3489', '6061', '13559', '9567', '9754', '5778', '212', '3363', '9530', '846', '7113', '2597', '3873', '10631', '11177', '5271', '1646', '12257', '9802', '8484', '13634', '12294', '6438', '12489', '12766', '4011', '8721', '8943', '1946', '5159', '7161', '8408', '6794', '11958', '5232', '2752', '5486', '6296', '179', '274', '4359', '5201', '8078', '13477', '7267', '4419', '12704', '13336', '13519', '3745', '1106', '13470', '9592', '10376', '9908', '9929', '9792', '5891', '1864', '801', '4847', '5999', '2821', '13397', '13237', '2874', '960', '1564', '3881', '6712', '8444', '3093', '5759', '13076', '4979', '6502', '977', '12925', '6367', '10391', '9856', '10683', '13199', '618', '2642', '93', '7460', '5651', '12801', '2661', '1980', '4734', '3983', '187', '5487', '4151', '1991', '11117', '9277', '1004', '13539', '5742', '6597', '10741', '2245', '5495', '4584', '4102', '6366', '4218', '28', '13028', '443', '1497', '240', '13088', '11532', '5718', '1200', '5076', '4440', '1732', '7721', '408', '11760', '966', '12122', '13082', '9408', '2118', '5443', '4482', '6118', '2137', '9822', '3254', '11928', '8510', '12662', '6136', '5335', '7494', '5093', '11932', '5183', '1112', '7749', '9534', '11271', '6775', '5780', '7729', '3405', '13556', '9162', '8490', '7964', '11681', '3853', '7708', '3847', '3597', '8723', '7179', '1358', '3234', '4812', '1394', '3353', '5497', '12171', '1600', '8962', '5791', '4317', '4224', '9578', '3692', '10045', '178', '10160', '13196', '1862', '6288', '8489', '2266', '2139', '7756', '1500', '9274', '8661', '9884', '1058', '8289', '584', '4085', '8285', '5843', '4197', '7414']

#traindf = traindf.reindex(columns=validfeatures)
testdf = testdf.reindex(columns=validfeatures)

totallist = list()
multilist = list()
acclist = list()
multilistp = list()

total = 0
acc = 0
multi = 0
for i in range(19):
    for j in range(i + 1, 19):
        print("Starting pair", i, " and ", j)
        tmptotal = 0
        tmpmulti = 0
        tmpacc = 0
        tmptestdf = testdf.copy()
        labellist = tmptestdf['labels']
        elimlist = list()
        for k in range(len(labellist)):
            if labellist[k] != i and labellist[k] != j:
                elimlist.append(k)
        tmptestdf.drop(elimlist, inplace=True)
        tmptestdf.reset_index(drop = True, inplace = True)
        for k in range(len(tmptestdf['labels'])):
            result = Test(i, j, tmptestdf, k)
            total += 1
            tmptotal += 1
            if result == 0.5 or result == -0.5:
                multi += 1
                tmpmulti += 1
                tmpacc += 1
                acc += 1
            if result == 1 and list(tmptestdf['labels'])[k] == i:
                tmpacc += 1
                acc += 1
            if result == -1 and list(tmptestdf['labels'])[k] == j:
                tmpacc += 1
                acc += 1
        totallist.append(tmptotal)
        acclist.append((tmpacc / tmptotal) * 100)
        multilist.append(tmpmulti)
        multilistp.append((tmpmulti / tmptotal) * 100)
        print("Accuracy:", ((tmpacc / tmptotal) * 100))

print("total:",total)
print("multi:",multi)
print("acc:",acc / total)

print("totallist:", totallist)
print("\n\nmultilist:", multilist)
print("\n\nacclist:", acclist)
print("\n\nmultilistp:", multilistp)
print("\n\n")

total = 0
multi = 0
acc = 0

acc100 = 0
acc99 = 0
acc98 = 0
acc97 = 0
acc96 = 0
acc90 = 0

multi0 = 0
multi5 = 0
multi10 = 0

for i in range(len(totallist)):
    total += totallist[i]
    acc += acclist[i]
    multi += multilist[i]
    if multilist[i] == 0:
        multi0 += 1
    if multilist[i] / totallist[i] < 0.05:
        multi5 += 1
    if multilist[i] / totallist[i] < 0.1:
        multi10 += 1
    tmpacc = acclist[i]
    if tmpacc == 100:
        acc100 += 1
    if tmpacc >= 99:
        acc99 += 1
    if tmpacc >= 98:
        acc98 += 1
    if tmpacc >= 97:
        acc97 += 1
    if tmpacc >= 96:
        acc96 += 1
    if tmpacc >= 90:
        acc90 += 1

print("\n\nAverage total:", total / 171)
print("Average acc:", acc / 171)
print("Average multi:", multi / 171)

print("Average multi divided by total:", multi / total)

print("acc100:", acc100 / 171, "   ", acc100)
print("acc99:", acc99 / 171, "   ", acc99)
print("acc98:", acc98 / 171, "   ", acc98)
print("acc97:", acc97 / 171, "   ", acc97)
print("acc96:", acc96 / 171, "   ", acc96)
print("acc90:", acc90 / 171, "   ", acc90)

print("multi0:", multi0 / 171, "   ", multi0)
print("multi5:", multi5 / 171, "   ", multi5)
print("multi10:", multi10 / 171, "   ", multi10)
