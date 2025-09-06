from unittest import TestCase

from src.chunker import Chunker


class TestChunker(TestCase):

    def test_create(self):
        delimeter = r"(?<=[.?!])\s+"
        Chunker(delimeter)

    def test_chunk(self):
        c = Chunker()
        text = "Hello World. This is the greatest"
        chunks = c.chunk(text)
        self.assertEqual(len(chunks), 1)

        text = "akldjfaskfjlskjflasjdf;lsdajflasjfl;asjf;laksj;flsjf;lasjf;laskjf;lasjflsajflasjflasjflsajflajdf. asdfj;laskjf;laskdjf;alsdkjf;laskdjf;laskdjf;laskjdf;laskjflaskfj;lasdkjf;lasjdfl;aksjdflaskjflaskjflskjflasjflskfjas;lkfj."
        chunks = c.chunk(text)
        self.assertEqual(len(chunks), 2)
