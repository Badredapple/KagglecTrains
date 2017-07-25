# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 09:57:16 2017

@author: DKjack
"""

import pandas as pd
import os
import json
os.chdir("/home/hadoop/jupyter/sdl/ZhangYidan")
filename1 = os.listdir("/home/hadoop/jupyter/sdl/ZhangYidan")
data_col=[]
colname=['timestamp','accelerate_x','accelerate_y','accelerate_z','gyroscope_x','gyroscope_y','gyroscope_x', 'gravity_x',
                     'gravity_y','gravity_z','magnetic_x','magnetic_y','magnetic_z','linear_accelerate_x','linear_accelerate_y','linear_accelerate_z',
                     'world_orientation_x','world_orientation_y','world_orientation_z','world_accelerometer_x','world_accelerometer_y','world_accelerometer_z',
                     'rotation_vector_x','rotation_vector_y','rotation_vector_z','game_rotation_vector_x','game_rotation_vector_y','game_rotation_vector_z','light','pressure','temperature']

select_colname=['world_accelerometer_x','world_accelerometer_y','world_accelerometer_z','label']

# -*- coding:utf-8 -*-
    # （1）时域：均值，方差，标准差，最大值，最小值，过零点个数，最大值与最小值之差，众数
    # （2）频域：直流分量，图形的均值、方差、标准差、斜度、峭度，幅度的均值、方差、标准差、斜度、峭度
    # 共19个特征
import numpy as np
from tsfeature.feature_time import Feature_time
from tsfeature.feature_fft import Feature_fft

def get_feature(arr):
        '''
        Get features of an array
        :param arr: input 1D array
        :return: feature list
        '''
        feature_list = list()
        # get time domain features
        feature_time = Feature_time(arr).time_all()
        feature_list.extend(feature_time)
        # get frequency domain features
        feature_fft = Feature_fft(arr).fft_all()
        feature_list.extend(feature_fft)
        return feature_list


def sequence_feature(seq, win_size, step_size):
        '''
        Get features of a sequence, with or without window
        :param seq: shape of the sequence: (n,1)
        :param win_size: window size, if window_size == 0, get features without window
        :param step_size: step size
        :return: 2D feature matrix
        '''
        if win_size == 0:
            return np.asarray(get_feature(seq))
        window_size = win_size
 
    
    del data_df['f_shape_kurt']
        data_df = data_df.dropna()