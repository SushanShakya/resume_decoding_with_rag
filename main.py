import numpy as np
from src.chunker import Chunker
from src.embedder import Embedder
from src.llm import LLM
from src.ocr import OCR
from src.utils import Utils


def main():
    ocr = OCR(docpath=Utils.asset_path("europass_resume.jpg"))
    content = ocr.extract_text()

    chunks = Chunker().chunk(content)

    e = Embedder()
    embeddings = Embedder().embed(chunks)

    query = "Work"
    scores = e.similarity(query, embeddings)

    top_k = 3
    top_indices = np.argsort(scores)[-top_k:][::-1]

    context = " ".join([chunks[i] for i in top_indices])

    llm = LLM(context)
    questions = [
        "What is the position where the person is working ?",
        "What is the name of the company where the person is working ?",
        "How many years of experience does the person have ?",
    ]
    for question in questions:
        answer = llm.ask(question)
        print()
        print(answer)
        print()


if __name__ == "__main__":
    main()
