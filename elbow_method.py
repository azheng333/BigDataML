# encoding=utf-8
import numpy as np
from sklearn.cluster import KMeans


# 面积km2,人口
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

#类簇的数量
n_clusters = 1

cls = KMeans(n_clusters).fit(X)

#每个簇的中心点
cls.cluster_centers_

#X中每个点所属的簇
cls.labels_

#曼哈顿距离
def manhattan_distance(x, y):
    return np.sum(abs(x - y))


distance_sum = 0
for i in range(n_clusters):
    group = cls.labels_ == i
    members = X[group, :]
    for v in members:
        distance_sum += manhattan_distance(np.array(v), cls.cluster_centers_)
print distance_sum
#结果63538.2443905
