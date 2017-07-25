# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:54:21 2017

@author: DKjack
"""
#reference :https://www.kaggle.com/anfro18/recognizing-human-activity-96-accuracy
#Use SVM 

import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import metrics
#from xgboost.sklearn import XGBClassifier

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
x_train, x_test, y_train, y_test = train_test_split(data_set, y_train, test_size=0.20, random_state=33)


#In reference .he tranform str into number but ibn our ,it's needless
#this is for test set pretreatment

y_test = test["New_Activity"]
X_test = test.drop(["New_Activity","Activity"],1)

from sklearn.svm import LinearSVC,SVC
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDClassifier


clf = LinearSVC()
clf.fit(x_train,y_train)

pred = clf.predict(X_test)
print(pred) #output the classifier result ,this is a  array
#score = accuracy_score(y_test, pred)

#print(score)





