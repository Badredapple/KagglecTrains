# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 22:32:01 2017

@author: DKjack
"""
##feature engineering Test under iris dataset and sklearn libs
#all of this code is from http://www.cnblogs.com/jasonfreak/p/5448385.html

#load iris dataset
from sklearn.datasets import load_iris

iris = load_iris()
#Load iris dataset
iris.data
#feature Martix

iris.target
#aims Vector

##2.1 无量纲化
#2.1.1 标准化
from sklearn.preprocessing import StandardScaler
iris_StandardScaler = StandardScaler().fit_transform(iris.data) 
print(iris_StandardScaler)

#2.1.2最值区间缩放法
from sklearn.preprocessing import MinMaxScaler
#区间缩放为[0,1]
iris_MinMaxScaler = MinMaxScaler().fit_transform(iris.data)
print(iris_MinMaxScaler)

#2.1.3归一化
from sklearn.preprocessing import Normalizer
#归一化
iris_Normalizer = Normalizer().fit_transform(iris.data)
print(iris_Normalizer)

#2.2对定量特征二值化
from sklearn.preprocessing import Binarizer
iris_Binarizer = Binarizer(threshold = 3).fit_transform(iris.data)
print(iris_Binarizer)

#2.3 对定性特征哑编码
from sklearn.preprocessing import OneHotEncoder

iris_OneHotEncoder = OneHotEncoder().fit_transform(iris.target.reshape(-1,1))

print(iris_OneHotEncoder)
#2.4计算缺失值
from numpy import vstack, array, nan
from sklearn.preprocessing import Imputer
#计算缺失值，
Imputer().fit_transform(vstack((array([nan, nan, nan, nan]), iris.data)))

#2.5数据变化 
from sklearn.preprocessing import PolynomialFeatures
#多项式转化
PolynomialFeatures().fit_transform(iris.data)

#对于单变元函数的数据变换
from numpy import log1p
from sklearn.preprocessing import FunctionTransformer

#自定义转换函数为对数函数的数据变换
FunctionTransformer(log1p).fit_transform(iris.data)

##3.特征选择
#3.1 Filter
#3.1.1 方差计算法
from sklearn.feature_selection import VarianceThreshold
#方差选择法
VarianceThreshold(threshold = 3).fit_transform(iris.data)

#3.1.2 相关系数
from sklearn.feature_selection import SelectKBest
from scipy.stats import pearsonr

#选择最好的K个特征值，返回选好的数据
iris_SelectKBest = SelectKBest(lambda X,Y: array(map(lambda x:pearsonr(x, Y), X.T)))
print(iris_SelectKBest)

#卡方检验
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
#选择最好的K个特征，返回选择以后的数据
SelectKBest(chi2, k=2).fit_transform(iris.data, iris.target)


#3.1.4 互信息法
#from sklearn.feature_selection import SelectKBest
#from minepy import MINE
#返回一个二元组。定义mic方法为函数式的，释放一个二元组，将二元组的第二项固定个P= 0.5
#minepy packet: https://pypi.python.org/pypi/minepy
#def mic(x,y):
 #   m = MINE()
 #  m.compute_score(x,y)
 #  return (m.mic(), 0.5)
#选择K个最好的特征，并返回选择后的数据
#SelectKBest(lambda X, Y: array(map(lambda x:mic(x, Y), X.T)).T, k=2..fit_transform(iris.data,iris.target))

#3.2 Wrapper
#3.2.1 递归特征消除法
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression 
#递归特征消除，返回特征选择以后的数据
#参数estimator为基模型
#参数n_features_to_select 为选择的特征个数
RFE(estimator = LogisticRegression(), n_features_to_select = 2).fit_transform(iris.data, iris.target)

#3.3 Embedded
#3.3.1 基于惩罚项的特征选择法
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
#带L1惩罚项的逻辑回归为基模型的特征选择
SelectFromModel(LogisticRegression(penalty = "11",C= 0.1).fit_transform(iris.data,iris.target))

#3.3.2基于树模型的特征选择法
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import GradientBoostingClassifier
#GBDT 为基模型的特征选择
SelectFromModel(GradientBoostingClassifier()).fit_transform(iris.data, iris.target)

##4.降维度
#4.1主成分分析法：PCA
from sklearn.decomposition import PCA
#主成分分析法，返回降维以后的数据
#参数n_components 为主成分数目
print(PCA(n_comopents=2).fit_transform(iris.data))

#4.2线性判别分析法：LDA 
from sklearn.lda import LDA
#线性判别分析法，返回降维以后的数据
LDA(n_components=2).fit_transform(iris.data, iris.target)