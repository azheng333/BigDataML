# coding=utf-8
import numpy as np

jin = ['近', '斤', '今', '金', '尽']
jin_per = [0.3, 0.2, 0.1, 0.06, 0.03]

jintian = ['天', '填', '田', '甜', '添']
jintian_per = [
    [0.001, 0.001, 0.001, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.001],
    [0.990, 0.001, 0.001, 0.001, 0.001],
    [0.002, 0.001, 0.850, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.001]]

wo = ['我', '窝', '喔', '握', '卧']
wo_per = [0.400, 0.150, 0.090, 0.050, 0.030]

women = ['们', '门', '闷', '焖', '扪']
women_per = [
    [0.970, 0.001, 0.003, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.001]]

qing = ['请', '晴', '清', '轻', '情']
qing_per = [0.2, 0.12, 0.09, 0.05, 0.02]

qinghua = ['话', '画', '化', '花', '华']
qinghua_per = [
    [0.001, 0.001, 0.001, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.950],
    [0.001, 0.001, 0.850, 0.001, 0.001],
    [0.003, 0.001, 0.001, 0.002, 0.001]]

da = ['大', '打', '达', '搭', '哒']
da_per = [0.300, 0.130, 0.120, 0.110, 0.090]

daxue = ['学', '雪', '血', '薛', '穴']
daxue_per = [
    [0.800, 0.140, 0.023, 0.004, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.001]]

N = 5


def found_from_oneword(oneword_per):
    index = []
    values = []
    a = np.array(oneword_per)
    for v in np.argsort(a)[::-1][:N]:
        index.append(v)
        values.append(oneword_per[v])
    return index, values


def found_from_twoword(oneword_per, twoword_per):
    last = 0
    for i in range(len(oneword_per)):
        current = np.multiply(oneword_per[i], twoword_per[i])
        if i == 0:
            last = current
        else:
            last = np.concatenate((last, current), axis=0)

    index = []
    values = []
    for v in np.argsort(last)[::-1][:N]:
        index.append([v / 5, v % 5])
        values.append(last[v])
    return index, values


def predict(word):
    if word == 'jin':
        for i in found_from_oneword(jin_per)[0]:
            print jin[i]
    elif word == 'jintian':
        for i in found_from_twoword(jin_per, jintian_per)[0]:
            print jin[i[0]] + jintian[i[1]]
    elif word == 'wo':
        for i in found_from_oneword(wo_per)[0]:
            print wo[i]
    elif word == 'women':
        for i in found_from_twoword(wo_per, women_per)[0]:
            print wo[i[0]] + women[i[1]]
    elif word == 'jintianwo':
        index1, values1 = found_from_oneword(wo_per)
        index2, values2 = found_from_twoword(jin_per, jintian_per)
        last = np.multiply(values1, values1)
        for i in np.argsort(last)[::-1][:N]:
            print jin[index2[i][0]], jintian[index2[i][1]], wo[i]
    elif word == 'jintianwomen':
        index1, values1 = found_from_twoword(jin_per, jintian_per)
        index2, values2 = found_from_twoword(wo_per, women_per)
        last = np.multiply(values1, values1)
        for i in np.argsort(last)[::-1][:N]:
            print jin[index1[i][0]], jintian[index1[i][1]], wo[index2[i][0]], women[index2[i][1]]
    else:
        pass


if __name__ == '__main__':
    predict('jin')
    # 近
    # 斤
    # 今
    # 金
    # 尽
    predict('jintian')
    # 今天
    # 金田
    # 近天
    # 近填
    # 近田
    predict('wo')
    # 近
    # 斤
    # 今
    # 金
    # 尽
    predict('women')
    # 我们
    # 我闷
    # 我门
    # 我焖
    # 我扪
    predict('jintianwo')
    # 今 天 我
    # 金 田 窝
    # 近 天 喔
    # 近 填 握
    # 近 田 卧
    predict('jintianwomen')
    # 今 天 我 们
    # 金 田 我 闷
    # 近 田 我 扪
    # 近 填 我 焖
    # 近 天 我 门