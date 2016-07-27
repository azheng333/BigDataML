#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt


def fun():
    # 原始数据
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [0.199, 0.389, 0.580, 0.783, 0.980, 1.177, 1.380, 1.575, 1.771]

    A = np.vstack([x, np.ones(len(x))]).T
    #A:
    #[[ 1.  1.]
    # [ 2.  1.]
    # [ 3.  1.]
    # [ 4.  1.]
    # [ 5.  1.]
    # [ 6.  1.]
    # [ 7.  1.]
    # [ 8.  1.]
    # [ 9.  1.]]

    #调用最小二乘法函数
    a, b = np.linalg.lstsq(A, y)[0]

    #转换成numpy arrary
    x = np.array(x)
    y = np.array(y)

    #画图
    plt.plot(x, y, 'o', label='Original data', markersize=10)
    plt.plot(x, a * x + b, 'r', label='Fitted line')
    plt.show()
    plt.savefig('test.png')

if __name__ == '__main__':
    fun()
