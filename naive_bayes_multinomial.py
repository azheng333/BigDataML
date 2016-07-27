#coding=utf-8
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from pprint import pprint


newsgroups_train = fetch_20newsgroups(subset='train')
pprint(list(newsgroups_train.target_names))
#20个主题
# ['alt.atheism',
#  'comp.graphics',
#  'comp.os.ms-windows.misc',
#  'comp.sys.ibm.pc.hardware',
#  'comp.sys.mac.hardware',
#  'comp.windows.x',
#  'misc.forsale',
#  'rec.autos',
#  'rec.motorcycles',
#  'rec.sport.baseball',
#  'rec.sport.hockey',
#  'sci.crypt',
#  'sci.electronics',
#  'sci.med',
#  'sci.space',
#  'soc.religion.christian',
#  'talk.politics.guns',
#  'talk.politics.mideast',
#  'talk.politics.misc',
#  'talk.religion.misc']

#这里选取4个主题
categories = ['rec.sport.baseball', 'alt.atheism', 'talk.politics.guns', 'sci.space']

#狭窄这4个主题
twenty_train = fetch_20newsgroups(subset='train', categories=categories)


#文件内容在twenty_train这个变量里，现在对内容进行分词和向量化操作
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)


#接着对向量化之后的结果做TF-IDF转换
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

from sklearn.neighbors.nearest_centroid import NearestCentroid

clf = NearestCentroid().fit(X_train_tfidf, twenty_train.target)

#创建测试集合，这里有2条数据，每条数据一行内容，进行向量化和tf-idf转换
docs_new = ['God is love', 'OpenGL on the GPU is fast']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

#预测
predicted = clf.predict(X_new_tfidf)

#打印结果
for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, twenty_train.target_names[category]))