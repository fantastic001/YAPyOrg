
from ..lib import ORGDocument, ORGElement

import unittest 

class TestORGDocument(unittest.TestCase):
    
    def test_parse(self):
        document = ORGDocument.parse("some text\n* section\nblah".split("\n"))
        self.assertEqual(document.getElements()[1].getType(), ORGElement.ELEMENT_TYPE_SECTION)
    
    def test_parse_tree(self):
        document = ORGDocument.parse("some text\n* section\nblah".split("\n"))
        self.assertEqual(document.getElements()[1].getType(), ORGElement.ELEMENT_TYPE_SECTION)
        root, elems = document.createTree()
        self.assertEqual(root.getLevel(), 0)
        self.assertEqual(len(root.getElements()), 1)
        self.assertEqual(elems, [])
        self.assertEqual(root.getSubSections()[0].getTitle(), "section")

    def test_output(self):
        document = ORGDocument.parse("some text\n* section\nblah".split("\n"))
        self.assertEqual(document.getOutput(), "some text\n* section\nblah")
