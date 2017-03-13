
from ..lib import ORGSection
from ..lib import ORGTape

import unittest

class TestORGSection(unittest.TestCase):
    def test_creation(self):
        section = ORGSection("   Section 1 ")
        self.assertEqual(section.getTitle(), "Section 1")
        section.setTODO()
        self.assertTrue(section.isTODO())
        section.setDONE()
        self.assertTrue(section.isDONE())
        self.assertEqual(section.getLevel(), 1)
        section = ORGSection("Section 2", level=2)
        self.assertEqual(section.getLevel(), 2)
    
    def test_parse_none(self):
        section = ORGSection.parse(ORGTape("Section"))
        self.assertEqual(section, None)
    
    def test_parse_simple(self):
        section = ORGSection.parse(ORGTape("* Section"))
        self.assertEqual(section.getTitle(), "Section")

    def test_parse_TODO(self):
        section = ORGSection.parse(ORGTape("* TODO Section"))
        self.assertEqual(section.getTitle(), "Section")
        self.assertTrue(section.isTODO())

    def test_parse_DONE(self):
        section = ORGSection.parse(ORGTape("* DONE Section"))
        self.assertEqual(section.getTitle(), "Section")
        self.assertTrue(section.isDONE())
    
    def test_parse_level(self):
        section = ORGSection.parse(ORGTape("** Section"))
        self.assertEqual(section.getTitle(), "Section")
        self.assertEqual(section.getLevel(), 2)

    def test_parse_complex(self):
        section = ORGSection.parse(ORGTape("* Section 1\nsome text\n** Section 2\nsome other text\n*** Section 3\n* New section\nbla"))
        self.assertEqual(len(section.getElements()), 2)
        self.assertEqual(len(section.getSubSections()), 1)
        self.assertEqual(section.getSubSections()[0].getTitle(), "Section 2")


