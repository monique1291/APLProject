from token import NUMBER
from ply import lex
import keyword

import tokens
lexer = lex.lex(module=tokens)
data = '''
3 + 4
'''
lexer.input("3+4 Moni Que")

for tok in lexer:
    print(tok)