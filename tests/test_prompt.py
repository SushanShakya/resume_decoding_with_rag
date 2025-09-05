from unittest import TestCase

from src.prompt import Prompt


class TestPrompt(TestCase):
    def test_system_prompt(self):
        prompt = Prompt.system()
        self.assertIsNotNone(prompt)
