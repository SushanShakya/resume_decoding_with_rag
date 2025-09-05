from unittest import TestCase
from src.llm import LLM
from src.ocr import OCR
from src.prompt import Prompt
from src.utils import Utils


class TestLLM(TestCase):

    def test_ask(self):
        ocr = OCR(docpath=Utils.asset_path("resume.jpg"))
        system_prompt = ocr.extract_text()
        llm = LLM(system_prompt)
        question = "What is the latest work experience ?"
        answer = llm.ask(question)
        print(answer)
