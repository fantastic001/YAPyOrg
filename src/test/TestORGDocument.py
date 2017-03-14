
from ..lib import ORGDocument 

import unittest 

class TestORGDocument(unittest.TestCase):
    
    def test_parse(self):
        document = ORGDocument.parse("some text\n* section\nblah")
        self.assertEqual(document.getElements()[1].getType(), ORGElement.ELEMENT_TYPE_SECTION)
    
    def test_parse_tree(self):
        document = ORGDocument.parse("some text\n* section\nblah".split("\n"))
        self.assertEqual(document.getElements()[1].getType(), ORGElement.ELEMENT_TYPE_SECTION)
        root = document.createTree()
        self.assertEqual(root.getLevel(), 0)
        self.assertEqual(root.getElements(), ["some text"])
        self.assertEqual(root.getSubSections()[0].getTitle(), "section")
