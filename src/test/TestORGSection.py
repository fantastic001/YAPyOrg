
from ..lib import ORGSection

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
        section, c = ORGSection.parse(["Section"])
        self.assertEqual(section, None)
    
    def test_parse_simple(self):
        section, c = ORGSection.parse(["* Section"])
        self.assertEqual(section.getTitle(), "Section")

    def test_parse_TODO(self):
        section, c = ORGSection.parse(["* TODO Section"])
        self.assertEqual(section.getTitle(), "Section")
        self.assertTrue(section.isTODO())

    def test_parse_DONE(self):
        section, c = ORGSection.parse(["* DONE Section"])
        self.assertEqual(section.getTitle(), "Section")
        self.assertTrue(section.isDONE())
    
    def test_parse_level(self):
        section, c = ORGSection.parse(["** Section"])
        self.assertEqual(section.getTitle(), "Section")
        self.assertEqual(section.getLevel(), 2)

    def test_parse_complex(self):
        section, c = ORGSection.parse("* Section 1\nsome text\n** Section 2\nsome other text\n*** Section 3\n* New section\nbla".split("\n"))
        self.assertEqual(section.getTitle(), "Section 1")
