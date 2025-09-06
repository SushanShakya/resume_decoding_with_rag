from unittest import TestCase

from src.embedder import Embedder


class TestEmbedder(TestCase):
    def test_embed(self):
        e = Embedder()
        text = ["Sushan"]
        embeddings = e.embed(text)
        self.assertEqual(embeddings.shape[0], 1)

        texts = [
            "The weather is sunny",
            "Hello World",
        ]
        embeddings = e.embed(texts)
        self.assertEqual(embeddings.shape[0], 2)

    def test_distance(self):
        e = Embedder()
        text = ["Sushan Shakya"]
        embeddings = e.embed(text)
        query = text
        diff = e.difference(query, embeddings)

        self.assertEqual(diff, 0)
