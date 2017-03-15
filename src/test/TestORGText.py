

import unittest 

from ..lib import ORGText

class TestORGText(unittest.TestCase):
    def setUp(self):
        pass 

    def test_text(self):
        text, c = ORGText.parse("A\nB\n* Section".split("\n"))
        self.assertEqual(text.getText(), "A B")
        
        tape = "* Section\nA\nB\n* Section".split("\n")
        text, c = ORGText.parse(tape)
        self.assertEqual(text, None)
