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
literals = ['+', '-', '*', '/', '=', '<', '>', '(', ')', '{', '}', '[', ']', ',', ]
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
             'EQUALSIGN',
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
             # Identifier
             'IDENTIFIER',
             'COMMENTS',
         ] + list(reserved.values())  # + literals #may be able to remove literals

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALSIGN = r'\='
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_TIMESEQUAL = r'\*='
t_DIVIDEEQUAL = r'/='
t_LCURVEDBRACE = r'\{'
t_RCURVEDBRACE = r'\}'
t_LSQUAREDBRACKET = r'\['
t_RSQUAREDBRACKET = r'\]'
t_COMMA = r'\,'

# Regular expression rule for comparison operators
t_EQUALEQUAL = r'=='
t_NOTEQUAL = r'!='
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='


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


def t_IDENTIFIER(t):
    r'[A-Z][a-zA-Z0-9]*'  # PascalCase pattern
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check if it's a reserved word
    return t


# Error handling rule for identifiers not in PascalCase
def t_IDENTIFIER_error(t):
    r"""[a-z][a-zA-Z0-9]*(?=\s*[=+\-*/<>=]|$)"""  # Check for lowercase identifiers
    print(f"Error: Variable '{t.value}' should be in PascalCase format")
    t.lexer.skip(1)


def t_STRING(t):
    r"'[^']*'"
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
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
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


# Ensures that what comes before an equal sign must be in pascal case
def t_ASSIGN_ERROR(t):
    r'[a-zA-Z_0-9]+=|[=]+[a-zA-Z_0-9]+'
    print(f"Syntax error: Invalid assignment '{t.value}'")
    t.lexer.skip(1)
