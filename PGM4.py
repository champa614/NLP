from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

docs = [
    "Python and Java are programming languages",
    "Python is used for machine learning",
    "Football and cricket are popular sports",
    "Cricket is played with bat and ball"
]

v = CountVectorizer(stop_words="english")
X = v.fit_transform(docs)

lda = LatentDirichletAllocation(n_components=2, random_state=0)
lda.fit(X)

words = v.get_feature_names_out()

for i, topic in enumerate(lda.components_):
    top = topic.argsort()[-5:][::-1]
    print("Topic", i + 1, ":", [words[j] for j in top])