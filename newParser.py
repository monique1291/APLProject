import ply.yacc as yacc
from ply.lex import lex
from tokens import *

# Define the start symbol of your grammar
start = 'statements'


# Define the grammar rules
def p_statements(p):
    """
    statements : statement statements
               | statement
               | empty
    """
    if len(p) == 3:
        p[0] = ('statements', p[1], p[2])
    elif len(p) == 2:
        p[0] = ('statements', p[1])
    else:
        p[0] = ('statements',)


def p_statement(p):
    """
    statement : conditional
              | expression
              | assignment_statement
              | function_call
              | print_statement
              | empty
    """
    p[0] = p[1]


def p_conditional(p):
    """
    conditional : inline_if_statement
                | for_statement
                | while_statement
    """
    p[0] = ('conditional', p[1])


def p_inline_if_statement(p):
    """inline_if_statement : IF expression COLON statements
                           | IF expression COLON statements ELSE statements"""
    if len(p) == 5:
        p[0] = ('inline_if_statement', p[2], p[4])
    elif len(p) == 7:
        p[0] = ('inline_if_statement', p[2], p[4], p[6])


def p_for_statement(p):
    """
    for_statement : FOR expression IN range_expression
    """
    p[0] = ('for_statement', p[2], p[4])


def p_range_expression(p):
    """
    range_expression : RANGE expression COMMA expression
    """
    p[0] = ('range_expression', p[2], p[4])


def p_while_statement(p):
    """
    while_statement : WHILE expression COLON statements
    """
    p[0] = ('while_statement', p[2], p[4])


def p_bool(p):
    """
    bool : TRUE
         | FALSE
    """
    p[0] = ('bool', p[1])


def p_print_statement(p):
    """
    print_statement : PRINT LPAREN expression RPAREN
    """
    p[0] = ('print_statement', p[3])


def p_expression(p):
    """
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression EQUALTO expression
               | LPAREN expression RPAREN
               | INTEGER
               | FLOAT
               | STRING
               | IDENTIFIER
               | bool
    """
    if len(p) == 4:
        p[0] = ('expression', p[2], p[1], p[3])
    elif len(p) == 2:
        p[0] = ('expression', p[1])
    else:
        p[0] = ('expression', p[1], p[2], p[3])


def p_assignment_statement(p):
    """assignment_statement : IDENTIFIER EQUAL expression"""
    p[0] = ('assignment_statement', p[1], p[3])


def p_function_call(p):
    """function_call : IDENTIFIER LPAREN argument_list RPAREN"""
    p[0] = ('function_call', p[1], p[3])


def p_argument_list(p):
    """argument_list : expression
                     | argument_list COMMA expression"""
    if len(p) == 2:
        p[0] = ('argument_list', p[1])
    else:
        p[0] = ('argument_list', p[1], p[3])


def p_empty(p):
    """
    empty :
    """
    pass


def p_error(p):
    raise SyntaxError(f"Syntax Error: Unexpected token '{p.value}'")


parser = yacc.yacc()