from token import NUMBER

from ply import lex

import tokens
lexer = lex.lex(module=tokens)
data = '''
3 + 4
'''
lexer.input("3+4")

for tok in lexer:
    print(tok)