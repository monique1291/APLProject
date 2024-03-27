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
              | array_assignment_statement
              | assignment_statement
              | function_call
              | print_statement
              | function_declaration
              | array_declaration
              | variable_declaration
              | class_declaration
              | main_function
              | empty
    """
    p[0] = p[1]


def p_main_function(p):
    """
    main_function : MAIN LPAREN RPAREN COLON statements
    """
    p[0] = ('main_function', p[5])


def p_conditional(p):
    """
    conditional : inline_if_statement
                | for_statement
                | while_statement
    """
    p[0] = ('conditional', p[1])


# declaring a variable
def p_variable_declaration(p):
    """
    variable_declaration : type IDENTIFIER
    """
    if len(p) == 3:
        p[0] = ('variable_declaration', p[1], p[2])


def p_array_declaration(p):
    """
    array_declaration : ARRAY type IDENTIFIER LSQUAREDBRACKET INTEGER RSQUAREDBRACKET
                      | ARRAY type IDENTIFIER LSQUAREDBRACKET INTEGER RSQUAREDBRACKET EQUAL LSQUAREDBRACKET array_values RSQUAREDBRACKET
    """
    if len(p) == 7:
        p[0] = ('array_declaration', p[2], p[3], p[5])
    if len(p) == 11:
        p[0] = ('array_declaration', p[2], p[3], p[5], p[9])


def p_function_declaration(p):
    """
    function_declaration : FUNC type IDENTIFIER LPAREN argument_list RPAREN COLON statements CLOSEFUNC
    """
    if len(p) == 10:
        p[0] = ('function_declaration', p[2], p[3], p[5], p[8])


def p_class_declaration(p):
    """
    class_declaration : CLASS IDENTIFIER COLON statements CLOSECLASS
    """
    if len(p) == 6:
        p[0] = ('class_declaration', p[2], p[4])


def p_inline_if_statement(p):
    """inline_if_statement : IF expression COLON statements ENDIF
                           | IF expression COLON statements ELSE COLON statements ENDIF
                           """
    if len(p) == 6:
        p[0] = ('inline_if_statement', p[2], p[4])
    elif len(p) == 9:
        p[0] = ('inline_if_statement', p[2], p[4], p[7])


def p_for_statement(p):
    """
    for_statement : FOR expression IN range_expression COLON statements ENDFOR
    """
    p[0] = ('for_statement', p[2], p[4])


def p_range_expression(p):
    """
    range_expression : RANGE INTEGER COMMA INTEGER
    """
    p[0] = ('range_expression', p[2], p[4])


def p_while_statement(p):
    """
    while_statement : WHILE expression COLON statements ENDWHILE
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
    print_statement : PRINT LPAREN STRING RPAREN
    """
    p[0] = ('print_statement', p[3])


def p_expression(p):
    """
    expression : expression GREATERTHAN expression
               | expression LESSTHAN expression
               | expression GREATEREQUAL expression
               | expression LESSEQUAL expression
               | expression EQUAL expression
               | expression EQUALEQUAL expression
               | expression NOTEQUAL expression
               | expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | token
               | data
    """
    if len(p) == 4:
        p[0] = ('expression', p[1], p[2], p[3])
    else:
        p[0] = p[1]


#  if len(p) == 4:
#     if p[1] == '(':
#        p[0] = p[2]  # If the expression is wrapped in parentheses, return the expression without parentheses
#    elif p[2] == '=':
#        p[0] = ('assignment', p[1], p[3])
#    else:
#        p[0] = ('binary_operation', p[2], p[1], p[3])
# elif len(p) == 2:
#    p[0] = p[1]
# else:
#    p[0] = p[2]  # For parentheses case


def p_data(p):
    """
    data : INTEGER
             | FLOAT
             | STRING
             | IDENTIFIER
             | bool
    """
    p[0] = p[1]


def p_tokens(p):
    """
    token : COLON
          | EQUAL
    """
    p[0] = ('token', p[1])


def p_array_values(p):
    """array_values : data
                    | COMMA data"""
    if len(p) == 3:
        p[0] = ('array_values', p[2])
    elif len(p) == 2:
        p[0] = ('array_values', p[1])


def p_assignment_statement(p):
    """assignment_statement : IDENTIFIER EQUAL expression"""
    p[0] = ('assignment_statement', p[1], p[3])


def p_array_assignment_statement(p):
    """array_assignment_statement : IDENTIFIER LSQUAREDBRACKET INTEGER RSQUAREDBRACKET EQUAL LSQUAREDBRACKET array_values RSQUAREDBRACKET"""
    p[0] = ('array_assignment_statement', p[1], p[3], p[7])


def p_function_call(p):
    """function_call : IDENTIFIER LPAREN argument_list RPAREN"""
    p[0] = ('function_call', p[1], p[3])


def p_argument_list(p):
    """argument_list : type IDENTIFIER COMMA argument_list
                     | type IDENTIFIER
                     | empty"""
    if len(p) == 5:
        p[0] = ('argument_list', p[1], p[2], p[4])
    elif len(p) == 3:
        p[0] = ('argument_list', p[1], p[2])
    else:
        p[0] = ('argument_list', p[1])


def p_type(p):
    """
    type : INT
         | FLT
         | STR
    """
    p[0] = p[1]


def p_empty(p):
    """
    empty :
    """
    pass


def p_error(p):
    if p:
        raise SyntaxError(f"Syntax Error: Unexpected token '{p.value}' at line {p.lineno}")
    else:
        raise SyntaxError("Syntax Error: Unexpected end of file")


parser = yacc.yacc()
