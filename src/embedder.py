from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def embed(self, texts):
        self.last_encoding = self.embedder.encode(texts)
        return self.last_encoding
