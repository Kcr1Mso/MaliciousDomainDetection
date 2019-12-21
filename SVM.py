#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Kcr1Mso
# datetime:2019-10-12 21:24
# software:PyCharm

import time
import pandas as pd
from sklearn import svm
from sklearn import datasets
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.externals import joblib
import matplotlib.pyplot as plt


if __name__ == '__main__':

    print('prepare datasets...')

    # rawdata = pd.read_csv('TrainSet_3_feature.csv', header=0)
    rawdata = pd.read_csv('TrainSet.csv', header=0)
    data = rawdata.values

    print(data)

    # features = data[::, 3::]
    features = data[::, 4::]
    print('features...')
    print(features)
    labels = data[::, 2]
    # labels = data[::, 2]
    #encoded_labels = data[::, 3].map(lambda x: 1 if x == 'Normal' else 0).values
    print('labels...')
    print(labels)
    print('encoded labels...')
    #print(encoded_labels)

    parameters = [

        {

            'C': [0.5, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 30,
                  50],

            'gamma': [0.1, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.2, 1.3, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 8, 9, 10, 11],

            'kernel': ['rbf']

        },

        {

            'C': [0.5, 0.8, 0.9, 1, 2, 3, 4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 5, 5.5, 6, 7, 9, 11, 13, 15, 17, 19, 30, 50],

            'kernel': ['linear']

        }

    ]


    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)

    time_2=time.time()
    print('Start training...')
    svc = svm.SVC()
    clf = svm.SVC(kernel='rbf', C= 50, gamma='auto')  # svm class
    # clf = GridSearchCV(svm.SVC(), parameters, cv=5, n_jobs=8)
    clf.fit(train_features, train_labels)  # training the svc model
    time_3 = time.time()
    # print(clf.best_params_)
    print('training cost %f seconds' % (time_3 - time_2))

    #joblib.dump(clf, 'domain.m')

#     print(clf.predict([[0.8143511100567237,-0.3125016658660619,-0.31611912576291107,0.20710776634396336,1.431194711531615,0.20465056816811145,0.15883682012601766
# ]]))
#     print(clf.get_params(deep=True))

    print('Start predicting...')
    test_predict=clf.predict(test_features)
    time_4 = time.time()
    print('predicting cost %f seconds' % (time_4 - time_3))

    # print(test_predict)
    # print(test_labels)

    accuracy_score = accuracy_score(test_labels, test_predict)
    precision_score = precision_score(test_labels, test_predict, pos_label='Normal')
    recall_score = recall_score(test_labels, test_predict, pos_label='Normal')
    f1_score = f1_score(test_labels, test_predict, pos_label='Normal')

    print('accuracy_score：', accuracy_score)
    print('precision_score：', precision_score)
    print('recall_score：', recall_score)
    print('f1_score：', f1_score)
    # print(clf.best_params_)
    # print(clf.coef_)
    # print(clf.intercept_)

    # fpr, tpr, thresholds = roc_curve(test_labels, test_predict, pos_label='Normal')
    #
    # plt.plot(fpr, tpr)
    # plt.show()

