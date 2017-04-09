
from ..lib.ORGTable import * 
import unittest 

class TestORGTable(unittest.TestCase):
    
    def test_simple(self):
        content = "| a | b |\n"
        table, lines = ORGTable.parse(content.split("\n"))
        self.assertEqual(table.getRows()[0].getItems(), ["a", "b"])
    
    def test_simple_two_rows(self):
        content = "| a | b |\n| c | d |"
        table, lines = ORGTable.parse(content.split("\n"))
        self.assertEqual(table.getRows()[0].getItems(), ["a", "b"])
        self.assertEqual(table.getRows()[1].getItems(), ["c", "d"])
    
    def test_simple_more_rows(self):
        content = "| a | b | c |\n| c | d | e|\n| f | g | h |"
        table, lines = ORGTable.parse(content.split("\n"))
        self.assertEqual(table.getRows()[0].getItems(), ["a", "b", "c"])
        self.assertEqual(table.getRows()[1].getItems(), ["c", "d", "e"])
        self.assertEqual(table.getRows()[2].getItems(), ["f", "g", "h"])

    
    def test_simple_two_rows_with_heading(self):
        content = "| a | b |\n------------\n| c | d |"
        table, lines = ORGTable.parse(content.split("\n"))
        self.assertEqual(table.getRows()[0].getItems(), ["a", "b"])
        self.assertEqual(table.getRows()[1].getItems(), ["c", "d"])
        self.assertTrue(table.getRows()[0].isHeading())
    
    def test_simple_more_rows_with_heading(self):
        content = "| a | b | c |\n------------\n| d | e | f |\n| g | h | i |"
        table, lines = ORGTable.parse(content.split("\n"))
        self.assertEqual(table.getRows()[0].getItems(), ["a", "b", "c"])
        self.assertEqual(table.getRows()[1].getItems(), ["d", "e", "f"])
        self.assertEqual(table.getRows()[2].getItems(), ["g", "h", "i"])
        self.assertTrue(table.getRows()[0].isHeading())
        self.assertFalse(table.getRows()[1].isHeading())
        self.assertFalse(table.getRows()[2].isHeading())

    def test_output_simple(self):
        content = "| a | b |\n---------\n| c | d |\n"
        table, lines = ORGTable.parse(content.split("\n"))
        self.assertEqual(table.getOutput(), content)
        
    def test_output_more_rows(self):
        content = "| a | b |\n---------\n| c | d |\n| e | f |"
        table, lines = ORGTable.parse(content.split("\n"))
        self.assertEqual(table.getOutput(), content+"\n")
