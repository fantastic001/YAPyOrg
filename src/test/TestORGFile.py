
from ..lib import ORGFile, ORGElement 

import unittest 

class TestORGFile(unittest.TestCase):
    
    def setUp(self):
        self.file = ORGFile("./test.org")
        self.document = self.file.getDocument()

    def test_sections(self):
        root, elems = self.document.createTree()
        self.assertEqual(len(root.getSubSections()), 5)
        self.assertEqual(root.getSubSections()[0].getTitle(), "Specific")
        self.assertEqual(root.getSubSections()[-1].getSubSections()[-1].getTitle(), "April 2017")
        self.assertTrue(root.getSubSections()[-1].getSubSections()[-1].isTODO())
