
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'statementsAND ARRAY BOOL BREAK CASE CLASS CLOSECLASS CLOSEFUNC COLON COMMA COMMENTS DEF DIVIDE DIVIDEEQUAL DO DOUBLEQUOTES ELIF ELSE ENDIF EQUAL EQUALEQUAL FALSE FINALLY FLOAT FLT FOR FUNC GLOBAL GREATEREQUAL GREATERTHAN IDENTIFIER IF IMPORT IN INT INTEGER IS LCURVEDBRACE LESSEQUAL LESSTHAN LPAREN LSQUAREDBRACKET MAIN MINUS MINUSEQUAL NOT NOTEQUAL OR PLUS PLUSEQUAL PRINT RANGE RCURVEDBRACE RETURN RPAREN RSQUAREDBRACKET RULE_CLOSE RULE_OPEN SINGLEQUOTES STR STRING SWITCH THEN TIMES TIMESEQUAL TRUE UNTIL VARIABLE WHILE\n    statements : statement statements\n               | statement\n               | empty\n    \n    statement : conditional\n              | expression\n              | assignment_statement\n              | function_call\n              | print_statement\n              | function_declaration\n              | variable_declaration\n              | array_declaration\n              | class_declaration\n              | main_function\n              | empty\n    \n    main_function : MAIN LPAREN RPAREN COLON statements\n    \n    conditional : inline_if_statement\n                | for_statement\n                | while_statement\n    \n    variable_declaration : type IDENTIFIER\n    \n    array_declaration : ARRAY type IDENTIFIER LSQUAREDBRACKET INTEGER RSQUAREDBRACKET\n    \n    function_declaration : FUNC type IDENTIFIER LPAREN argument_list RPAREN statements CLOSEFUNC\n    \n    class_declaration : CLASS IDENTIFIER COLON statements CLOSECLASS\n    inline_if_statement : IF LPAREN expression RPAREN COLON statements ENDIF\n                           | IF LPAREN expression RPAREN COLON statements ELSE COLON statements ENDIF\n                           \n    for_statement : FOR expression IN range_expression\n    \n    range_expression : RANGE expression COMMA expression\n    \n    while_statement : WHILE expression COLON statements\n    \n    bool : TRUE\n         | FALSE\n    \n    print_statement : PRINT LPAREN STRING RPAREN\n    \n    expression : expression GREATERTHAN expression\n               | expression LESSTHAN expression\n               | expression GREATEREQUAL expression\n               | expression LESSEQUAL expression\n               | expression EQUALEQUAL expression\n               | expression NOTEQUAL expression\n               | expression PLUS expression\n               | expression MINUS expression\n               | expression TIMES expression\n               | expression DIVIDE expression\n               | expression EQUAL expression\n               | token\n               | data\n    \n    data : INTEGER\n             | FLOAT\n             | STRING\n             | IDENTIFIER\n             | bool\n    \n    token : COLON\n          | EQUAL\n    assignment_statement : IDENTIFIER EQUAL expressionfunction_call : IDENTIFIER LPAREN argument_list RPARENargument_list : type IDENTIFIER COMMA argument_list\n                     | type IDENTIFIER\n                     | empty\n    type : INT\n         | FLT\n         | STR\n    \n    empty :\n    '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,33,34,38,39,40,56,62,64,65,66,67,68,69,70,71,72,73,74,75,86,87,89,93,95,97,101,102,107,111,113,114,117,],[-59,0,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,-1,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,-59,-52,-30,-59,-25,-27,-22,-15,-20,-23,-26,-21,-24,]),'IDENTIFIER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,26,27,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,60,62,64,65,66,67,68,69,70,71,72,73,74,75,77,82,86,87,89,93,95,96,97,101,102,103,106,107,109,111,113,114,115,117,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,56,-44,58,-49,62,62,-45,-48,-56,-57,-58,-28,-29,-1,62,62,62,62,62,62,62,62,62,62,62,62,80,-19,81,62,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,88,20,20,-52,-30,20,-25,62,-27,-22,-15,20,20,-20,62,-23,-26,-21,20,-24,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,33,34,38,39,40,56,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,93,95,97,101,102,103,106,107,111,113,114,115,117,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,-1,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,21,21,-52,-30,21,-25,-27,-22,-15,21,21,-20,-23,-26,-21,21,-24,]),'FUNC':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,33,34,38,39,40,56,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,93,95,97,101,102,103,106,107,111,113,114,115,117,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,-1,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,23,23,-52,-30,23,-25,-27,-22,-15,23,23,-20,-23,-26,-21,23,-24,]),'ARRAY':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,33,34,38,39,40,56,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,93,95,97,101,102,103,106,107,111,113,114,115,117,],[25,25,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,-1,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,25,25,-52,-30,25,-25,-27,-22,-15,25,25,-20,-23,-26,-21,25,-24,]),'CLASS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,33,34,38,39,40,56,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,93,95,97,101,102,103,106,107,111,113,114,115,117,],[27,27,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,-1,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,27,27,-52,-30,27,-25,-27,-22,-15,27,27,-20,-23,-26,-21,27,-24,]),'MAIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,33,34,38,39,40,56,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,93,95,97,101,102,103,106,107,111,113,114,115,117,],[29,29,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,-1,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,29,29,-52,-30,29,-25,-27,-22,-15,29,29,-20,-23,-26,-21,29,-24,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,33,34,38,39,40,56,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,93,95,97,101,102,103,106,107,111,113,114,115,117,],[30,30,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,-1,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,30,30,-52,-30,30,-25,-27,-22,-15,30,30,-20,-23,-26,-21,30,-24,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,33,34,38,39,40,56,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,93,95,97,101,102,103,106,107,111,113,114,115,117,],[31,31,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,-1,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,31,31,-52,-30,31,-25,-27,-22,-15,31,31,-20,-23,-26,-21,31,-24,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,33,34,38,39,40,56,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,93,95,97,101,102,103,106,107,111,113,114,115,117,],[32,32,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,-1,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,32,32,-52,-30,32,-25,-27,-22,-15,32,32,-20,-23,-26,-21,32,-24,]),'COLON':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,31,32,33,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,56,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,82,83,86,87,89,93,94,95,96,97,101,102,103,106,107,109,111,112,113,114,115,117,],[28,28,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,28,28,-45,-48,-28,-29,-1,28,28,28,28,28,28,28,28,28,28,28,28,-19,82,28,-47,86,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,28,93,28,-52,-30,28,103,-25,28,-27,-22,-15,28,28,-20,28,-23,115,-26,-21,28,-24,]),'EQUAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,31,32,33,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,56,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,82,84,86,87,89,93,95,96,97,101,102,103,104,106,107,109,111,113,114,115,117,],[17,17,-3,-4,51,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,52,-46,-44,-49,17,17,-45,-48,-28,-29,-1,17,17,17,17,17,17,17,17,17,17,17,17,-19,17,51,-47,51,51,51,51,51,51,51,51,51,51,51,51,51,17,51,17,-52,-30,17,-25,17,-27,-22,-15,17,51,17,-20,17,-23,51,-21,17,-24,]),'INTEGER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,31,32,33,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,56,60,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,91,93,95,96,97,101,102,103,106,107,109,111,113,114,115,117,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,26,26,-45,-48,-28,-29,-1,26,26,26,26,26,26,26,26,26,26,26,26,-19,26,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,26,26,-52,-30,100,26,-25,26,-27,-22,-15,26,26,-20,26,-23,-26,-21,26,-24,]),'FLOAT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,31,32,33,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,56,60,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,93,95,96,97,101,102,103,106,107,109,111,113,114,115,117,],[33,33,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,33,33,-45,-48,-28,-29,-1,33,33,33,33,33,33,33,33,33,33,33,33,-19,33,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,33,33,-52,-30,33,-25,33,-27,-22,-15,33,33,-20,33,-23,-26,-21,33,-24,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,31,32,33,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,54,56,60,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,93,95,96,97,101,102,103,106,107,109,111,113,114,115,117,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,22,22,-45,-48,-28,-29,-1,22,22,22,22,22,22,22,22,22,22,22,22,79,-19,22,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,22,22,-52,-30,22,-25,22,-27,-22,-15,22,22,-20,22,-23,-26,-21,22,-24,]),'INT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,25,26,28,33,34,38,39,40,53,56,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,90,93,95,97,98,101,102,103,106,107,111,113,114,115,117,],[35,35,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,35,35,-44,-49,-45,-48,-28,-29,-1,35,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,35,35,-52,-30,35,35,-25,-27,35,-22,-15,35,35,-20,-23,-26,-21,35,-24,]),'FLT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,25,26,28,33,34,38,39,40,53,56,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,90,93,95,97,98,101,102,103,106,107,111,113,114,115,117,],[36,36,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,36,36,-44,-49,-45,-48,-28,-29,-1,36,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,36,36,-52,-30,36,36,-25,-27,36,-22,-15,36,36,-20,-23,-26,-21,36,-24,]),'STR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,25,26,28,33,34,38,39,40,53,56,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,90,93,95,97,98,101,102,103,106,107,111,113,114,115,117,],[37,37,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,37,37,-44,-49,-45,-48,-28,-29,-1,37,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,37,37,-52,-30,37,37,-25,-27,37,-22,-15,37,37,-20,-23,-26,-21,37,-24,]),'TRUE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,31,32,33,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,56,60,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,93,95,96,97,101,102,103,106,107,109,111,113,114,115,117,],[38,38,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,38,38,-45,-48,-28,-29,-1,38,38,38,38,38,38,38,38,38,38,38,38,-19,38,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,38,38,-52,-30,38,-25,38,-27,-22,-15,38,38,-20,38,-23,-26,-21,38,-24,]),'FALSE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,31,32,33,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,56,60,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,93,95,96,97,101,102,103,106,107,109,111,113,114,115,117,],[39,39,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,39,39,-45,-48,-28,-29,-1,39,39,39,39,39,39,39,39,39,39,39,39,-19,39,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,39,39,-52,-30,39,-25,39,-27,-22,-15,39,39,-20,39,-23,-26,-21,39,-24,]),'CLOSECLASS':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,33,34,38,39,40,56,62,64,65,66,67,68,69,70,71,72,73,74,75,82,86,87,89,92,93,95,97,101,102,107,111,113,114,117,],[-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,-1,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,-59,-59,-52,-30,101,-59,-25,-27,-22,-15,-20,-23,-26,-21,-24,]),'ENDIF':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,33,34,38,39,40,56,62,64,65,66,67,68,69,70,71,72,73,74,75,86,87,89,93,95,97,101,102,103,107,108,111,113,114,115,116,117,],[-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,-1,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,-59,-52,-30,-59,-25,-27,-22,-15,-59,-20,111,-23,-26,-21,-59,117,-24,]),'ELSE':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,33,34,38,39,40,56,62,64,65,66,67,68,69,70,71,72,73,74,75,86,87,89,93,95,97,101,102,103,107,108,111,113,114,117,],[-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,-1,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,-59,-52,-30,-59,-25,-27,-22,-15,-59,-20,112,-23,-26,-21,-24,]),'CLOSEFUNC':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,26,28,33,34,38,39,40,56,62,64,65,66,67,68,69,70,71,72,73,74,75,86,87,89,93,95,97,101,102,106,107,110,111,113,114,117,],[-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-17,-18,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,-1,-19,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-51,-59,-52,-30,-59,-25,-27,-22,-15,-59,-20,114,-23,-26,-21,-24,]),'GREATERTHAN':([5,17,18,19,20,22,26,28,33,34,38,39,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,84,104,113,],[41,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,41,-47,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'LESSTHAN':([5,17,18,19,20,22,26,28,33,34,38,39,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,84,104,113,],[42,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,42,-47,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'GREATEREQUAL':([5,17,18,19,20,22,26,28,33,34,38,39,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,84,104,113,],[43,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,43,-47,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'LESSEQUAL':([5,17,18,19,20,22,26,28,33,34,38,39,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,84,104,113,],[44,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,44,-47,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'EQUALEQUAL':([5,17,18,19,20,22,26,28,33,34,38,39,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,84,104,113,],[45,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,45,-47,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'NOTEQUAL':([5,17,18,19,20,22,26,28,33,34,38,39,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,84,104,113,],[46,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,46,-47,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'PLUS':([5,17,18,19,20,22,26,28,33,34,38,39,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,84,104,113,],[47,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,47,-47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'MINUS':([5,17,18,19,20,22,26,28,33,34,38,39,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,84,104,113,],[48,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,48,-47,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'TIMES':([5,17,18,19,20,22,26,28,33,34,38,39,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,84,104,113,],[49,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,49,-47,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'DIVIDE':([5,17,18,19,20,22,26,28,33,34,38,39,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,84,104,113,],[50,-50,-42,-43,-47,-46,-44,-49,-45,-48,-28,-29,50,-47,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'IN':([17,18,19,22,26,28,33,34,38,39,61,62,64,65,66,67,68,69,70,71,72,73,74,],[-50,-42,-43,-46,-44,-49,-45,-48,-28,-29,85,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,]),'RPAREN':([17,18,19,22,26,28,33,34,38,39,53,59,62,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,88,90,98,99,105,],[-50,-42,-43,-46,-44,-49,-45,-48,-28,-29,-59,83,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,87,-55,89,94,-54,-59,-59,106,-53,]),'COMMA':([17,18,19,22,26,28,33,34,38,39,62,64,65,66,67,68,69,70,71,72,73,74,88,104,],[-50,-42,-43,-46,-44,-49,-45,-48,-28,-29,-47,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,98,109,]),'LPAREN':([20,21,29,30,80,],[53,54,59,60,90,]),'LSQUAREDBRACKET':([81,],[91,]),'RANGE':([85,],[96,]),'RSQUAREDBRACKET':([100,],[107,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,2,82,86,93,103,106,115,],[1,40,92,97,102,108,110,116,]),'statement':([0,2,82,86,93,103,106,115,],[2,2,2,2,2,2,2,2,]),'empty':([0,2,53,82,86,90,93,98,103,106,115,],[3,3,78,3,3,78,3,78,3,3,3,]),'conditional':([0,2,82,86,93,103,106,115,],[4,4,4,4,4,4,4,4,]),'expression':([0,2,31,32,41,42,43,44,45,46,47,48,49,50,51,52,60,82,86,93,96,103,106,109,115,],[5,5,61,63,64,65,66,67,68,69,70,71,72,73,74,75,84,5,5,5,104,5,5,113,5,]),'assignment_statement':([0,2,82,86,93,103,106,115,],[6,6,6,6,6,6,6,6,]),'function_call':([0,2,82,86,93,103,106,115,],[7,7,7,7,7,7,7,7,]),'print_statement':([0,2,82,86,93,103,106,115,],[8,8,8,8,8,8,8,8,]),'function_declaration':([0,2,82,86,93,103,106,115,],[9,9,9,9,9,9,9,9,]),'variable_declaration':([0,2,82,86,93,103,106,115,],[10,10,10,10,10,10,10,10,]),'array_declaration':([0,2,82,86,93,103,106,115,],[11,11,11,11,11,11,11,11,]),'class_declaration':([0,2,82,86,93,103,106,115,],[12,12,12,12,12,12,12,12,]),'main_function':([0,2,82,86,93,103,106,115,],[13,13,13,13,13,13,13,13,]),'inline_if_statement':([0,2,82,86,93,103,106,115,],[14,14,14,14,14,14,14,14,]),'for_statement':([0,2,82,86,93,103,106,115,],[15,15,15,15,15,15,15,15,]),'while_statement':([0,2,82,86,93,103,106,115,],[16,16,16,16,16,16,16,16,]),'token':([0,2,31,32,41,42,43,44,45,46,47,48,49,50,51,52,60,82,86,93,96,103,106,109,115,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'data':([0,2,31,32,41,42,43,44,45,46,47,48,49,50,51,52,60,82,86,93,96,103,106,109,115,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'type':([0,2,23,25,53,82,86,90,93,98,103,106,115,],[24,24,55,57,77,24,24,77,24,77,24,24,24,]),'bool':([0,2,31,32,41,42,43,44,45,46,47,48,49,50,51,52,60,82,86,93,96,103,106,109,115,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'argument_list':([53,90,98,],[76,99,105,]),'range_expression':([85,],[95,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statement statements','statements',2,'p_statements','newParser.py',12),
  ('statements -> statement','statements',1,'p_statements','newParser.py',13),
  ('statements -> empty','statements',1,'p_statements','newParser.py',14),
  ('statement -> conditional','statement',1,'p_statement','newParser.py',26),
  ('statement -> expression','statement',1,'p_statement','newParser.py',27),
  ('statement -> assignment_statement','statement',1,'p_statement','newParser.py',28),
  ('statement -> function_call','statement',1,'p_statement','newParser.py',29),
  ('statement -> print_statement','statement',1,'p_statement','newParser.py',30),
  ('statement -> function_declaration','statement',1,'p_statement','newParser.py',31),
  ('statement -> variable_declaration','statement',1,'p_statement','newParser.py',32),
  ('statement -> array_declaration','statement',1,'p_statement','newParser.py',33),
  ('statement -> class_declaration','statement',1,'p_statement','newParser.py',34),
  ('statement -> main_function','statement',1,'p_statement','newParser.py',35),
  ('statement -> empty','statement',1,'p_statement','newParser.py',36),
  ('main_function -> MAIN LPAREN RPAREN COLON statements','main_function',5,'p_main_function','newParser.py',43),
  ('conditional -> inline_if_statement','conditional',1,'p_conditional','newParser.py',50),
  ('conditional -> for_statement','conditional',1,'p_conditional','newParser.py',51),
  ('conditional -> while_statement','conditional',1,'p_conditional','newParser.py',52),
  ('variable_declaration -> type IDENTIFIER','variable_declaration',2,'p_variable_declaration','newParser.py',60),
  ('array_declaration -> ARRAY type IDENTIFIER LSQUAREDBRACKET INTEGER RSQUAREDBRACKET','array_declaration',6,'p_array_declaration','newParser.py',68),
  ('function_declaration -> FUNC type IDENTIFIER LPAREN argument_list RPAREN statements CLOSEFUNC','function_declaration',8,'p_function_declaration','newParser.py',76),
  ('class_declaration -> CLASS IDENTIFIER COLON statements CLOSECLASS','class_declaration',5,'p_class_declaration','newParser.py',84),
  ('inline_if_statement -> IF LPAREN expression RPAREN COLON statements ENDIF','inline_if_statement',7,'p_inline_if_statement','newParser.py',91),
  ('inline_if_statement -> IF LPAREN expression RPAREN COLON statements ELSE COLON statements ENDIF','inline_if_statement',10,'p_inline_if_statement','newParser.py',92),
  ('for_statement -> FOR expression IN range_expression','for_statement',4,'p_for_statement','newParser.py',102),
  ('range_expression -> RANGE expression COMMA expression','range_expression',4,'p_range_expression','newParser.py',109),
  ('while_statement -> WHILE expression COLON statements','while_statement',4,'p_while_statement','newParser.py',116),
  ('bool -> TRUE','bool',1,'p_bool','newParser.py',123),
  ('bool -> FALSE','bool',1,'p_bool','newParser.py',124),
  ('print_statement -> PRINT LPAREN STRING RPAREN','print_statement',4,'p_print_statement','newParser.py',131),
  ('expression -> expression GREATERTHAN expression','expression',3,'p_expression','newParser.py',138),
  ('expression -> expression LESSTHAN expression','expression',3,'p_expression','newParser.py',139),
  ('expression -> expression GREATEREQUAL expression','expression',3,'p_expression','newParser.py',140),
  ('expression -> expression LESSEQUAL expression','expression',3,'p_expression','newParser.py',141),
  ('expression -> expression EQUALEQUAL expression','expression',3,'p_expression','newParser.py',142),
  ('expression -> expression NOTEQUAL expression','expression',3,'p_expression','newParser.py',143),
  ('expression -> expression PLUS expression','expression',3,'p_expression','newParser.py',144),
  ('expression -> expression MINUS expression','expression',3,'p_expression','newParser.py',145),
  ('expression -> expression TIMES expression','expression',3,'p_expression','newParser.py',146),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','newParser.py',147),
  ('expression -> expression EQUAL expression','expression',3,'p_expression','newParser.py',148),
  ('expression -> token','expression',1,'p_expression','newParser.py',149),
  ('expression -> data','expression',1,'p_expression','newParser.py',150),
  ('data -> INTEGER','data',1,'p_data','newParser.py',173),
  ('data -> FLOAT','data',1,'p_data','newParser.py',174),
  ('data -> STRING','data',1,'p_data','newParser.py',175),
  ('data -> IDENTIFIER','data',1,'p_data','newParser.py',176),
  ('data -> bool','data',1,'p_data','newParser.py',177),
  ('token -> COLON','token',1,'p_tokens','newParser.py',184),
  ('token -> EQUAL','token',1,'p_tokens','newParser.py',185),
  ('assignment_statement -> IDENTIFIER EQUAL expression','assignment_statement',3,'p_assignment_statement','newParser.py',191),
  ('function_call -> IDENTIFIER LPAREN argument_list RPAREN','function_call',4,'p_function_call','newParser.py',196),
  ('argument_list -> type IDENTIFIER COMMA argument_list','argument_list',4,'p_argument_list','newParser.py',201),
  ('argument_list -> type IDENTIFIER','argument_list',2,'p_argument_list','newParser.py',202),
  ('argument_list -> empty','argument_list',1,'p_argument_list','newParser.py',203),
  ('type -> INT','type',1,'p_type','newParser.py',214),
  ('type -> FLT','type',1,'p_type','newParser.py',215),
  ('type -> STR','type',1,'p_type','newParser.py',216),
  ('empty -> <empty>','empty',0,'p_empty','newParser.py',223),
]
