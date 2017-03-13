

import unittest 

from ..lib import ORGText

class TestORGText(unittest.TestCase):
    def setUp(self):
        pass 

    def test_text(self):
        tape = ORGTape("A\nB\n* Section")
        text = ORGText.parse(tape)
        self.assertEqual(text.getText(), "A\nB")
        
        tape = ORGTape("* Section\nA\nB\n* Section")
        text = ORGText.parse(tape)
        self.assertEqual(text, None)
