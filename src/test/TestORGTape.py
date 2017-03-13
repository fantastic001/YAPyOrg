

import unittest 

from ..lib import ORGTape

class TestORGTape(unittest.TestCase):
    def setUp(self):
        pass 

    def test_current_next(self):
        tape = ORGTape("A\nB")
        self.assertEqual(tape.current(), "A")
        tape.next()
        self.assertEqual(tape.current(), "B")

    def test_finished(self):
        tape = ORGTape("1\n2\n3")
        tape.next()
        tape.next()
        tape.next()
        self.assertTrue(tape.finished())
        tape.next()
        self.assertTrue(tape.finished())
