# coding=utf-8
import numpy as np
from math import log

#枚举型
#学历分类里 大专， 本科， 硕士  占比
education = (2.0 / 12, 5.0 / 12, 5.0 / 12)

#大专分类里相亲占比
junior_college = (1.0 / 2, 1.0 / 2)

#本科分类里相亲占比
undergraduate = (3.0 / 5, 2.0 / 5)

#硕士分类里相亲占比
master = (4.0 / 5, 1.0 / 5)

#学历各分类里相亲占比
date_per = (junior_college, undergraduate, master)


#相亲字段划分规则下的熵
def info_date(p):
    info = 0
    for v in p:
        info += v * log(v, 2)
    return info


#使用学历字段划分规则下的熵
def infoA():
    info = 0
    for i in range(len(education)):
        info += -education[i] * info_date(date_per[i])
    return info


print infoA()
#结果0.872032787226


#连续型
#年龄
age = [25, 25, 28, 28, 29, 30, 33, 34, 35, 36, 40, 46]

#是否相亲 1:是   0:否
date = [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0]

length_total = 12

#这里我们从年龄28，29中间切开
#左,右分类里的数量占总数的百分比
split_per = (4.0 / 12, 8.0 / 12)

#左边分类里相亲占比
date_left = (1.0 / 2, 1.0 / 2)

#右边分类里相亲占比
date_right = (5.0 / 8, 3.0 / 8)

#左右各分类里相亲占比
date_per = (date_left, date_right)

#相亲字段划分规则下的熵
def info_date(p):
    info = 0
    for v in p:
        info += v * log(v, 2)
    return info


#使用学历字段划分规则下的熵
def infoA():
    info = 0
    for i in range(len(split_per)):
        info += -split_per[i] * info_date(date_per[i])
    return info


print infoA()

