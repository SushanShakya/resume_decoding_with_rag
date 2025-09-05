from unittest import TestCase

from src.ocr import OCR


class TestOCR(TestCase):
    def test_extract(self):
        text = OCR().extract_text()
        print(text)
