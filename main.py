import ply.lex as lex
import tokens

lexer = lex.lex(module=tokens)
data = '''
3 + 4
'''
lexer.input("Major Landing in sequence.")

for tok in lexer:
    print(tok)

