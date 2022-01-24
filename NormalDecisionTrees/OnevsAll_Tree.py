import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import tree

#Test of qualities and accuracies of automated one-vs-all trees


#Implements decision tree based on the training and testing data given one label: target
def IndividualTree(otraindf, otestdf, target):
    print("Starting label ", target)

    #Takes a copy so the original is unaffected
    traindf = otraindf.copy()
    testdf = otestdf.copy()

    trainlist = list(traindf['labels'])
    testlist = list(testdf['labels'])

    for i in range(len(trainlist)):
        if trainlist[i] == target:
            trainlist[i] = 1
        else:
            trainlist[i] = 0
    traindf['labels'] = trainlist

    for i in range(len(testlist)):
        if testlist[i] == target:
            testlist[i] = 1
        else:
            testlist[i] = 0
    testdf['labels'] = testlist

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


traindf = pd.read_csv("data/exToptimizedtrain.csv")
testdf = pd.read_csv("data/exToptimizedtest.csv")

print("Finished Loading data")

leaves = list()
non_leaves = list()
normalTree = list()


#Iterates over all labels
for i in range(23):
    print("\n\n")
    p, l, nl = IndividualTree(traindf, testdf, i)
    leaves.append(l)
    non_leaves.append(nl)
    normalTree.append(p)



print("normal")
print(normalTree)

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


#normal
#[0.99475925319358, 0.9868981329839502, 0.998689813298395, 0.990501146413364, 0.9868981329839502, 0.9921388797903701, 0.9901735997379627, 0.9816573861775303, 0.9898460530625615, 0.9963969865705863, 0.9957418932197838, 0.9862430396331477, 0.9977071732721913, 0.9950867998689813, 0.990501146413364, 0.9895185063871602, 0.998689813298395, 0.9895185063871602, 0.9977071732721913, 0.9882083196855552, 0.998689813298395, 0.9996724533245988, 0.9823124795283328]
#leaves: [27, 64, 13, 66, 91, 38, 39, 80, 46, 16, 13, 78, 19, 47, 37, 54, 9, 53, 15, 52, 15, 7, 69]


#non-leaves [26, 63, 12, 65, 90, 37, 38, 79, 45, 15, 12, 77, 18, 46, 36, 53, 8, 52, 14, 51, 14, 6, 68]
#Number of leaves: 948
#Average per pair: 41.21739130434783


#Number of non-leaves: 925
#Average per pair: 40.21739130434783
