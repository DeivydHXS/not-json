from lexer import Lexer
from parser import Parser
from expr import *

class NotJson():
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
    
    def dumps(self, source):
        self.lexer.source = source
        tokens = self.lexer.run()

        self.parser.tokens = tokens
        block = self.parser.run()
        
        return self.makeBlock(block)
    
    def loads(self):
        pass
    
    def makeList(self, l):
        result = []
        for i in l.value:
            result.append(i.value)
        return result

    def makeBlock(self, block):
        result = {}
        for e in block.value:
            if isinstance(e, Assign):
                if isinstance(e.value, Literal):
                    result[e.name] = e.value.value
                elif isinstance(e.value, List):
                    result[e.name] = self.makeList(e.value)
                elif isinstance(e.value, Block):
                    result[e.name] = self.makeBlock(e.value)
        return result