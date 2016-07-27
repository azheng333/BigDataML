# coding=utf-8
import numpy as np
from sklearn.cluster import KMeans


X = [
    [9670250, 1392358258],
    [2980000, 1247923065],
    [9629091, 317408015],
    [8514877, 201032714],
    [377873, 127270000],
    [7692024, 23540517],
    [9984670, 34591000],
    [17075400, 143551289],
    [513115, 67041000],
    [181035, 14805358],
    [99600, 50400000],
    [120538, 24052231]]

# 转换成numpy array
X = np.array(X)

#归一化
a = X[:, :1] / 17075400.0 * 10000
b = X[:, 1:] / 1392358258.0 * 10000
X = np.concatenate((a, b), axis=1)

pn = X[np.random.choice(X.shape[0], 3, replace=False), :]
#随机选出来的三个
# [[   221.29671926    914.06072589]
#  [    70.59161132    172.74455667]
#  [ 10000.           1030.99391392]]
xn = []
for i in pn:
    distance_min = 1000000
    for j in X:
        if np.array_equal(j, i):
            continue
        distance = np.linalg.norm(j - i)
        if distance_min > distance:
            distance_min = distance
    xn.append(distance_min)

qn = X[np.random.choice(X.shape[0], 3, replace=False), :]
#随机选出来的三个
# [[ 10000.           1030.99391392]
#  [  4986.63398808   1443.82893444]
#  [   221.29671926    914.06072589]]
yn = []
for i in qn:
    distance_min = 1000000
    for j in X:
        if np.array_equal(j, i):
            continue
        distance = np.linalg.norm(j - i)
        if distance_min > distance:
            distance_min = distance
    yn.append(distance_min)

H = float(np.sum(yn)) / (np.sum(xn) + np.sum(yn))
print H
#结果为 0.547 059 223 781
