import ply.lex as lex
from ply import yacc

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'elif': 'ELIF',
    'while': 'WHILE',
    'for': 'FOR',
    'do': 'DO',
    'until': 'UNTIL',
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
    'finally': 'FINALLY',
    'def': 'DEF',
    'break': 'BREAK',
    'case': 'CASE',
    'switch': 'SWITCH'

}
tokens = [
    'INT',
    'FLOAT',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'GREATERTHAN',
    'LESSTHAN',
    # Parentheses
    'LPAREN',
    'RPAREN',
    'LCURVEDBRACE',
    'RCURVEDBRACE',
    'LSQUAREDBRACKET',
    'RSQUAREDBRACKET',
]

t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'\/'
t_MULTIPLY = r'\*'
t_EQUALS = r'\='
t_GREATERTHAN = r'\>'
t_LESSTHAN = r'\<'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = r't'


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_NAME(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')
)


def calc(p):
    """
    calc: expression
        | empty
    """
    print(run(p[1]))


# In case of an EOF error for whatever reason
while True:
    try:
        s = input(1+(4*2))
    except EOFError:
        break

parser = yacc.yacc()


# run function
def run(p):
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
    if type(p) == tuple:
        if p[0] == '-':
            return run(p[1]) - run(p[2])
    if type(p) == tuple:
        if p[0] == '*':
            return run(p[1]) * run(p[2])
    if type(p) == tuple:
        if p[0] == '/':
            return run(p[1]) / run(p[2])
    else:
        return p


# GRAMMAR
