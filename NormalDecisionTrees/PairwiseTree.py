import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import tree
from PairFunctions import Test
from PairFunctions import Aggregate

#Initial test of how automated pairwise tree would compare to the maually created trees that were made
#Prints out the automated trees, calculates accuracies of both types, and compares them


#Implements decision tree based on the training and testing data given on the pair target1 and target2
def PairwiseTree(otraindf, otestdf, target1, target2):
    print("Starting pair ", target1, " and ", target2)

    #Takes a copy so the original is unaffected
    traindf = otraindf.copy()
    testdf = otestdf.copy()


    #eliminates all instances that don't belong to the pair for both training and testing sets
    elimlist = list()
    trainlabels = list(traindf['labels'])
    for i in range(len(trainlabels)):
        if trainlabels[i] != target1 and trainlabels[i] != target2:
            elimlist.append(i)
    traindf.drop(elimlist, inplace=True)
    traindf.reset_index(drop = True, inplace = True)

    elimlist = list()
    testlabels = list(testdf['labels'])
    for i in range(len(testlabels)):
        if testlabels[i] != target1 and testlabels[i] != target2:
            elimlist.append(i)
    testdf.drop(elimlist, inplace=True)
    testdf.reset_index(drop = True, inplace = True)

    feature_cols = list(traindf.columns)
    feature_cols.remove('labels')

    x_train = traindf[feature_cols].to_numpy()
    y_train = traindf['labels'].to_numpy()

    x_test = testdf[feature_cols].to_numpy()
    y_test = testdf['labels'].to_numpy()


    clf = DecisionTreeClassifier()
    clf = clf.fit(x_train,y_train)
    leaves = clf.get_n_leaves()
    non_leaves = clf.tree_.node_count - leaves


    y_pred = clf.predict(x_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)

    #Print out tree
    text_rep = tree.export_text(clf)
    print(text_rep)
    print("Leaves:", leaves)
    print("Non-Leaves:", non_leaves)


    return accuracy, leaves, non_leaves

#Classifies everying using the manual bounds processing and returns testing accuracy
def ManualTree(testdf, target1, target2):
    elimlist = list()
    testlabels = list(testdf['labels'])
    for i in range(len(testlabels)):
        if testlabels[i] != target1 and testlabels[i] != target2:
            elimlist.append(i)
    testdf.drop(elimlist, inplace=True)
    testdf.reset_index(drop = True, inplace = True)
    acc = 0
    for i in range(len(testdf['labels'])):
        result = Test(target1, target2, testdf, i)
        answer = -1
        if result == 1 or result == 0.5:
            answer = target1
        elif result == -1 or result == -0.5:
            answer = target2
        if(testdf['labels'].values[i] == answer):
            acc += 1
    return acc / len(testdf['labels'])





traindf = pd.read_csv("data/exToptimizedtrain.csv")
testdf = pd.read_csv("data/exToptimizedtest.csv")

print("Finished Loading data")


PairwiseTree(traindf, testdf, 0, 3)
PairwiseTree(traindf, testdf, 0, 15)
PairwiseTree(traindf, testdf, 1, 5)
PairwiseTree(traindf, testdf, 2, 18)
PairwiseTree(traindf, testdf, 12, 22)
PairwiseTree(traindf, testdf, 5, 22)

normalTree = list()
manualTree = list()
listCompare = list()
leaves = list()
non_leaves = list()


tie = 0
manualwins = 0
normalwins = 0

#Iterates over all pairs
for i in range(23):
    for j in range(i + 1, 23):
        print("\n\n\n")
        p, l, nl = PairwiseTree(traindf, testdf, i, j)
        leaves.append(l)
        non_leaves.append(nl)
        normalTree.append(p)


        m = ManualTree(testdf.copy(), i, j)
        manualTree.append(m)


        c = p - m
        listCompare.append(c)


        print("Automated:",p)
        print("Manual",m)
        print("Compare:", c)


        if c == 0:
            tie += 1
        elif c > 0:
            normalwins += 1
        elif c < 0:
            manualwins += 1


print("normal")
print(normalTree)
print("\n\n\nmanual")
print(manualTree)
print("\n\n\ncomparison")
print(listCompare)

print("normal wins:", normalwins)
print("manual wins:", manualwins)
print("ties:", tie)

print("leaves:", leaves)
print("\n\nnon-leaves", non_leaves)


sum = 0
for i in range(len(leaves)):
    sum += leaves[i]
print("Number of leaves:", sum)
print("Average per pair:", sum / len(leaves))


sum = 0
for i in range(len(non_leaves)):
    sum += non_leaves[i]
print("\n\nNumber of non-leaves:", sum)
print("Average per pair:", sum / len(non_leaves))
