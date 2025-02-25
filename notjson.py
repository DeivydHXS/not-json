from lexer import Lexer
from parser import Parser

class NotJson():
    def scan(self, source):
        l = Lexer(source)
        result = l.run()
        return result

    def parse(self, tokens):
        p = Parser(tokens)
        return p.parse()