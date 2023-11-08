from sklearn.datasets import fetch_20newsgroups   #获取数据集
from sklearn.feature_extraction.text import TfidfVectorizer #TF-IDF文本特征提取

select = ['alt.atheism','comp.graphics','misc.forsale','rec.autos',
          'sci.crypt','soc.religion.christian','talk.politics.guns']
train=fetch_20newsgroups(subset='train',categories=select)
test=fetch_20newsgroups(subset='test',categories=select)

vectorizer = TfidfVectorizer() 
train_v=vectorizer.fit_transform(train.data)
test_v=vectorizer.transform(test.data)

print(test_v[0])
