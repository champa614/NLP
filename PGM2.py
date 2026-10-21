from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = [
    "Python is a programming language.",
    "Machine learning uses data to learn.",
    "NLP processes human language.",
]

question = input("Enter your question: ")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs + [question])
scores = cosine_similarity(X[-1], X[:-1])

print("Answer:", docs[scores.argmax()])