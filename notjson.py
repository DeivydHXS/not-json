from lexer import Lexer
from parser import Parser
from expr import *

class NotJson():
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
    
    # Take a dict and convert to a not-json string
    def dumps(self, pydict):
        return self.dumpDict(pydict)
    
    def dumpList(self, pylist):
        result = ''
            
        for idx, e in enumerate(pylist):
            if isinstance(e, str):
                result += '\'' + e + '\''
            elif isinstance(e, float):
                result += str(e)
            elif isinstance(e, bool):
                result += 'true' if e else 'false'
            elif isinstance(e, list):
                result += '[' + self.dumpList(e) + '] '
            elif isinstance(e, dict):
                result += self.dumpList(e) + ' '

            if not idx + 1 == len(pylist):
                result += ', '

        return result

    def dumpDict(self, pydict):
        notJsonString = '{ '

        for name, value in pydict.items():
            if isinstance(value, str):
                notJsonString += name + ': \'' + str(value) + '\' '
            elif isinstance(value, float):
                notJsonString += name + ': ' + str(value) + ' '
            elif isinstance(value, bool):
                notJsonString += name + ': '
                notJsonString += 'true' if value else 'false'
                notJsonString += ' '
            elif isinstance(value, list):
                notJsonString += name + ': [' + self.dumpList(value) + '] '
            elif isinstance(value, dict):
                notJsonString += name + ': ' + self.dumpDict(value) + ' '

        notJsonString += '}'
        return notJsonString

    # Take some not-json string and convert to a dict
    def loads(self, source):
        self.lexer.source = source
        tokens = self.lexer.run()

        self.parser.tokens = tokens
        block = self.parser.run()
        
        return self.loadBlock(block)

    def loadList(self, l):
        result = []
        for i in l.value:
            result.append(i.value)
        return result

    def loadBlock(self, block):
        result = {}
        for e in block.value:
            if isinstance(e, Assign):
                if isinstance(e.value, Literal):
                    result[e.name] = e.value.value
                elif isinstance(e.value, List):
                    result[e.name] = self.loadList(e.value)
                elif isinstance(e.value, Block):
                    result[e.name] = self.loadBlock(e.value)
        return result