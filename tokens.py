reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'elif': 'ELIF',
    'while': 'WHILE',
    'for': 'FOR',
    'do': 'DO',
    'until': 'UNTIL',
    'int': 'INT',
    'str': 'STR',
    'float': 'FLT',
    'bool': 'BOOL',
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
    'finally': 'FINALLY',
    'def': 'DEF',
    'break': 'BREAK',
    'case': 'CASE',
    'switch': 'SWITCH',
    'variable': 'VARIABLE',
    'array': 'ARRAY',
    'closeclass': 'CLOSECLASS',
    'endif': 'ENDIF',
    'closefunc': 'CLOSEFUNC',
    'print': 'PRINT'
}

tokens = [
             'INTEGER',
             'STRING',
             'FLOAT',
             # Comparison Operators
             'EQUALEQUAL',
             'NOTEQUAL',
             'LESSTHAN',
             'GREATERTHAN',
             'LESSEQUAL',
             'GREATEREQUAL',
             # Operators
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'EQUAL',
             'PLUSEQUAL',
             'MINUSEQUAL',
             'TIMESEQUAL',
             'DIVIDEEQUAL',
             # Parentheses
             'LPAREN',
             'RPAREN',
             'LCURVEDBRACE',
             'RCURVEDBRACE',
             'LSQUAREDBRACKET',
             'RSQUAREDBRACKET',
             # Other symbols
             'COMMA',
             'DOUBLEQUOTES',
             'SINGLEQUOTES',
             'COLON',
             # Identifier
             'IDENTIFIER',
             'COMMENTS',
             'RULE_OPEN',
             'RULE_CLOSE',
             'RANGE',
         ] + list(reserved.values())  # + literals

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'\='
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_TIMESEQUAL = r'\*='
t_DIVIDEEQUAL = r'/='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURVEDBRACE = r'\{'
t_RCURVEDBRACE = r'\}'
t_LSQUAREDBRACKET = r'\['
t_RSQUAREDBRACKET = r'\]'
t_COMMA = r'\,'
t_DOUBLEQUOTES = r'\"'
t_SINGLEQUOTES = r'\''
t_COLON = r'\:'

# Regular expression rule for comparison operators
t_EQUALEQUAL = r'\=='
t_NOTEQUAL = r'\!='
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_LESSEQUAL = r'\<='
t_GREATEREQUAL = r'\>='


# Regular expression rule for comments
def t_COMMENT(t):
    r'\#.*'
    pass  # Discard comments


# A regular expression rule with some action code
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)
