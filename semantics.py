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

    def visit_assignment_statement(self, identifier, value):
        var_name = identifier
        if var_name not in self.symbol_table:
            raise NameError(f"Variable '{var_name}' is not defined")
        expected_type = self.symbol_table[var_name]
        actual_type = self.get_value_type(value)
        if actual_type != expected_type:
            raise TypeError(f"Type mismatch: Variable '{var_name}' expected {expected_type}, got {actual_type}")

    def visit_variable_declaration(self, datatype, identifier):
        var_name = identifier
        if var_name in self.symbol_table:
            raise NameError(f"Variable '{var_name}' is already defined")
        self.symbol_table[var_name] = datatype

    def get_value_type(self, value):
        if isinstance(value, int):
            return 'int'
        elif isinstance(value, str):
            return 'str'
        elif isinstance(value, float):
            return 'float'
        #elif isinstance(value, bool): #do we neeed boolean?
        #    return 'bool'
        else:
            return None

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

    def visit_conditional(self, *args):
        # Handling conditionals is not explicitly specified in the example. You can add the logic here if needed.
        pass

    def visit_expression(self, *args):
        # Handling expressions
        pass

    def visit_function_call(self, *args):
        # Handling function calls
        pass

    def visit_print_statement(self, *args):
        # Handling print statements
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

    def visit_inline_if_statement(self, *args):
        # Handling inline if statements
        pass

    def visit_array_declaration(self, *args):
        # Handling array declarations
        pass

    def visit_bool(self, *args):
        # Handling boolean values
        pass

    def visit_type(self, *args):
        # Handling types
        pass

    # Define visit_empty method
    def visit_empty(self):
        # This method does nothing since the empty production doesn't produce any meaningful AST node
        pass
