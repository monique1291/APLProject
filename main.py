import ply.lex as lex
import tokens

lexer = lex.lex(module=tokens)
data = '''
3 + 4
'''
lexer.input("b=4-3")

for tok in lexer:
    print(tok)

