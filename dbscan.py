# coding=utf-8
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt


#国家面积和人口
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

#转换成numpy array
X = np.array(X)

#归一化
a = X[:, :1] / 17075400.0 * 10000
b = X[:, 1:] / 1392358258.0 * 10000
X = np.concatenate((a, b), axis=1)

#现在我们把训练数据，和对应的分类放入分类器中进行训练，在这没有噪点出现因为我们把min_samples设置成了1
cls = DBSCAN(2000, min_samples=1).fit(X)

#类簇的数量
n_clusters = len(set(cls.labels_))

#X中每项所属分类的一个列表
cls.labels_

#画图
markers = ['^', 'x', 'o', '*', '+']
for i in range(n_clusters):
    my_members = cls.labels_ == i
    plt.scatter(X[my_members, 0], X[my_members, 1], s=60, marker=markers[i], c='b', alpha=0.5)

plt.title('dbscan')
plt.show()
plt.savefig('dbscan.png')