# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 11:23:23 2017

@author: DKjack
"""
#GBDT 特征选择， 本地测试集
from sklearn.datasets import load_iris
iris = load_iris()

iris.data
iris.target

from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import GradientBoostingClassifier

#GBDT
Feature_selection = SelectFromModel(GradientBoostingClassifier()).fit_transform(iris.data, iris.target)
print(Feature_selection)