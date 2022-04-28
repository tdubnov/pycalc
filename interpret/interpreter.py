from typing import Optional

from lex.lexer import Lexer, ABCLexer
from interpret.ast import AST, Node, ABCAbstractSyntaxTree
from tokentypes.tokens import Context
from semantic.semantizer import Semantizer, ABCSemantizer


class Calculator:
    def __init__(self,
                 ctx: Context,
                 lexer: Optional[ABCLexer] = None,
                 semantizer: Optional[ABCSemantizer] = None,
                 ast_builder: Optional[ABCAbstractSyntaxTree] = None):
        self.ctx = ctx
        self._lexer = lexer or Lexer()
        self._tokenizer = semantizer or Semantizer()
        self._ast = ast_builder or AST()

    def execute(self, expression: str) -> float:
        return self._parse_expression(expression).execute(self._ast, self.ctx).value

    def _parse_expression(self, expression: str) -> Node:
        lexemes = self._lexer.lex(expression)
        tokens = self._tokenizer.semantize(lexemes)

        return self._ast.build(tokens)
