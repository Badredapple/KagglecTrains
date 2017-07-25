# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:42:45 2017

@author: DKjack
"""

import pandas as pd
from sklearn import metrics
from xgboost.sklearn import XGBClassifier
import xgboost as xgb
import numpy as np
from sklearn.cross_validation import train_test_split

x_train = pd.read_csv("特征矩阵")
y_train = pd.read_csv("label")

#预测数据还需要从json修改为
x_train_test = pd.read_csv("预测的数据")

x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.20, random_state=33)


#生成DMatrix 输入 和验证集合产生
d_train = xgb.DMatrix(x_train, label=y_train)
d_valid = xgb.DMatrix(x_test, label=y_test)
d_test = xgb.DMatrix(x_train_test)
watchlist = [(d_train, 'train'), (d_valid, 'valid')]

#XGBoost interface
'''
params={
    'eta': 0.1,
    'max_depth':6,   
    'min_child_weight':1,
    'gamma':0.3, 
    'subsample':0.8,
    'colsample_bytree':0.8,
    'booster':'gbtree',
    'objective': 'binary:logistic',
    'nthread':6,
    'scale_pos_weight': 1,
    'lambda':1,  
    'seed':27,
    'silent':0 ,
    'eval_metric': 'auc'
}
'''
#sklearn interface
'''
clf = XGBClassifier(
    n_estimators=400,#400棵树
    learning_rate =0.1,
    max_depth=6,
    min_child_weight=1,
    gamma=0.3,
    subsample=0.8,
    colsample_bytree=0.8,
    objective= 'binary:logistic',
    nthread=8,
    scale_pos_weight=1,
    reg_lambda=1,
    seed=27)

'''
#model_bst = xgb.train(params, d_train, 400, watchlist, early_stopping_rounds=500, verbose_eval=10)
clf = XGBClassifier()
model_sklearn=clf.fit(x_train, y_train)
#使用默认的参数，寻找参数变化范围
#y_bst= model_bst.predict(d_test)

#print(y_bst)
#prob = pd.DataFrame(y_bst, columns = ['probability'])
#X_train_test['male'] = prob['probability']

#output = X_train_test[['tdid','male']]

#output.columns = ['id','probability']
#print(output.head())
y_sklearn= clf.predict_proba(d_test)[:,1]

print("XGBoost_sklearn接口 AUC Score : %f" % metrics.roc_auc_score(y_test, y_sklearn))
#使用反思， 先将数据导入，其次使用自带分类器求解最合适的值，然后再使用xgb 原型 提高拟合度