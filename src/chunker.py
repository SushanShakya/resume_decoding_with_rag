import re


class Chunker:
    def __init__(self, delimeter=r"[\n]+", chunk_size=500):
        self.delimeter = delimeter
        self.chunk_size = chunk_size

    def chunk(self, text):
        sentences = re.split(self.delimeter, text)
        chunks = []
        chunk = ""
        for s in sentences:
            chunk += f" {s}"
            if len(chunk) >= self.chunk_size:
                chunks.append(chunk.strip())
                chunk = ""

        return chunks
