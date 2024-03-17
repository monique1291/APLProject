import ply.yacc as yacc
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
literals = ['+', '-', '*', '/']
tokens = [
             'INTEGER',
             'STRING',
             'FLOAT',
             # Operators
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'EQUALSIGN',
             # Parentheses
             'LPAREN',
             'RPAREN',
             'LCURVEDBRACE',
             'RCURVEDBRACE',
             'LSQUAREDBRACKET',
             'RSQUAREDBRACKET',
             # Other symbols
             'COMMA',
             'LESSTHAN',
             'GREATERTHAN',
             'TILDE',
             'BACKSLASH',
             'VERTICALBAR',
             'QUOTATION',
             'APOSTROPHE',
             # Identifier
             'IDENTIFIER',
         ] + list(reserved.values())  # + literals #may be able to remove literals

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALSIGN = r'\='
t_LCURVEDBRACE = r'\{'
t_RCURVEDBRACE = r'\}'
t_LSQUAREDBRACKET = r'\['
t_RSQUAREDBRACKET = r'\]'
t_COMMA = r'\,'
t_LESSTHAN = r'\<'          # Less than symbol
t_GREATERTHAN = r'\>'       # More than symbol
t_TILDE = r'\~'             # Tilde
t_BACKSLASH = r'\\'         # Backslash
t_VERTICALBAR = r'\|'       # Vertical bar
t_QUOTATION = r'\”'         # Quotation
t_APOSTROPHE = r'\''          # Apostrophe


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


def t_IDENTIFIER(t):
    r'[A-Z_][a-zA-Z_0-9]*'
    t.value = t.value
    return t


def t_STRING(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'  # should i let all strings have same rules as identifiers?
    t.value = t.value
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

    # Build the lexer


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_int(p):
    'factor : INTEGER'
    p[0] = p[1]


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")