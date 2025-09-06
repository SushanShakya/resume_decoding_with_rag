import re


class Chunker:
    def __init__(self, delimeter="r'(?<=[.?!])\s+'", chunk_size=100):
        self.delimeter = delimeter
        self.chunk_size = chunk_size

    def chunk(self, text):
        sentences = re.split(r"(?<=[.?!])\s+", text)
        chunks = []
        chunk = ""
        for s in sentences:
            if len(chunk) + len(s) < self.chunk_size:
                chunk += " " + s
            else:
                chunks.append(chunk.strip())
                chunk = s
        if chunk:
            chunks.append(chunk.strip())
        return chunks
