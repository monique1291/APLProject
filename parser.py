from ply.yacc import yacc
from tokens import tokens


def p_calc(p):
    '''
    calc : expression
         | var_assign
         | empty
    '''
    print(run(p[1]))


# rule for various types of expressions
def p_expression(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression MULTIPLY expression
               | expression DIVIDE expression
               | LPAREN expression RPAREN
               | expression_var
    '''
    p[0] = (p[2], p[1], p[3])

def p_var_assign(p):
    '''
    expression :
    '''
# rule specifically for ints and floats - note this is just for a calculator
def p_expression_int_float(p):
    '''
    expression : INT
               | FLOAT
               |empty
    '''
    p[0] = p[1]


# this is new
# rule for variables
def p_expression_var(p):
    '''
    expression : IDENTIFIER
    '''
    p[0] = ('var', p[1])


# rule for errors in syntax
def p_error(p):
    raise SyntaxError(f"Syntax Error: Unexpected token '{p.value}'")


# rule for empty input
def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


# method call to build parser
parser = yacc()
env = {}  # this is to store the variables


def run(p):
    global env
    if type(p) == tuple:  # all parameters passed are tuples which can be one of those shown below
        if p[0] == '+':
            return run(p[1]) + run(p[2])  # if its +. add the parameters etc
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == '=':
            env[p[1]] = run(p[2])
            print(env)
        elif p[0] == 'var':  # if a variable is passed, check global var array for name and value
            if p[1] not in env:
                return 'Undeclared variable found!'
            else:
                return env[p[1]]
    else:
        return p


while True:
    try:
        # accept input to tokenize and perform semantic analysis
        s = input(">")
    except EOFError:
        break
    parser.parse(s)
