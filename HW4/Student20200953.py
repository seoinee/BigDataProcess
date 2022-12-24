from os import listdir
import sys
import numpy as np
import operator

def createDataSet(dir):
    labels = []
    training = listdir(dir)
    n = len(training)
    group = np.zeros((n, 1024))

    for i in range(n):
        realResult = training[i]
        answer = int(realResult.split('_')[0])
        labels.append(answer)
        group[i, :] = vector(dir + '/' + realResult)
    return group, labels 

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]] 
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key= operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def vector(file): 
    vector = np.zeros((1, 1024))
    with open(file) as fp:
        for i in range(32):
            s = fp.readline()
            for j in range(32):
                vector[0, i * 32 + j] = int(s[j])
        return vector        

trainingFile = sys.argv[1]
testFile = sys.argv[2]

testFileList = listdir(testFile)
length = len(testFileList)

group, labels = createDataSet(trainingFile)

for k in range(1, 20):
    count = 0
    errorCount = 0
    
    for i in range(length):
        answer = int(testFileList[i].split('_')[0])
        list = vector(testFile + '/' + testFileList[i])
        knn_result = classify0(list, group, labels, k)
        
        count += 1
        if answer != knn_result :
            errorCount += 1
    
    print(int(errorCount / count * 100))
