# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:19:46 2017

@author: DKjack
"""
##reference :https://www.kaggle.com/badredapple/model-based-feature-selection-newbie-f93189/editnb
#this is Different ML Methods in Python

#load Data
import numpy as np
import pandas as pd



from sklearn.cross_validation import train_test_split

#if you want to load test set
test_set=input("load this csv:")
test = pd.read_csv(test_set)

## Load Data :
data_set = pd.read_csv("处理好的数据")
y_train =data_set['label']


#null value check 
print(data_set.isnull().any().any())
print(y_train.isnull().any().any())

#split train and test
x_train, x_test, y_train, y_test = train_test_split(data_set, y_train, test_size=0.20, random_state=33)

print(x_train.shape)

##Featrure Selection
#Tree-based fearture selection 

from sklearn.ensemble import ExtraClassifier
from sklearn.feature_selection import SelectFromModel
features = x_train.iloc[:,0:114]
label = x_train['label']
clf = ExtraClassifier()
clf = clf.fit(features, label)
model = SelectFromModel(clf, prefit = True)
New_features = model.transform(features)
print(New_features.shape)


#L1-based feature selection
from sklearn.svm import LinearSVC
lsvc = LinearSVC(C = 0.01, penalty = "11", dual = False).fit(features,label)
model_2 =  SelectFromModel(lsvc, prefit = True)
New_features_2 = model_2.transform(features)
print(New_features_2.shape)


##Fitting Classifiers
#loadModels

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GrandientBoostingClassifier
Classifiers = [DecisionTreeClassifier(), RandomForestClassifier(n_estimators = 200),GrandientBoostingClassifier(n_estimators = 200)]

#if you not do feature selection
from sklearn.metrics import accuracy_score
import timeit
test_features = test.iloc[:,0:114]
Time_1 = []
Model_1 = []
Out_Accuracy_1 = []
for clf in Classifiers:
    start_time = timeit.default_timer()
    fit = clf.fit(features,label)
    pred = fit.predict(test_features)
    elapsed = timeit.default_timer() - start_time
    Time_1.append(elapsed)
    Model_1.append(clf.__class__.__name__)
    Out_Accuracy_1.append(accuracy_score(test['label'],pred))
    print(Out_Accuracy_1)
  
#Tree based feature selection
test_features = model.transform(test.iloc[:,0:562])
Time_2 = []
Model_2 = []
Out_Accuracy_2 = []
for clf in Classifiers:
    start_time = timeit.default_timer()
    fit = clf.fit(New_features,label)
    pred = fit.predict(test_features)
    elapsed = timeit.defaulr_timer() - start_time
    print(elapsed)
    Time_2.append(elapsed)
    Model_2.append(clf.__class__.__name__)
    Out_Accuracy_2.append(accuracy_score(test['label'],pred),pred)
    print(Out_Accuracy_2)
    
#L1-Based feature selection
test_features = model_2.transform(test.iloc[:,0:114])
Time_3 =[]
Model_3 = []
Out_Accuracy_3 = []
for clf in Classifiers:
    start_time = timeit.default_timer()
    fit = clf.fit(New_features,label)
    pred = fit.predict(test_features)
    elapsed = timeit.defaulr_timer() - start_time
    print(elapsed)
    Time_3.append(elapsed)
    Model_3.append(clf.__class__.__name__)
    Out_Accuracy_3.append(accuracy_score(test['label'],pred),pred)
    print(Out_Accuracy_3)
    
