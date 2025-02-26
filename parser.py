from lexer import TokenType
from expr import *

class Parser():
    def __init__(self, tokens=[]):
        self.tokens = tokens
        self.current = 0

    def run(self):
        statements = self.statement()
        return statements
    
    def statement(self):
        expr = self.expression()
        return expr
    
    def expression(self):
        if self.check(TokenType.LEFT_BRACE):
            return self.block()
        
        return self.assignment()
        
    def block(self):
        self.consume(TokenType.LEFT_BRACE, 'Expect \'{\' ')
        statements = []

        while not self.check(TokenType.RIGHT_BRACE) and not self.isAtEnd():
            statements.append(self.statement())

        self.consume(TokenType.RIGHT_BRACE, 'Expect \'}\' ')

        return Block(statements)
    
    def grouping(self):
        self.consume(TokenType.LEFT_BRACKET, 'Expect \'[\' ')
        statements = []

        while not self.check(TokenType.RIGHT_BRACKET) and not self.isAtEnd():
            statements.append(self.statement())
            self.consume(TokenType.COMMA, 'Expect \',\'')

        self.consume(TokenType.RIGHT_BRACKET, 'Expect \']\' ')

        return List(statements)

    def assignment(self):
        expr = self.primary()

        if self.match(TokenType.COLON):
            colon = self.previous()
            value = self.assignment()
            
            if isinstance(expr, Identifier):
                name = expr.name
                return Assign(name, value)

            return self.error(colon, 'Invalid assignment')
        
        return expr
    
    def primary(self):
        if self.match(TokenType.FALSE):
            return Literal(False)
        if self.match(TokenType.TRUE):
            return Literal(False)
        if self.match(TokenType.NONE):
            return Literal(None)
        
        if self.match(TokenType.NUMBER):
            return Literal(float(self.previous().lexeme))
        
        if self.match(TokenType.STRING):
            return Literal(self.previous().lexeme)
        
        if self.match(TokenType.IDENTIFIER):
            return Identifier(self.previous().lexeme)
        
        if self.check(TokenType.LEFT_BRACKET):
            return self.grouping()
        
        if self.check(TokenType.LEFT_BRACE):
            return self.block()

        return self.error(self.peek(), 'Expect expression')

        
    def isAtEnd(self):
        return self.peek().type == TokenType.EOF
    
    def peek(self):
        return self.tokens[self.current]
    
    def previous(self):
        return self.tokens[self.current - 1]
    
    def check(self, ttype):
        if self.isAtEnd():
            return False
        
        return self.peek().type == ttype
    
    def advance(self):
        if not self.isAtEnd():
            self.current += 1
        
        return self.previous()
    
    def match(self, tokenType):
        if self.check(tokenType):
            self.advance()
            return True
        
        return False
    
    def consume(self, ttype, message):
        if self.check(ttype):
            return self.advance()
        
        return self.error(self.peek(), message)


    def error(self, token, message):
        return self.loxError(token, message)
    
    def loxError(self, token, message):
        # TODO: Lox Error
        return token, message