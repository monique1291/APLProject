from ply.yacc import yacc

# Define global environment stack
env_stack = [{}]


# Define function for pushing a new environment onto the stack
def push_env():
    env_stack.append({})


# Define function for popping the top environment from the stack
def pop_env():
    if len(env_stack) > 1:
        return env_stack.pop()
    else:
        raise RuntimeError("Cannot pop global environment")


# Define function for accessing the current environment
def current_env():
    return env_stack[-1]


# Define function for updating the current environment
def update_env(variable_name, value):
    current_env()[variable_name] = value


# Define function for looking up a variable in the current environment
def lookup_env(variable_name):
    for env in reversed(env_stack):
        if variable_name in env:
            return env[variable_name]
    raise NameError(f"Variable '{variable_name}' not defined")


# Define precedence for operators
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'MINUS'),
)


def p_calc(p):
    '''
    calc : expression
         | var_assign
         | empty
    '''
    if len(p) > 1:
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
    if len(p) == 2:
        p[0] = p[1]  # If it's just an expression_var, pass it through
    elif p[1] == '(':
        p[0] = p[2]  # If it's inside parentheses, pass through the expression
    else:
        p[0] = (p[2], p[1], p[3])  # Store operator and operands


def p_var_assign(p):
    '''
    var_assign : IDENTIFIER EQUAL expression
               | IDENTIFIER EQUALEQUAL expression
               | IDENTIFIER PLUSEQUAL expression
               | IDENTIFIER MINUSEQUAL expression
               | IDENTIFIER TIMESEQUAL expression
               | IDENTIFIER DIVIDEEQUAL expression
    '''
    p[0] = (p[2], p[1], p[3])


# rule specifically for ints and floats - note this is just for a calculator
def p_expression_int_float(p):
    '''
    expression : INT
               | FLOAT
               | empty
    '''
    if len(p) == 2:  # Check if it's either INT or FLOAT
        p[0] = p[1]
    else:
        p[0] = None  # Handle the case when it's empty


# rule for variables
def p_expression_var(p):
    '''
    expression : IDENTIFIER
    '''
    p[0] = ('var', p[1])


# rule for empty input
def p_empty(p):
    '''
    empty :
    '''
    p[0] = ('None',)


# rule for errors in syntax
def p_error(p):
    raise SyntaxError(f"Syntax Error: Unexpected token '{p.value}'")


# Update run function to handle variable scope
def run(p):
    if isinstance(p, tuple):
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            divisor = run(p[2])
            if divisor == 0:
                raise ValueError("Division by zero")
            return run(p[1]) / divisor
        elif p[0] == '=':
            variable_name = p[1]
            value = run(p[2])
            update_env(variable_name, value)
            print(env_stack)  # Print environment stack
        elif p[0] == 'var':
            variable_name = p[1]
            return lookup_env(variable_name)
    else:
        return p


# Define parser object
parser = yacc()
