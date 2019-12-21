#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Kcr1Mso
# datetime:2019-11-18 09:40
# software:PyCharm

import os,Feature

def createdata():

    if not os.path.isfile('Data.csv'):

        data = open('Data.csv', mode='w', encoding='utf-8')

        data.close()


def extract():

    traindata = open('TrainData.csv', mode='r', encoding='utf-8')

    # data = open('TrainSet_3_feature.csv', mode='w', encoding='utf-8')

    data = open('TrainSet.csv', mode='w', encoding='utf-8')

    # data.writelines('doamin,result,len,mvdlen,entr,hmm\n')

    data.writelines('doamin,result,suff, len, numratio,consnumber, conschar, consamenum, mvdlen, entr, hmm\n')

    while True:

        if traindata.readline() == '':
            break

        line = traindata.readline().strip('\n')
        domain = line.split(',')[0]

        suff, len, numratio,consnumber, conschar, consamenum, mvdlen, entr, hmm = Feature.extract(domain)

        # dataline = line + ',' + str(len) + ',' + str(mvdlen) + ',' + str(entr) + ',' + str(hmm) + '\n'
        dataline = line + ',' + str(suff) + ',' + str(len) + ',' \
                   + str(numratio) + ',' \
                   + str(consnumber) + ',' \
                   + str(conschar) + ',' \
                   + str(consamenum) + ',' \
                   + str(mvdlen) + ',' + str(entr) + ',' + str(hmm) + '\n'

        data.writelines(dataline)

    data.close()

    traindata.close()

if __name__ == '__main__':

    extract()