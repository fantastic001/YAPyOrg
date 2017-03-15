
from .ORGDocument import * 

class ORGFile(object):
    
    def __init__(self, path):
        self.path = path 
        self.file = open(path)
        self.document = ORGDocument.parse(self.file.read().split("\n"))

    def getDocument(self):
        return self.document
