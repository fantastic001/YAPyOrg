
from .ORGElement import * 

class ORGSection(ORGElement):
    
    def __init__(self, title, **kw):
        self.title = title.strip()
        self.level = kw.get("level", 1)
        self.todo = kw.get("TODO", False)
        self.done = kw.get("DONE", False)

    def parse(lines):
            """
            Returns new object with this element which is trying to parse 
        
            lines: list of lines to parse
        
            returns: tuple (ORGElement or its child, remaining_lines)
        
            remaining_lines - list of lines that are not parsed
        
            if parsing cannot be done then (None, lines) is returned 
            """
            title = lines[0]
            if "*" == title[0]:
                level = 1
                while title[level] == "*":
                    level = level + 1
                if title[level] != " ":
                    return (None, lines)
                else:
                    heading = title[level+1:]
                    todo = heading[:4] == "TODO"
                    done = heading[:4] == "DONE"
                    if todo or done:
                        heading = heading[4:]
                    return (ORGSection(heading.strip(), level=level, TODO=todo, DONE=done), lines[1:])
            else:
                return (None, lines)

    def getType(self):
        """
        Returns one of types listed above
        """
        return ORGElement.ELEMENT_TYPE_SECTION

    def getTitle(self):
        return self.title

    def getLevel(self): 
        return self.level

    def setTODO(self):
        self.todo = True 
    def isTODO(self):
        return self.todo 
    def setDONE(self):
        self.done = True
    def isDONE(self):
        return self.done
