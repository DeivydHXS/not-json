from enum import Enum, auto

class TokenType(Enum):
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_BRACKET = 0
    RIGHT_BRACKET = auto()

    COLON = auto()
    COMMA = auto()

    NUMBER = auto()
    STRING = auto()
    IDENTIFIER = auto()
    NONE = auto()
    FALSE = auto()
    TRUE = auto()
    LIST = auto()

    ERROR = auto()
    EOF = auto()

class Token():
    def __init__(self):
        self.type = None
        self.lexeme = ''
        self.line = 0

class Lexer():
    def __init__(self, source = ''):
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 0
        self.atEnd = False
    
    def run(self):
        result = []
        while(True):
            tok = self.scanToken()
            if tok.type == TokenType.EOF:
                result.append(tok)
                break

            result.append(tok)
        
        return result

    def scanToken(self):
        if self.atEnd:
            return self.makeToken(TokenType.EOF)

        self.skipWhitespace()
        self.start = self.current

        c = self.advance()

        if self.isAlpha(c):
            return self.identifier()
        
        if self.isDigit(c):
            return self.number()

        match c:
            case '{':
                return self.makeToken(TokenType.LEFT_BRACE)
            case '}':
                return self.makeToken(TokenType.RIGHT_BRACE)
            case '[':
                return self.makeToken(TokenType.LEFT_BRACKET)
            case ']':
                return self.makeToken(TokenType.RIGHT_BRACKET)
            case ',':
                return self.makeToken(TokenType.COMMA)
            case ':':
                return self.makeToken(TokenType.COLON)
            case '\'':
                self.start = self.current
                return self.string()
            
        return self.errorToken('Unexpected character') 
    
    def isDigit(self, c):
        if self.isAtEnd():
            return False
        
        return c >= '0' and c <= '9'
    
    def isAlpha(self, c):
        if self.isAtEnd():
            return False

        return c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z' or c == '_'

    def identifier(self):
        while self.isAlpha(self.peek()) or self.isDigit(self.peek()):
            self.advance()

        return self.makeToken(self.identifierType())

    def identifierType(self):
        match self.source[self.start]:
            case 'f':
                return self.checkKeyword('alse', TokenType.FALSE)
            case 't':
                return self.checkKeyword('rue', TokenType.TRUE)
        
        return TokenType.IDENTIFIER

    def isKeywordEqual(self, rest):
        if (self.source[self.start] + rest) == self.source[self.start:self.current]:
            return True

        return False

    def checkKeyword(self, rest, ttype):
        if self.isKeywordEqual(rest):
            return ttype

        return TokenType.IDENTIFIER

    def number(self):
        while self.isDigit(self.peek()):
            self.advance()
        
        if self.peek() == '.' and self.isDigit(self.peekNext()):
            self.advance()
            while self.isDigit(self.peek()):
                self.advance()

        return self.makeToken(TokenType.NUMBER)


    def string(self):
        while self.peek() != '\'' and not self.isAtEnd():
            if self.peek() == '\n':
                self.line += 1
            self.advance()
        if self.isAtEnd():
            return self.errorToken("Unterminated string")
        
        result = self.makeToken(TokenType.STRING)
        self.advance()
        return result


    def skipWhitespace(self):
        while True:
            c = self.peek()
            match c:
                case ' ' | '\r' | '\t':
                    self.advance()
                case '\n':
                    self.line += 1
                    self.advance()
                case '/':
                    print(ord(c), c)
                    if self.peekNext() == '/':
                        while self.peek() != '\n' and (not self.isAtEnd()):
                            self.advance()
                        else:
                            return
                case _:
                    return
                
    def peekNext(self):
        if self.isAtEnd():
            return '\0'
        
        return self.source[self.current + 1]

    def peek(self):
        if self.isAtEnd():
            return '\0'
        return self.source[self.current]

    def match(self, expected):
        if self.isAtEnd():
            return False
        
        if self.current != expected:
            return False
        
        self.current += 1
        return True

    def isAtEnd(self):
        if self.current == len(self.source):
            self.atEnd = True
            return True
        return False
    
    def advance(self):
        self.current += 1
        return self.source[self.current - 1]
    
    def makeToken(self, type):
        tok = Token()
        tok.type = type
        tok.line = self.line
        if type == TokenType.EOF:
            tok.lexeme = ''
            return tok
        tok.lexeme = self.source[self.start:self.current]
        return tok

    def errorToken(self, message):
        tok = Token()
        tok.type = TokenType.ERROR
        tok.lexeme = message
        tok.line = self.line
        return tok