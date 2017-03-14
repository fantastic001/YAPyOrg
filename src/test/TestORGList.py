
from ..lib import ORGList, ORGElement

import unittest 

class TestORGList(unittest.TestCase):
    
    def test_parse(self):
        l = ORGList.parse("+a\n+ b\n+ c".split("\n"))
        self.assertEqual(l.getType(), ORGElement.ELEMENT_TYPE_LIST)
        self.assertEqual(l.getItems()[0].getText(), "a")
        self.assertEqual(l.getItems()[1].getText(), "b")
        self.assertEqual(l.getItems()[2].getText(), "c")
