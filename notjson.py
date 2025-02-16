from lexer import Lexer

class NotJson():
    def scan(self, source):
        l = Lexer(source)
        result = l.run()
        return result