from src.utils import Utils
import torch


class LLM:
    def __init__(self, docpath):
        self.docpath = docpath
        self.llm = self.init_llm()

    def init_llm(self):
        from transformers import pipeline

        return pipeline(
            task="document-question-answering",
            model="naver-clova-ix/donut-base-finetuned-docvqa",
            device=0,
            dtype=torch.float16,
        )

    def ask(self, question):
        resume_path = Utils.asset_path(self.docpath)
        answer = self.llm(resume_path, question)
        print(answer)
        return answer
