from lexer import Lexer
from parser import Parser
from expr import Listy

class NotJson():
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
    
    def dumps(self, source):
        self.lexer.source = source
        tokens = self.lexer.run()

        # for e in tokens:
        #     print(e.type, e.lexeme)

        self.parser.tokens = tokens
        exprs = self.parser.run()
        # print(exprs)

        result = {}
        for e in exprs:
            result[e.name] = self.makeList(e.value) if isinstance(e.value, Listy) \
                                                    else e.value.value

        # print(result)
        return result

    def makeList(self, l):
        result = []
        for i in l.value:
            result.append(i.value)
        return result
