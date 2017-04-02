
from ..lib.ORGTable import * 
import unittest 

class TestORGTable(unittest.TestCase):
    
    def test_simple(self):
        content = "| a | b |\n"
        table, lines = ORGTable.parse(content.split("\n"))
        self.assertEqual(table.getRows()[0].getItems(), ["a", "b"])
    
    def test_simple_more_rows(self):
        content = "| a | b |\n| c | d |"
        table, lines = ORGTable.parse(content.split("\n"))
        self.assertEqual(table.getRows()[0].getItems(), ["a", "b"])
        self.assertEqual(table.getRows()[1].getItems(), ["c", "d"])
    
    def test_simple_more_rows_with_heading(self):
        content = "| a | b |\n------------\n| c | d |"
        table, lines = ORGTable.parse(content.split("\n"))
        self.assertEqual(table.getRows()[0].getItems(), ["a", "b"])
        self.assertEqual(table.getRows()[1].getItems(), ["c", "d"])
        self.assertTrue(table.getRows()[0].isHeading())

    def test_output(self):
        content = "| a | b |\n---------\n| c | d |\n"
        table, lines = ORGTable.parse(content.split("\n"))
        self.assertEqual(table.getOutput(), content)
        
