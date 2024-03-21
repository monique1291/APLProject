import ply.lex as lex

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'elif': 'ELIF',
    'while': 'WHILE',
    'for': 'FOR',
    'do': 'DO',
    'until': 'UNTIL',
    'end': 'END',
    'Int': 'INT',
    'Str': 'Str',
    'Double': 'Double',
    'Float': 'Float',
    'Bool': 'Bool',
    'func': 'FUNC',
    'return': 'RETURN',
    'main': 'MAIN',
    'and': 'AND',
    'false': 'FALSE',
    'true': 'TRUE',
    'class': 'CLASS',
    'import': 'IMPORT',
    'global': 'GLOBAL',
    'not': 'NOT',
    'or': 'OR',
    'is': 'IS',
    'in': 'IN',
    'range': 'RANGE',
    'finally': 'FINALLY',
    'def': 'DEF',
    'break': 'BREAK',
    'case': 'CASE',
    'switch': 'SWITCH',
    'else_if': 'ELSE_IF',
    'print': 'PRINT',

}
# Define the lexer tokens
tokens = list(reserved.values()) + [

    'LPAREN',
    'RPAREN',
    'CONDITION',
    'RULE_OPEN',
    'RULE_CLOSE',
    'IDENTIFIER',
    'COMMENT',
    'CODE_BLOCK',  # Token for code blocks
    'COLON',
    'COMMA',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALTO',
    'EQUALSIGN',
    'PLUSEQUAL',
    'MINUSEQUAL',
    'TIMESEQUAL',
    'DIVIDEEQUAL',
]

# Regular expression rules for tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_RULE_OPEN = r'RULE_OPEN'
t_RULE_CLOSE = r'RULE_CLOSE'
t_COLON = r':'
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALTO = r'=='
t_EQUALSIGN = r'\='
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_TIMESEQUAL = r'\*='
t_DIVIDEEQUAL = r'/='

# Ignored characters (whitespace)
t_ignore = ' \t\n'


def t_COMMENT(t):
    r'\#.*'
    pass  # Discard comments


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check if it's a reserved word
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


'''
def t_CODE_BLOCK(t):
    r'\{a-zA-Z_0-9.*?\}'  # Matches anything enclosed in curly braces
    t.value = t.value[1:-1]  # Remove the curly braces
    return t
'''


# Error handling rule
def t_error(t):
    print(f"Unexpected character: {t.value[0]}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Example input code
input_code = """
IF some_condition
    # Code to execute if the condition is true
ELSE
    # Code to execute if the condition is false
END
"""

# Tokenize the input
lexer.input(input_code)

# Print the tokens
for token in lexer:
    print(f"Token: {token.type}, Value: {token.value}")
