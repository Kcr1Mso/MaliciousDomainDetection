#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Kcr1Mso
# datetime:2019-11-05 15:47
# software:PyCharm

import function,re,math
import HMM


# def alexa(domain):
#     #alexa排名
#     file = open('WhiteList.csv', mode='r', encoding='utf-8')
#     while True:
#         if file.readline() == '':
#             break
#         line = file.readline().strip()
#         str = line.split(',')[1]
#         # print(str[1])
#         if domain == str:
#             return line[0]
#             break
#     return 9999999
#
# def seo(domain):
#     #seo收录数
#     pass

def suffix(domain):
    #是否主流域名后缀

    list = domain.split('.')
    suff = list[len(list) - 1]
    Mainstream = ['com', 'cn', 'org', 'edu', 'net']
    if suff in Mainstream:
        return 1
    else:
        return 0

def number(domain):
    # 域名中的数字字符数
    count = 0
    str = domain.split('.')[0]
    for i in str:
        if function.isnumber(i):
            count += 1
    return count

def numberratio(domain):
    #域名中的数字字符比率
    str = domain.split('.')[0]
    numofnum = number(domain)
    numofdomain = len(str)
    ratio = numofnum / numofdomain
    return ratio

def consecutivenumber(domain):
    #连续数字字符的最大长度
    str = domain.split('.')[0]
    list1 = []
    list2 = []
    pattern = '[1-9]'

    r = re.compile(pattern)
    for i in str:
        if r.match(i):
            list1.append(i)
        else:
            if len(list1) > len(list2):
                list2 = [i for i in list1]
            list1 = []
    if len(list1) > len(list2):
        return len(list1)
    else:
        return len(list2)

def consecutivechar(domain):
    #连续字母字符的最大长度
    str = domain.split('.')[0]
    list1 = []
    list2 = []
    pattern = '[a-z,A-Z]'

    r = re.compile(pattern)
    for i in str:
        if r.match(i):
            list1.append(i)
        else:
            if len(list1) > len(list2):
                list2 = [i for i in list1]
            list1 = []
    if len(list1) > len(list2):
        return len(list1)
    else:
        return len(list2)

def consecutivesamechar(domain):

    #连续相同字母字符的最大长度
    curmaxlen = 1
    maxlen = 1

    str = domain.split('.')[0]

    list = []

    for i in str:

        if len(list) == 0:

            list.append(i)

        elif i == list[0]:

            list.append(i)

        else:

            #print(list)

            curmaxlen = len(list)

            list = []

            list.append(i)

        if curmaxlen > maxlen:

            maxlen = curmaxlen

    return maxlen

def mvd(domain):

    #最长元音距
    vowel = ['a', 'e', 'i', 'o', 'u', '-']
    index = []
    length = 0
    maxlen = 0

    str = domain.split('.')[0]

    for i in range(len(str)):

        if str[i] in vowel:

            index.append(i)

    index.append(len(str))

    #print(index)

    for i in  range(len(index) - 1):

        length = index[i + 1] - index[i] - 1

        if length > maxlen:

            maxlen = length

    return maxlen

def entropy(domain):

    #信息熵，表示字符串的随机程度
    #𝐇(𝐱) = −𝒔𝒖𝒎(𝒑(𝒙)𝒍𝒐𝒈𝟐𝒑(𝒙))

    str = domain.split('.')[0]

    h = 0.0
    sumletter = 0
    sumnum = 0
    letter = [0] * 26
    num = [0] * 10
    str = str.lower()

    for i in range(len(str)):
        if str[i].isalpha():
            letter[ord(str[i]) - ord('a')] += 1
            sumletter += 1
        if str[i].isnumeric():
            num[int(str[i])] += 1
            sumnum += 1
    # print('\n', letter)
    # print('\n', num)
    sum = sumletter + sumnum
    for i in range(26):
        p = 1.0 * letter[i] / sum
        if p > 0:
            h += -(p * math.log(p, 2))
    for i in range(10):
        p = 1.0 * num[i] / sum
        if p > 0:
            h += -(p * math.log(p, 2))
    return h


def extract(domain):
    # alex = alexa(domain) #alexa排名
    # seonum = seo(domain) #seo收录数
    suff = suffix(domain)    #是否主流域名后缀
    #num = number(domain) #域名中的数字数量
    length = len(domain)
    numratio = numberratio(domain)   #域名中的数字比率
    consnumber = consecutivenumber(domain)   #域名中连续数字的最大长度
    conschar = consecutivechar(domain)       #域名中连续字符的最大长度
    consamenum = consecutivesamechar(domain)     #连续相同字母字符的最大长度
    mvdlen = mvd(domain)
    entr = entropy(domain)
    hmm = HMM.HMM(domain)

    return suff, length, numratio, consnumber, conschar, consamenum, mvdlen,entr,hmm
