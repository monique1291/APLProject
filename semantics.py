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
        pass

    def visit_expression(self, left_operand, operator, right_operand):
        left_type = self.visit(left_operand)
        right_type = self.visit(right_operand)
        if left_type != right_type:
            raise TypeError("Type mismatch in expression")
        return left_type

    def visit_function_call(self, function_name, argument_list):
        # Check if the function is defined in the symbol table
        if function_name not in self.symbol_table:
            raise NameError(f"Function '{function_name}' is not defined")

        # Get the expected argument types and return type from the symbol table
        expected_arg_types, return_type = self.symbol_table[function_name]

        # Get the actual argument types from the argument list
        actual_arg_types = [self.visit(arg) for arg in argument_list]

        # Check if the number of arguments matches the expected number
        if len(expected_arg_types) != len(actual_arg_types):
            raise TypeError(f"Function '{function_name}' expects {len(expected_arg_types)} arguments, "
                            f"but {len(actual_arg_types)} were provided")

        # Check if the types of arguments match the expected types
        for expected_type, actual_type in zip(expected_arg_types, actual_arg_types):
            if expected_type != actual_type:
                raise TypeError(f"Type mismatch in function call '{function_name}': "
                                f"expected {expected_type}, got {actual_type}")

    def visit_range_expression(self, *args):
        pass

    def visit_while_statement(self, *args):
        pass

    def visit_for_statement(self, *args):
        pass

    def visit_inline_if_statement(self, *args):
        pass

    def visit_array_declaration(self, *args):
        pass

    def visit_bool(self, *args):
        pass

    def visit_type(self, *args):
        pass

    @staticmethod
    def get_value_type(value):
        if isinstance(value, int):
            return 'int'
        elif isinstance(value, str):
            return 'str'
        elif isinstance(value, float):
            return 'float'
        else:
            return None

    @staticmethod
    def visit_print_statement(text):
        print(text)

    def visit_empty(self):
        pass
