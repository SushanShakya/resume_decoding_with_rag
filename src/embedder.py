from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_distances, cosine_similarity


class Embedder:
    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def similarity(self, query, embeddings):
        e = self.embed(query).reshape(1, -1)
        return cosine_similarity(e, embeddings)[0]

    def difference(self, query, embeddings):
        e = self.embed(query)
        return cosine_distances(e, embeddings)[0]

    def embed(self, texts):
        self.last_encoding = self.embedder.encode(texts)
        return self.last_encoding
