import ply.lex as lex
import tokens

lexer = lex.lex(module=tokens)
data = '''
3 + 4
'''
lexer.input("M = ( 3 * 6) - Y + (6 / 2) , moni 9.9")

for tok in lexer:
    print(tok)

