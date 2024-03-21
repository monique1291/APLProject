from ply.yacc import yacc
from newLexer import tokens

# to do:


'''
variable declarations
variable assignments
program/ new file creation
conditionals -> while, for , until etc
print statement
'''


# Define the grammar rules
def p_newCode(p):
    """
    newCode : statements
    """


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


#              | declaration
#      | assignment
def p_statement(p):
    """
    statement : conditional

              | print_statement
              | empty
    """
    p[0] = p[1]


# | block_if_statement
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
    # Execute code based on the condition and presence of ELSE
    if len(p) == 5:
        p[0] = ('inline_if_statement', p[2], p[4])
    elif len(p) == 7:
        p[0] = ('inline_if_statement', p[2], p[4], p[6])


# REVISIT STRUCTURE BELOW
'''
def p_block_if_statement(p):
    """block_if_statement : RULE_OPEN IF expression RULE_CLOSE statements RULE_OPEN END RULE_CLOSE
                          | RULE_OPEN IF expression RULE_CLOSE statements block_else_statement"""
    if len(p) == 9:
        p[0] = ('block_if_statement', p[3], p[5])
    elif len(p) == 7:
        p[0] = ('block_if_statement', p[3], p[5], p[6])

'''


def p_for_statement(p):
    """
    for_statement : FOR expression IN range_expression
    """
    p[0] = ('for_statement', p[2], p(4))


def p_range_expression(p):
    """
    range_expression : RULE_OPEN RANGE NUMBER COMMA NUMBER RULE_CLOSE
    """
    start = int(p[3])
    end = int(p[5])
    p[0] = list(range(start, end))  # may need to change to number so rule can be accessed


def p_while_statement(p):
    """
    while_statement : WHILE expression COLON statements
    """
    p[0] = ('while_statement', p[2], p[3])


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
               | IDENTIFIER
               | bool

    """
    if len(p) == 4:
        p[0] = ('expression', p[1], p[2], p[3])
    if len(p) == 1:
        p[0] = ('expression', p[1])


def p_empty(p):
    """
    empty :
    """
    p[0] = None


def p_error(p):
    raise SyntaxError(f"Syntax Error: Unexpected token '{p.value}'")


parser = yacc()
'''
def p_statements(p):
    """statements : statement
                  | statements statement"""
    # Handle statements here (e.g., execute code, print output, etc.)


def p_statement(p):
    """statement : code
                 | rule"""


def p_code(p):
    """code : CODE_BLOCK"""


def p_rule(p):
    """rule : inline_if_statement
            | block_if_statement
            | nested_else_if_statement"""


def p_block_if_statement(p):
    """block_if_statement : RULE_OPEN IF expression RULE_CLOSE statements RULE_OPEN END RULE_CLOSE
                          | RULE_OPEN IF expression RULE_CLOSE statements block_else_statement"""

def p_expression(p):
    """expression : IDENTIFIER
                  | statement"""
def p_block_else_statement(p):
    """block_else_statement : RULE_OPEN ELSE RULE_CLOSE statements RULE_OPEN END RULE_CLOSE
                            | empty"""


def p_nested_else_if_statement(p):
    """
    nested_else_if_statement : RULE_OPEN IF CONDITION RULE_CLOSE statements else_if_blocks RULE_OPEN ELSE RULE_CLOSE statements RULE_OPEN END RULE_CLOSE
   """


def p_else_if_blocks(p):
    """
    else_if_blocks : else_if_block
                   | else_if_blocks else_if_block
    """


def p_else_if_block(p):
    """else_if_block : RULE_OPEN ELSE_IF CONDITION RULE_CLOSE statements"""
    if len(p) == 6:
        # Handle the ELSE_IF block
        condition = p[3]
        statements = p[5]
        # Your logic for the ELSE_IF condition goes here
        # ...
    else:
        # Handle the empty case
        pass

def p_empty(p):
    """empty :"""
    pass


# Example action for handling IF-ELSE statements
def p_inline_if_statement(p):
    """inline_if_statement : IF CONDITION
                           | IF CONDITION ELSE
                           | IF CONDITION ELSE statements"""
    # Execute code based on the condition and presence of ELSE


def p_error(p):
    raise SyntaxError(f"Syntax Error: Unexpected token '{p.value}'")


# Build the parser
parser = yacc.yacc()

# Example input
input_code = """
if some_condition
    {# Code to execute if the condition is true}
else
    {# Code to execute if the condition is false}
END

"""

# Parse the input
result = parser.parse(input_code)
print(result)'''
