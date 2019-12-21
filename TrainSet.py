#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Kcr1Mso
# datetime:2019-11-19 14:13
# software:PyCharm

import pandas as pd

def trainset():

    # data = pd.read_csv('Data_3_feature.csv')
    data = pd.read_csv('Data.csv')

    data = data.sample(frac=1.0)
    cut_idx = int(round(0.1 * data.shape[0]))

    data_test, data_train = data.iloc[:cut_idx], data.iloc[cut_idx:]

    print(data.shape, data_test.shape, data_train.shape)

    # data_test.to_csv('TestSet.csv')
    # data_train.to_csv('TrainSet.csv')

    print(data_train.describe())

    print(data_train.groupby(['result']).size()['Normal'])
    print(data_train.groupby(['result']).size()['Malicious'])
    print(data_test.groupby(['result']).size()['Normal'])
    print(data_test.groupby(['result']).size()['Malicious'])

def Normalize(dataframe):

    dataframe2 = (dataframe - dataframe.mean())/dataframe.std()

    return dataframe2

if __name__ == '__main__':

    #trainset()

    # traindata = pd.read_csv('TrainSet_3_feature.csv')
    traindata = pd.read_csv('TrainSet.csv')

    # columns = ['len','mvdlen','entr', 'hmm']
    columns = ['suff', 'len', 'numratio', 'consnumber', 'conschar', 'consamenum','len','mvdlen','entr', 'hmm']

    for i in columns:

        traindata[i] = Normalize(traindata[i])

    # traindata.to_csv('TrainSet_3_feature.csv')
    traindata.to_csv('TrainSet.csv')

