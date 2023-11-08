from sklearn.feature_extraction.text import CountVectorizer

# 创建CountVectorizer对象
vectorizer = CountVectorizer()

# 输入任意文本
text = ["ba ba ba balab balab ba ba ba da da da"]

# 将文本进行向量化
vectorized_text = vectorizer.fit_transform(text)

# 输出向量结果
print(vectorizer.get_feature_names_out())
print(vectorized_text.toarray())
