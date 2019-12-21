#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Kcr1Mso
# datetime:2019-12-15 20:41
# software:PyCharm

import pickle
import gib_detect_train
import pandas as pd

def test():
    csv = pd.read_csv('Data.csv')
    domain = csv['domain'].values
    res = []
    model_data = pickle.load(open('gib_model.pki', 'rb'))
    for i in range(len(domain)):
        model_mat = model_data['mat']
        dom = domain[i].split('.')[0]
        print(domain[i])
        print(gib_detect_train.avg_transition_prob(dom, model_mat))

def HMM(domain):
    model_data = pickle.load(open('gib_model.pki', 'rb'))
    model_mat = model_data['mat']
    str = domain.split('.')[0]
    hmm = gib_detect_train.avg_transition_prob(str, model_mat)
    return hmm

if __name__ == '__main__':
    HMM()