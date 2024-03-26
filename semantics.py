def get_value_type(value):
    if isinstance(value, int):
        return 'int'
    elif isinstance(value, str):
        return 'str'
    elif isinstance(value, float):
        return 'float'
    # elif isinstance(value, bool): #do we need boolean?
    #    return 'bool'
    else:
        return None


def visit_print_statement(text):
    print(text)
    pass


class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, ast):
        self.visit(ast)

    def visit(self, node):
        method_name = 'visit_' + node[0]
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            return method(*node[1:])
        else:
            raise NotImplementedError(f"Method {method_name} not implemented")

    def visit_statements(self, *statements):
        for statement in statements:
            self.visit(statement)

    def visit_assignment_statement(self, identifier, *expressions):
        if len(expressions) == 1:
            # Regular assignment
            value = expressions[0]
            # Perform semantic analysis for regular assignment
        elif len(expressions) == 3:
            # Array assignment
            index = expressions[0]
            value = expressions[1]
            # Perform semantic analysis for array assignment

    def visit_variable_declaration(self, datatype, identifier):
        var_name = identifier
        if var_name in self.symbol_table:
            raise NameError(f"Variable '{var_name}' is already defined")
        self.symbol_table[var_name] = datatype

    def visit_function_declaration(self, datatype, identifier, argument_list, statements):
        func_name = identifier
        if func_name in self.symbol_table:
            raise NameError(f"Function '{func_name}' is already defined")
        self.symbol_table[func_name] = datatype
        self.visit(statements)

    def visit_class_declaration(self, identifier, statements):
        class_name = identifier
        if class_name in self.symbol_table:
            raise NameError(f"Class '{class_name}' is already defined")
        self.symbol_table[class_name] = 'CLASS'

    def visit_main_function(self, statements):
        self.visit(statements)

    # Define visit_conditional method
        # Define visit_conditional method
    def visit_conditional(self, if_statement, else_statement=None):
        # Extract the condition expression and true/false statements from the AST node
        condition_expr = if_statement[0]
        true_statements = if_statement[1]
        false_statements = else_statement[0] if else_statement else None

        # Analyze the condition expression
        self.visit(condition_expr)

        # Analyze the true statements
        self.visit(true_statements)

        # Analyze the false statements if present
        if false_statements:
            self.visit(false_statements)

    def visit_expression(self, left_operand, operator, right_operand):
        # Perform semantic analysis on the expression
        left_type = self.visit(left_operand)
        right_type = self.visit(right_operand)

        # Add your semantic analysis logic here
        # For simplicity, let's assume the operands are of the same type
        if left_type != right_type:
            raise TypeError("Type mismatch in expression")

        # Return the type of the expression
        return left_type

    def visit_function_call(self, *args):
        # Handling function calls
        pass

    def visit_range_expression(self, *args):
        # Handling range expressions
        pass

    def visit_while_statement(self, *args):
        # Handling while statements
        pass

    def visit_for_statement(self, *args):
        # Handling for statements
        pass

    def visit_inline_if_statement(self, condition_expr, true_statements, false_statements=None):
        # Analyze the condition expression
        self.visit(condition_expr)

        # Analyze the true statements
        self.visit(true_statements)

        # Analyze the false statements if present
        if false_statements:
            self.visit(false_statements)

    def visit_array_declaration(self, datatype, identifier, size):
        # Check for duplicate declarations
        if identifier in self.symbol_table:
            raise NameError(f"Variable '{identifier}' is already defined")

        # Check if the datatype is one of the supported types
        supported_types = ['int', 'float', 'str', 'bool']
        if datatype not in supported_types:
            raise ValueError(f"Unsupported data type: {datatype}")

        # Perform semantic analysis for the size of the array
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Array size must be a positive integer")

        # Store the array declaration information in the symbol table
        self.symbol_table[identifier] = f'{datatype}[]'

    def visit_bool(self, *args):
        # Handling boolean values
        pass

    def visit_type(self, type_name):
        # Check if the type name is one of the supported types
        supported_types = ['int', 'float', 'str', 'bool']
        if type_name not in supported_types:
            raise ValueError(f"Unsupported data type: {type_name}")

        # Return the type name if it is supported
        return type_name

    # Define visit_empty method
    def visit_empty(self):
        # This method does nothing since the empty production doesn't produce any meaningful AST node
        pass
