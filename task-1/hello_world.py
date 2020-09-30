#!/usr/bin/env python3

class TokenType:
    LPAREN = 0
    RPAREN = 1
    STRING = 2
    IDENT = 3
    EOF = 4


class Token:
    def __init__(self, token_type: int, token_literal: str = ""):
        self.type = token_type
        self.literal = token_literal


class Lexer:
    def __init__(self, code: str):
        self.__code = code
        self.__position = 0
        self.__position_read = 0
        self.__char = None
        self.__read_char()

    def next_token(self) -> Token:
        position = self.__position
        def __isnext(): return position < self.__position
        def __maybe(arr): return next(iter(arr), 0)

        token_type = {
            '(': TokenType.LPAREN,
            ')': TokenType.RPAREN,
            '"': TokenType.STRING,
            None: TokenType.EOF,
        }.get(self.__char, TokenType.IDENT)

        [should_stop, *extra] = {
            TokenType.LPAREN: [__isnext],
            TokenType.RPAREN: [__isnext],
            TokenType.IDENT:  [lambda: not ('A' <= self.__char <= 'z')],
            TokenType.STRING: [lambda: __isnext() and self.__char == '"' and self.__read_char(), 1, 1],
            TokenType.EOF: [lambda: True],
        }.get(token_type)

        position += __maybe(extra)
        skip = __maybe(extra)
        while not should_stop():
            self.__read_char()
        return Token(token_type, self.__code[position:self.__position - skip])

    def __read_char(self):
        if self.__position_read >= len(self.__code):
            self.__char = None
        else:
            self.__char = self.__code[self.__position_read]
        self.__position = self.__position_read
        self.__position_read += 1
        return self.__char


class AST:
    pass


class ASTCallExpression(AST):

    def __init__(self, function, arguments):
        self.function = function
        self.arguments = arguments


class ASTStringLiteral(AST):

    def __init__(self, value):
        self.value = value


class ASTIdentifier(AST):
    def __init__(self, name):
        self.name = name


class ASTProgram(AST):
    def __init__(self, statements):
        self.statements = statements


class Parser:

    def __init__(self, lexer: Lexer):
        self.__cur = None
        self.__peek = None
        self.__lexer = lexer
        self.__prefix_fn = {
            TokenType.IDENT: self.__parse_ident,
            TokenType.STRING: self.__parse_string,
            # TokenType.LPAREN: self.__parse_grouped
        }
        self.__infix_fn = {
            TokenType.LPAREN: self.__parse_call
        }
        self.__next_token()
        self.__next_token()

    def __next_token(self):
        self.__cur = self.__peek
        self.__peek = self.__lexer.next_token()

    def __cur_token_is(self, token_type: int):
        return self.__cur.type == token_type

    def __peek_precedence(self):
        return {TokenType.LPAREN: 1}.get(self.__peek.type, 0)

    def parse(self):
        statements = []
        while not self.__cur_token_is(TokenType.EOF):
            statements.append(self.__parse_statement())
            self.__next_token()
        return ASTProgram(statements)

    def __parse_expression(self, precedence: int = 0):
        prefix = self.__prefix_fn.get(self.__cur.type)
        if not prefix:
            return
        left = prefix()
        while precedence < self.__peek_precedence():
            infix = self.__infix_fn[self.__peek.type]
            if not infix:
                return left
            self.__next_token()
            left = infix(left)
        return left

    def __parse_expression_list(self, end: int):
        exps = []
        if self.__peek.type == end:
            self.__next_token()
            return exps
        self.__next_token()
        exps.append(self.__parse_expression())
        return exps

    def __parse_statement(self):
        return self.__parse_expression()

    def __parse_ident(self):
        return ASTIdentifier(self.__cur.literal)

    def __parse_string(self):
        return ASTStringLiteral(self.__cur.literal)

    def __parse_call(self, function: AST):
        return ASTCallExpression(
            function=function,
            arguments=self.__parse_expression_list(TokenType.LPAREN)
        )


class Evaluator:
    def __init__(self, lexer: Lexer, parser: Parser):
        self.__lexer_class = lexer
        self.__parser_class = parser
        self.__builtin = {'print': print, 'len': len}

    def eval(self, code: str):
        ast = self.__parser_class(self.__lexer_class(code)).parse()
        return self.__eval_ast(ast)

    def __eval_ast(self, node: AST):
        if isinstance(node, ASTProgram):
            return self.__eval_ast_list(node.statements)
        elif isinstance(node, ASTStringLiteral):
            return node.value
        elif isinstance(node, ASTCallExpression):
            args = self.__eval_ast_list(node.arguments)
            if (fn := self.__builtin.get(node.function.name)):
                return fn(*args)

    def __eval_ast_list(self, ast_list):
        return list(map(self.__eval_ast, ast_list))


def test_lexer():
    tests = [
        Token(TokenType.IDENT, 'print'),
        Token(TokenType.LPAREN, '('),
        Token(TokenType.STRING, 'hello world'),
        Token(TokenType.RPAREN, ')'),
        Token(TokenType.EOF),
    ]
    lexer = Lexer('print("hello world")')
    for test in tests:
        token = lexer.next_token()
        assert test.type == token.type
        assert test.literal == token.literal


if __name__ == '__main__':
    evaluator = Evaluator(lexer=Lexer, parser=Parser)
    evaluator.eval('print("hello world")')
    assert 11 in evaluator.eval('len("hello world")')
