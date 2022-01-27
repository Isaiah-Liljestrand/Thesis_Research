Author: Isaiah Liljestrand

Research Advisor: Dr. Subhasish Mazumdar

Project: Pairwise classification of tissue types based on gene expression levels - Thesis research

Purpose: Collaborative research effort between Los Alamos National Labs and New Mexico Tech to use machine learning to find the most useful genes for classification to assist in stem cell research.

This is most of the research done by me for this project, there are old experiments including correlation-based filtering and parallelization experimentation that did not end up providing anything useful that are not included here.

The primary research done here falls under two categories that went hand in hand. Other research was focused on finding the most useful genes based on multiple metrics.

The first is heuristic-driven pairwise classification:

    -Gene relationships were studies and classification heuristics were created.
    
    -These heuristics were manually followed to create pairwise decision trees.
    
    -The decision trees involved 4 valued logic. Outputs included:label A, label B, Both, Neither.
    
    -Ties were considered a valid output as they correlated with labels have real world overlap such as cervix and uterus or stomach and esophagus.
    
    -The tool 'Pair Seperation Scatterplot Tool.ipynb' was used for pairwise classifier creation.

The second is pairwise aggregation methods, ways to combine all pairwise classifiers to come to a decision on classification:

    -There are four pairwise aggregation methods all of which involve potential to result in tied results
    
    -1: Class voting: Each pairwise classifier contributes a vote towards the winning label and another vote against the losing label. ties contribute a positive vote towards both
    
    -2: Victim elimination: Run class voting but remove label with the worst score. Repeat until either one label remains or the remaining labels are locked in a stalemate
    
    -3: Tourney: Tournament classification that randomly pairs up labels that are classified against each other to move onto the next round until one remains, or tied in a stalemate
    
    -4: Hybrid: Runs class voting and finishes classification by running tourney on top k values



Brief Folder/File Descriptions:

data - Contains original dataset and collaborator's top gene results

exT.csv - Original dataset. Curated TCGA data already put through some pre-processing

Top.genes.csv - Contains most important genes according to Neural Network LIME results



ExplainablePairwiseClassifier - Main project folder

Preprocess.py - applies log2, removes useless genes, removes datapoints from 10 least populated labels

PairFunctions.py - Test function contains the pairwise decision tree for every pair of labels and the function used for small aggregates

Features.py - Extracts useful data such as features used from PairFunctions.py

PairClassifier.py - Classifies the testing set with each pairwise aggregation method, uses class voting, victim elimination, tourney, and hybrid

Pair Seperation Scatterplot Tool.ipynb - jupyter notebook used to create pairwise classifiers and observe pairwise plots of different genes

StatisticsExtractor.py - extra file to test out different criteria. Currently tests how many pairwise classifications results in ties as well as accuracy thresholds



FeatureSelectionExperiments - Experiments with sorting genes based on different criteria to find the most useful genes

Preprocess.py - Applies log2, creates a binned version, and removes 10 least populated labels in preparation.

CalculateInformationGain.py - Calculates the information gain for every gene-label combination in a one-vs-all manner. For example, info gain on bladder vs all other labels for gene GRHL2

CalculatePairwiseInformationGain.py - Calculates the information gain for every gene for every pair of labels. Takes all samples from two labels and runs information gain for a particular gene.

AllTopTest.py - Runs a neural net using the top genes based on each gene value metric. Tests 10 different numbers of genes: 23 through 230 in increments of 23.



LabelGraph - Jupyter notebook that graphs the cardinalities of all used labels



NewExplainable - Exactly the same as ExplainablePairwiseClassifier formatted for and using a modified dataset. This modified dataset removes or relabels almost all confusing datapoints and narrows the number of labels further. Additionally, all gene names have been swapped with randomized integers to anonymize genes during classifier creation.



NormalDecisionTrees - Creates and displays automated decision trees and neural networks to compare results to manually made solution

NeuralNetworkComparison.py - Runs a neural network for comparison

NormalPairClassifier.py - Creates and runs automated pairwise classifiers under every pairwise aggregation configuration

OnevsAll_Tree.py - Creates, prints, and gathers information on automated one-vs-all classifiers

PairClassifier.py - Runs both types of pairwise trees through pairwise aggregation methods to compare overall effectiveness

PairFunctions.py - Holds the manual pairwise classifiers

PairwiseNeuralNetwork.py - Creates and runs neural networks run on each pair of labels

PairwiseTree.py - Directly compares automated and manual pairwise classifiers

PairwiseTreeData.txt - Stores information from some experimentation in this folder



Redundancy - Randomly selects features and uses them to create neural nets of sizes 1 - 600 and graphs results. Tests where accuracy saturates and how many features are needed for a fully accurate classifier.



Top Feature Analysis - Quickly made tool to view graphs and information for top features from LIME results



automatedtrees.txt - every automated decision tree printed out for review and comparison purposes



FeatureGraphs.ipynb - tool to view graphs of particular genes with samples seperated by label from left to right and color coded



Pairwise Accuracies.ipynb - Prints out histogram of accuracies of manually made pairwise classifiers



Translator.ipynb - Translates integers used in NewExplainable back to original gene names
