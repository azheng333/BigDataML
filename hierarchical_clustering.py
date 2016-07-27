# coding=utf-8
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering


X = []
f = open('data.txt')
for v in f:
    X.append([float(v.split(',')[2]), float(v.split(',')[3])])

#转换成numpy array
X = np.array(X)

#类簇的数量
n_clusters = 5

#现在我们把训练数据和对应的分类数放入聚类函数中进行聚类，使用方差最小化的方法'ward'
cls = AgglomerativeClustering(linkage='ward', n_clusters=n_clusters).fit(X)

#X中每项所属分类的一个列表
cls.labels_

#画图
markers = ['^', 'x', 'o', '*', '+']
plt.subplots()
for i in range(n_clusters):
    my_members = cls.labels_ == i
    plt.scatter(X[my_members, 0], X[my_members, 1], s=60, marker=markers[i], c='b', alpha=0.5)

plt.title("hierarchical_clustering")
plt.show()
plt.savefig('hierarchical_clustering.png')
