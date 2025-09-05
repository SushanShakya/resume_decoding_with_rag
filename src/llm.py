from src.utils import Utils


class LLM:
    def __init__(
        self,
        system_prompt="",
    ):
        self.model = "distilbert/distilbert-base-cased-distilled-squad"
        self.llm = self.init_llm()
        self.system_prompt = system_prompt

    def init_llm(self):
        from transformers import pipeline

        return pipeline(
            "question-answering",
            model=self.model,
        )

    def ask(self, query):
        answer = self.llm(
            context=self.system_prompt,
            question=query,
        )
        return answer
