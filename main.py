import ply.lex as lex
from newParser import parser
#import semantics
import tokens
import sys

# example.txt should act as source code
try:
    # Open the file in read mode
    with open('example.txt', 'r') as file:
        # Read the contents of the file and store them in a variable
        file_contents = file.read()
except FileNotFoundError:
    print("File 'example.txt' not found.")
    sys.exit(1)
except IOError as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

# Build the lexer and pass it the source code
lexer = lex.lex(module=tokens)
lexer.input(file_contents)

# Build the parser and pass it the tokens
result = parser.parse(lexer=lexer)

print(result)

#semantics.analyze(result)