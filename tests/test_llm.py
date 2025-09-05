from unittest import TestCase
from src.llm import LLM
from src.prompt import Prompt


class TestLLM(TestCase):

    def __create(self):
        docpath = "resume.jpg"
        return LLM(docpath)

    def test_ask(self):
        llm = self.__create()
        # question = Prompt.system()
        question = "Answer in 1000 words : Extract Text"
        answer = llm.ask(question)
