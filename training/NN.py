# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:25:16 2017

@author: DKjack
"""
##refrence :https://www.kaggle.com/badredapple/performance-comparison-of-ml-algorithms-a24044/editnb
#In this test ,use NN and K_NN
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import metrics

#if you want to load test set
test_set=input("load this csv:")
test = pd.read_csv(test_set)

## Load Data :
data_set = pd.read_csv("处理好的数据")
y_train = pd.read_csv("一个一个对应的结果")


#null value check 
print(data_set.isnull().any().any())
print(y_train.isnull().any().any())

#split train and test
#x_train, x_test, y_train, y_test = train_test_split(data_set, y_train, test_size=0.20, random_state=33)

#This is a problem : How we tranform a continuous variable into discrete variable

from sklearn.utils import shuffle

test     = utils.shuffle(test) 
data_set = utils.shuffle(data_set)



# Separating data inputs and output labels
trainData = data_set.dorp('label', axis = 1).values
trainLabelE= data_set.label.values

testData = test.dorp('label', axis = 1).values
testLabelE = test.label.values


##encoding labels
from sklean import preprocessing

encoder = preprocessing.LabelEncoder()

#encoding test labels
encoder.fit(testLabelE)
testLabelE = encoder.transform(testLabelE)

#encoding train labels
encoder.fit(trainLabelE)
trainLabelE = encoder.transform(trainLabelE)

##applying supervised neural network using multi-layper preception

import sklearn.neural_network as nn

mlpSGD = nn.MLPClassifier(hidden_layer_sizes = (90,)\
                         ,max_iter = 1000, alpha = 1e-4\
                         ,solver = 'sgd', verbose = 10\
                         ,tol = 1e-19, random_state = 1\
                         ,learning_rate_init = .001)
mlpADAM = nn.MLPClassifier(hidden_layer_sizes = (90,)\
                           ,max_iter = 1000, alpha = 1e-4\
                           ,solver = 'adam', verbose = 10\
                           ,tol = 1e-19, random_state = 1\
                           ,learning_rate_init = .001)

nnModelSGD  = mlpSGD.fit(trainData,  trainLabelE)
nnModelADAM = mlpADAM.fit(trainData, trainLabelE)

#show two models
import matplotlib.pyplot as plt


X1 = np.linspace(1,nnModelSGD.n_iter_ , nnModelSGD.n_iter_)
X2 = np.linspace(1,nnModelADAM.n_iter_ , nnModelADAM.n_iter_)

plt.plot(X1 , nnModelSGD.loss_curve_ , label = 'SGD Convergence')
plt.plot(X2 , nnModelADAM.loss_curve_, label = 'ADAM Convergence')
plt.title('Error Convergence')

plt.ylabel('Cost function')
plt.xlabel('Iterations')

plt.show()

#generating test scores for both classifiers

print("Training set score for SDG :%f" %mlpSGD.score(trainData, trainLabelE))
print("Training set score for ADAM :%f" %mlpADAM.score(trainData, trainLabelE))
print("Test set score for SDG :%f" %mlpSGD.score(testData, testLabelE))
print("Test set score for SDG :%f" %mlpADAM.score(testData, testLabelE))

## applying supervised k -Nearest Neighbor
from sklearn.neighbors import KNeighborsClassifirt as knn

knnclf = knn(n_negihbors = 20, n_jobs = 2, weights = 'distance')
knnModel = knnclf.fit(trainData, trainLabelE)

print("Training set score for ADAM :%f" %knnModel.score(trainData, trainLabelE))
print("Test set score for SDG :%f" %knnModel.score(testData, testLabelE))


