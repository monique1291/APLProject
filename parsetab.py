
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'newCodeAND BREAK Bool CASE CLASS COLON COMMA COMMENTS DEF DIVIDE DIVIDEEQUAL DO DOUBLEQUOTES Double ELIF ELSE EQUAL EQUALEQUAL FALSE FINALLY FLOAT FOR FUNC Float GLOBAL GREATEREQUAL GREATERTHAN IDENTIFIER IF IMPORT IN INT INTEGER IS LCURVEDBRACE LESSEQUAL LESSTHAN LPAREN LSQUAREDBRACKET MAIN MINUS MINUSEQUAL NOT NOTEQUAL OR PLUS PLUSEQUAL PRINT RANGE RCURVEDBRACE RESERVEDWORD RETURN RPAREN RSQUAREDBRACKET RULE_CLOSE RULE_OPEN SINGLEQUOTES STRING SWITCH Str THEN TIMES TIMESEQUAL TRUE UNTIL WHILE\n    newCode : statements\n    \n    statements : statement statements\n               | statement\n               | empty\n    \n    statement : conditional\n              | expression\n              | assignment_statement\n              | function_call\n              | print_statement\n              | empty\n    \n    conditional : inline_if_statement\n                | block_if_else_statement\n                | for_statement\n                | while_statement\n    inline_if_statement : IF expression COLON statements\n                           \n     block_if_else_statement : IF expression COLON statements block_else_statement\n    \n     block_else_statement : ELSE statements\n                          | ELSE expression COLON statements\n                          | ELSE block_if_else_statement\n    \n    for_statement : FOR expression IN range_expression\n    \n    range_expression : RANGE expression COMMA expression\n    \n    while_statement : WHILE expression COLON statements\n    \n    bool : TRUE\n         | FALSE\n    \n    print_statement : PRINT LPAREN expression RPAREN\n    \n    expression : term\n               | expression PLUS term\n               | expression MINUS term\n               | expression TIMES term\n               | expression DIVIDE term\n               | expression EQUALEQUAL term\n               | expression EQUAL term\n               | expression NOTEQUAL term\n               | expression LESSEQUAL term\n               | expression GREATEREQUAL term\n               | expression PLUSEQUAL term\n               | expression MINUSEQUAL term\n               | expression TIMESEQUAL term\n               | expression DIVIDEEQUAL term\n               | expression GREATERTHAN term\n               | expression LESSTHAN term\n               | LPAREN expression RPAREN\n    \n    term : INTEGER\n         | FLOAT\n         | STRING\n         | IDENTIFIER\n         | bool\n         | LPAREN expression RPAREN\n    assignment_statement : IDENTIFIER EQUAL expressionfunction_call : IDENTIFIER LPAREN argument_list RPARENargument_list : expression\n                     | argument_list COMMA expression\n    empty :\n    '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,23,24,25,26,27,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,74,76,78,79,80,82,83,85,86,88,89,90,92,94,96,97,98,99,],[-53,0,-1,-3,-4,-5,-6,-7,-8,-9,-11,-12,-13,-14,-26,-46,-43,-44,-45,-47,-23,-24,-2,-46,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-49,-53,-53,-50,-25,-15,-20,-22,-48,-16,-53,-17,-6,-12,-46,-53,-21,-18,-53,-15,]),'LPAREN':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,74,76,77,78,79,80,81,82,83,85,86,88,89,90,91,92,93,94,96,97,98,99,],[15,15,-4,-5,-6,-7,-8,-9,-11,-12,-13,-14,-26,15,46,47,15,15,15,-43,-44,-45,-47,-23,-24,-2,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-46,15,15,15,-27,15,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-49,15,15,-50,15,-25,-15,-20,15,-22,-48,-16,15,-17,-6,-12,15,46,15,15,-21,-18,15,-15,]),'IDENTIFIER':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,74,76,77,78,79,80,81,82,83,85,86,88,89,90,91,92,93,94,96,97,98,99,],[16,16,-4,-5,-6,-7,-8,-9,-11,-12,-13,-14,-26,44,-46,44,44,44,-43,-44,-45,-47,-23,-24,-2,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-46,44,44,44,-27,44,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-49,16,16,-50,44,-25,-15,-20,44,-22,-48,-16,92,-17,-6,-12,44,-46,44,16,-21,-18,16,-15,]),'PRINT':([0,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,23,24,25,26,27,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,74,76,78,79,80,82,83,85,86,88,89,90,92,94,96,97,98,99,],[17,17,-4,-5,-6,-7,-8,-9,-11,-12,-13,-14,-26,-46,-43,-44,-45,-47,-23,-24,-2,-46,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-49,17,17,-50,-25,-15,-20,-22,-48,-16,17,-17,-6,-12,-46,17,-21,-18,17,-15,]),'IF':([0,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,23,24,25,26,27,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,74,76,78,79,80,82,83,85,86,88,89,90,92,94,96,97,98,99,],[18,18,-4,-5,-6,-7,-8,-9,-11,-12,-13,-14,-26,-46,-43,-44,-45,-47,-23,-24,-2,-46,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-49,18,18,-50,-25,-15,-20,-22,-48,-16,91,-17,-6,-12,-46,18,-21,-18,18,-15,]),'FOR':([0,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,23,24,25,26,27,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,74,76,78,79,80,82,83,85,86,88,89,90,92,94,96,97,98,99,],[19,19,-4,-5,-6,-7,-8,-9,-11,-12,-13,-14,-26,-46,-43,-44,-45,-47,-23,-24,-2,-46,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-49,19,19,-50,-25,-15,-20,-22,-48,-16,19,-17,-6,-12,-46,19,-21,-18,19,-15,]),'WHILE':([0,3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,23,24,25,26,27,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,74,76,78,79,80,82,83,85,86,88,89,90,92,94,96,97,98,99,],[20,20,-4,-5,-6,-7,-8,-9,-11,-12,-13,-14,-26,-46,-43,-44,-45,-47,-23,-24,-2,-46,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-49,20,20,-50,-25,-15,-20,-22,-48,-16,20,-17,-6,-12,-46,20,-21,-18,20,-15,]),'INTEGER':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,74,76,77,78,79,80,81,82,83,85,86,88,89,90,91,92,93,94,96,97,98,99,],[21,21,-4,-5,-6,-7,-8,-9,-11,-12,-13,-14,-26,21,-46,21,21,21,-43,-44,-45,-47,-23,-24,-2,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-46,21,21,21,-27,21,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-49,21,21,-50,21,-25,-15,-20,21,-22,-48,-16,21,-17,-6,-12,21,-46,21,21,-21,-18,21,-15,]),'FLOAT':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,74,76,77,78,79,80,81,82,83,85,86,88,89,90,91,92,93,94,96,97,98,99,],[22,22,-4,-5,-6,-7,-8,-9,-11,-12,-13,-14,-26,22,-46,22,22,22,-43,-44,-45,-47,-23,-24,-2,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-46,22,22,22,-27,22,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-49,22,22,-50,22,-25,-15,-20,22,-22,-48,-16,22,-17,-6,-12,22,-46,22,22,-21,-18,22,-15,]),'STRING':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,74,76,77,78,79,80,81,82,83,85,86,88,89,90,91,92,93,94,96,97,98,99,],[23,23,-4,-5,-6,-7,-8,-9,-11,-12,-13,-14,-26,23,-46,23,23,23,-43,-44,-45,-47,-23,-24,-2,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-46,23,23,23,-27,23,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-49,23,23,-50,23,-25,-15,-20,23,-22,-48,-16,23,-17,-6,-12,23,-46,23,23,-21,-18,23,-15,]),'TRUE':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,74,76,77,78,79,80,81,82,83,85,86,88,89,90,91,92,93,94,96,97,98,99,],[25,25,-4,-5,-6,-7,-8,-9,-11,-12,-13,-14,-26,25,-46,25,25,25,-43,-44,-45,-47,-23,-24,-2,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-46,25,25,25,-27,25,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-49,25,25,-50,25,-25,-15,-20,25,-22,-48,-16,25,-17,-6,-12,25,-46,25,25,-21,-18,25,-15,]),'FALSE':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,74,76,77,78,79,80,81,82,83,85,86,88,89,90,91,92,93,94,96,97,98,99,],[26,26,-4,-5,-6,-7,-8,-9,-11,-12,-13,-14,-26,26,-46,26,26,26,-43,-44,-45,-47,-23,-24,-2,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-46,26,26,26,-27,26,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-49,26,26,-50,26,-25,-15,-20,26,-22,-48,-16,26,-17,-6,-12,26,-46,26,26,-21,-18,26,-15,]),'ELSE':([3,4,5,6,7,8,9,10,11,12,13,14,16,21,22,23,24,25,26,27,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,74,76,78,79,80,82,83,85,86,88,89,90,92,94,96,97,98,99,],[-3,-4,-5,-6,-7,-8,-9,-11,-12,-13,-14,-26,-46,-43,-44,-45,-47,-23,-24,-2,-46,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-49,-53,-53,-50,-25,86,-20,-22,-48,-16,-53,-17,-6,-12,-46,-53,-21,-18,-53,86,]),'PLUS':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[28,-26,-46,-43,-44,-45,-47,-23,-24,28,-46,28,28,28,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,28,28,28,28,-48,28,28,28,-46,28,28,]),'MINUS':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[29,-26,-46,-43,-44,-45,-47,-23,-24,29,-46,29,29,29,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,29,29,29,29,-48,29,29,29,-46,29,29,]),'TIMES':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[30,-26,-46,-43,-44,-45,-47,-23,-24,30,-46,30,30,30,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,30,30,30,30,-48,30,30,30,-46,30,30,]),'DIVIDE':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[31,-26,-46,-43,-44,-45,-47,-23,-24,31,-46,31,31,31,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,31,31,31,31,-48,31,31,31,-46,31,31,]),'EQUALEQUAL':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[32,-26,-46,-43,-44,-45,-47,-23,-24,32,-46,32,32,32,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,32,32,32,32,-48,32,32,32,-46,32,32,]),'EQUAL':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[33,-26,45,-43,-44,-45,-47,-23,-24,33,-46,33,33,33,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,33,33,33,33,-48,33,33,33,45,33,33,]),'NOTEQUAL':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[34,-26,-46,-43,-44,-45,-47,-23,-24,34,-46,34,34,34,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,34,34,34,34,-48,34,34,34,-46,34,34,]),'LESSEQUAL':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[35,-26,-46,-43,-44,-45,-47,-23,-24,35,-46,35,35,35,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,35,35,35,35,-48,35,35,35,-46,35,35,]),'GREATEREQUAL':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[36,-26,-46,-43,-44,-45,-47,-23,-24,36,-46,36,36,36,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,36,36,36,36,-48,36,36,36,-46,36,36,]),'PLUSEQUAL':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[37,-26,-46,-43,-44,-45,-47,-23,-24,37,-46,37,37,37,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,37,37,37,37,-48,37,37,37,-46,37,37,]),'MINUSEQUAL':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[38,-26,-46,-43,-44,-45,-47,-23,-24,38,-46,38,38,38,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,38,38,38,38,-48,38,38,38,-46,38,38,]),'TIMESEQUAL':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[39,-26,-46,-43,-44,-45,-47,-23,-24,39,-46,39,39,39,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,39,39,39,39,-48,39,39,39,-46,39,39,]),'DIVIDEEQUAL':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[40,-26,-46,-43,-44,-45,-47,-23,-24,40,-46,40,40,40,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,40,40,40,40,-48,40,40,40,-46,40,40,]),'GREATERTHAN':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[41,-26,-46,-43,-44,-45,-47,-23,-24,41,-46,41,41,41,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,41,41,41,41,-48,41,41,41,-46,41,41,]),'LESSTHAN':([6,14,16,21,22,23,24,25,26,43,44,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,75,83,84,87,89,92,95,96,],[42,-26,-46,-43,-44,-45,-47,-23,-24,42,-46,42,42,42,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,42,42,42,42,-48,42,42,42,-46,42,42,]),'RPAREN':([14,21,22,23,24,25,26,43,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,75,83,84,],[-26,-43,-44,-45,-47,-23,-24,67,-46,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,76,-51,78,83,-48,-52,]),'COLON':([14,21,22,23,24,25,26,44,48,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,83,89,92,95,],[-26,-43,-44,-45,-47,-23,-24,-46,72,74,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-48,94,-46,98,]),'IN':([14,21,22,23,24,25,26,44,49,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,83,],[-26,-43,-44,-45,-47,-23,-24,-46,73,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-48,]),'COMMA':([14,21,22,23,24,25,26,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,83,84,87,],[-26,-43,-44,-45,-47,-23,-24,-46,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,77,-51,-48,-52,93,]),'RANGE':([73,],[81,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'newCode':([0,],[1,]),'statements':([0,3,72,74,86,94,98,],[2,27,79,82,88,97,99,]),'statement':([0,3,72,74,86,94,98,],[3,3,3,3,3,3,3,]),'empty':([0,3,72,74,86,94,98,],[4,4,4,4,4,4,4,]),'conditional':([0,3,72,74,86,94,98,],[5,5,5,5,5,5,5,]),'expression':([0,3,15,18,19,20,45,46,47,52,72,74,77,81,86,91,93,94,98,],[6,6,43,48,49,50,68,70,71,75,6,6,84,87,89,95,96,6,6,]),'assignment_statement':([0,3,72,74,86,94,98,],[7,7,7,7,7,7,7,]),'function_call':([0,3,72,74,86,94,98,],[8,8,8,8,8,8,8,]),'print_statement':([0,3,72,74,86,94,98,],[9,9,9,9,9,9,9,]),'inline_if_statement':([0,3,72,74,86,94,98,],[10,10,10,10,10,10,10,]),'block_if_else_statement':([0,3,72,74,86,94,98,],[11,11,11,11,90,11,11,]),'for_statement':([0,3,72,74,86,94,98,],[12,12,12,12,12,12,12,]),'while_statement':([0,3,72,74,86,94,98,],[13,13,13,13,13,13,13,]),'term':([0,3,15,18,19,20,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,47,52,72,74,77,81,86,91,93,94,98,],[14,14,14,14,14,14,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'bool':([0,3,15,18,19,20,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,45,46,47,52,72,74,77,81,86,91,93,94,98,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'argument_list':([46,],[69,]),'range_expression':([73,],[80,]),'block_else_statement':([79,99,],[85,85,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> newCode","S'",1,None,None,None),
  ('newCode -> statements','newCode',1,'p_newCode','newParser.py',12),
  ('statements -> statement statements','statements',2,'p_statements','newParser.py',19),
  ('statements -> statement','statements',1,'p_statements','newParser.py',20),
  ('statements -> empty','statements',1,'p_statements','newParser.py',21),
  ('statement -> conditional','statement',1,'p_statement','newParser.py',33),
  ('statement -> expression','statement',1,'p_statement','newParser.py',34),
  ('statement -> assignment_statement','statement',1,'p_statement','newParser.py',35),
  ('statement -> function_call','statement',1,'p_statement','newParser.py',36),
  ('statement -> print_statement','statement',1,'p_statement','newParser.py',37),
  ('statement -> empty','statement',1,'p_statement','newParser.py',38),
  ('conditional -> inline_if_statement','conditional',1,'p_conditional','newParser.py',45),
  ('conditional -> block_if_else_statement','conditional',1,'p_conditional','newParser.py',46),
  ('conditional -> for_statement','conditional',1,'p_conditional','newParser.py',47),
  ('conditional -> while_statement','conditional',1,'p_conditional','newParser.py',48),
  ('inline_if_statement -> IF expression COLON statements','inline_if_statement',4,'p_inline_if_statement','newParser.py',54),
  ('block_if_else_statement -> IF expression COLON statements block_else_statement','block_if_else_statement',5,'p_block_if_else_statement','newParser.py',63),
  ('block_else_statement -> ELSE statements','block_else_statement',2,'p_block_else_statement','newParser.py',70),
  ('block_else_statement -> ELSE expression COLON statements','block_else_statement',4,'p_block_else_statement','newParser.py',71),
  ('block_else_statement -> ELSE block_if_else_statement','block_else_statement',2,'p_block_else_statement','newParser.py',72),
  ('for_statement -> FOR expression IN range_expression','for_statement',4,'p_for_statement','newParser.py',84),
  ('range_expression -> RANGE expression COMMA expression','range_expression',4,'p_range_expression','newParser.py',91),
  ('while_statement -> WHILE expression COLON statements','while_statement',4,'p_while_statement','newParser.py',98),
  ('bool -> TRUE','bool',1,'p_bool','newParser.py',105),
  ('bool -> FALSE','bool',1,'p_bool','newParser.py',106),
  ('print_statement -> PRINT LPAREN expression RPAREN','print_statement',4,'p_print_statement','newParser.py',113),
  ('expression -> term','expression',1,'p_expression','newParser.py',120),
  ('expression -> expression PLUS term','expression',3,'p_expression','newParser.py',121),
  ('expression -> expression MINUS term','expression',3,'p_expression','newParser.py',122),
  ('expression -> expression TIMES term','expression',3,'p_expression','newParser.py',123),
  ('expression -> expression DIVIDE term','expression',3,'p_expression','newParser.py',124),
  ('expression -> expression EQUALEQUAL term','expression',3,'p_expression','newParser.py',125),
  ('expression -> expression EQUAL term','expression',3,'p_expression','newParser.py',126),
  ('expression -> expression NOTEQUAL term','expression',3,'p_expression','newParser.py',127),
  ('expression -> expression LESSEQUAL term','expression',3,'p_expression','newParser.py',128),
  ('expression -> expression GREATEREQUAL term','expression',3,'p_expression','newParser.py',129),
  ('expression -> expression PLUSEQUAL term','expression',3,'p_expression','newParser.py',130),
  ('expression -> expression MINUSEQUAL term','expression',3,'p_expression','newParser.py',131),
  ('expression -> expression TIMESEQUAL term','expression',3,'p_expression','newParser.py',132),
  ('expression -> expression DIVIDEEQUAL term','expression',3,'p_expression','newParser.py',133),
  ('expression -> expression GREATERTHAN term','expression',3,'p_expression','newParser.py',134),
  ('expression -> expression LESSTHAN term','expression',3,'p_expression','newParser.py',135),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','newParser.py',136),
  ('term -> INTEGER','term',1,'p_term','newParser.py',153),
  ('term -> FLOAT','term',1,'p_term','newParser.py',154),
  ('term -> STRING','term',1,'p_term','newParser.py',155),
  ('term -> IDENTIFIER','term',1,'p_term','newParser.py',156),
  ('term -> bool','term',1,'p_term','newParser.py',157),
  ('term -> LPAREN expression RPAREN','term',3,'p_term','newParser.py',158),
  ('assignment_statement -> IDENTIFIER EQUAL expression','assignment_statement',3,'p_assignment_statement','newParser.py',164),
  ('function_call -> IDENTIFIER LPAREN argument_list RPAREN','function_call',4,'p_function_call','newParser.py',169),
  ('argument_list -> expression','argument_list',1,'p_argument_list','newParser.py',174),
  ('argument_list -> argument_list COMMA expression','argument_list',3,'p_argument_list','newParser.py',175),
  ('empty -> <empty>','empty',0,'p_empty','newParser.py',184),
]
