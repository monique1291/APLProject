import ply.lex as lex
import tokens
import newParser

with open('example.txt', 'r') as file:
    # Read the contents of the file and store them in a variable
    file_contents = file.read()

lexer = lex.lex(module=tokens)
# Open the file in read mode

lexer.input(file_contents)

for tok in lexer:
    print(tok)
