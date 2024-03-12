import string

reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
    'for' : 'FOR',
    'do' : 'DO',
    'until' : 'UNTIL',
    'Int' :   'INT',
    'Str' :   'Str',
    'Double' :'Double',
    'Float' : 'Float',
    'Bool' :  'Bool',
    'func' : 'FUNC',
    'return' : 'RETURN',
    'main' : 'MAIN',
    'and' : 'AND',
    'false' : 'FALSE',
    'true' : 'TRUE',
    'class' : 'CLASS',
    'import' : 'IMPORT',
}
tokens = [
   'NUMBER',
#Operators
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'EQUALSIGN',
#Parentheses   
   'LPAREN',
   'RPAREN',
#Identifier
   'IDENTIFIER',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUALSIGN = r'\='

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_IDENTIFIER(t):
    r'[A-Z_][a-z_0-9]*'
    t.value = string(t.value)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
