
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'statementsAND BREAK Bool CASE CLASS COLON COMMA COMMENTS DEF DIVIDE DIVIDEEQUAL DO DOUBLEQUOTES Double ELIF ELSE EQUAL EQUALEQUAL EQUALTO FALSE FINALLY FLOAT FOR FUNC Float GLOBAL GREATEREQUAL GREATERTHAN IDENTIFIER IF IMPORT IN INT INTEGER IS LCURVEDBRACE LESSEQUAL LESSTHAN LPAREN LSQUAREDBRACKET MAIN MINUS MINUSEQUAL NOT NOTEQUAL OR PLUS PLUSEQUAL PRINT RANGE RCURVEDBRACE RESERVEDWORD RETURN RPAREN RSQUAREDBRACKET RULE_CLOSE RULE_OPEN SINGLEQUOTES STRING SWITCH Str THEN TIMES TIMESEQUAL TRUE UNTIL WHILE\n    statements : statement statements\n               | statement\n               | empty\n    \n    statement : conditional\n              | expression\n              | assignment_statement\n              | function_call\n              | print_statement\n              | empty\n    \n    conditional : inline_if_statement\n                | for_statement\n                | while_statement\n    inline_if_statement : IF expression COLON statements\n                           | IF expression COLON statements ELSE statements\n    for_statement : FOR expression IN range_expression\n    \n    range_expression : RANGE expression COMMA expression\n    \n    while_statement : WHILE expression COLON statements\n    \n    bool : TRUE\n         | FALSE\n    \n    print_statement : PRINT LPAREN expression RPAREN\n    \n    expression : expression PLUS expression\n               | expression MINUS expression\n               | expression TIMES expression\n               | expression DIVIDE expression\n               | expression EQUALTO expression\n               | LPAREN expression RPAREN\n               | INTEGER\n               | FLOAT\n               | IDENTIFIER\n               | bool\n    assignment_statement : IDENTIFIER EQUAL expressionfunction_call : IDENTIFIER LPAREN argument_list RPARENargument_list : expression\n                     | argument_list COMMA expression\n    empty :\n    '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,21,22,23,30,37,38,39,40,41,42,43,47,49,50,52,53,54,56,58,60,62,],[-35,0,-2,-3,-4,-5,-6,-7,-8,-10,-11,-12,-27,-28,-29,-30,-18,-19,-1,-29,-21,-22,-23,-24,-25,-26,-31,-35,-35,-32,-20,-13,-15,-17,-35,-14,-16,]),'LPAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,37,38,39,40,41,42,43,47,49,50,51,52,53,54,55,56,58,60,61,62,],[12,12,-3,-4,-5,-6,-7,-8,-10,-11,-12,12,-27,-28,32,-30,33,12,12,12,-18,-19,-1,12,12,12,12,12,-29,12,12,12,-21,-22,-23,-24,-25,-26,-31,12,12,-32,12,-20,-13,-15,12,-17,12,-14,12,-16,]),'INTEGER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,37,38,39,40,41,42,43,47,49,50,51,52,53,54,55,56,58,60,61,62,],[13,13,-3,-4,-5,-6,-7,-8,-10,-11,-12,13,-27,-28,-29,-30,13,13,13,-18,-19,-1,13,13,13,13,13,-29,13,13,13,-21,-22,-23,-24,-25,-26,-31,13,13,-32,13,-20,-13,-15,13,-17,13,-14,13,-16,]),'FLOAT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,37,38,39,40,41,42,43,47,49,50,51,52,53,54,55,56,58,60,61,62,],[14,14,-3,-4,-5,-6,-7,-8,-10,-11,-12,14,-27,-28,-29,-30,14,14,14,-18,-19,-1,14,14,14,14,14,-29,14,14,14,-21,-22,-23,-24,-25,-26,-31,14,14,-32,14,-20,-13,-15,14,-17,14,-14,14,-16,]),'IDENTIFIER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,37,38,39,40,41,42,43,47,49,50,51,52,53,54,55,56,58,60,61,62,],[15,15,-3,-4,-5,-6,-7,-8,-10,-11,-12,30,-27,-28,-29,-30,30,30,30,-18,-19,-1,30,30,30,30,30,-29,30,30,30,-21,-22,-23,-24,-25,-26,-31,15,15,-32,30,-20,-13,-15,30,-17,15,-14,30,-16,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,21,22,23,30,37,38,39,40,41,42,43,47,49,50,52,53,54,56,58,60,62,],[17,17,-3,-4,-5,-6,-7,-8,-10,-11,-12,-27,-28,-29,-30,-18,-19,-1,-29,-21,-22,-23,-24,-25,-26,-31,17,17,-32,-20,-13,-15,-17,17,-14,-16,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,21,22,23,30,37,38,39,40,41,42,43,47,49,50,52,53,54,56,58,60,62,],[18,18,-3,-4,-5,-6,-7,-8,-10,-11,-12,-27,-28,-29,-30,-18,-19,-1,-29,-21,-22,-23,-24,-25,-26,-31,18,18,-32,-20,-13,-15,-17,18,-14,-16,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,21,22,23,30,37,38,39,40,41,42,43,47,49,50,52,53,54,56,58,60,62,],[19,19,-3,-4,-5,-6,-7,-8,-10,-11,-12,-27,-28,-29,-30,-18,-19,-1,-29,-21,-22,-23,-24,-25,-26,-31,19,19,-32,-20,-13,-15,-17,19,-14,-16,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,13,14,15,16,21,22,23,30,37,38,39,40,41,42,43,47,49,50,52,53,54,56,58,60,62,],[20,20,-3,-4,-5,-6,-7,-8,-10,-11,-12,-27,-28,-29,-30,-18,-19,-1,-29,-21,-22,-23,-24,-25,-26,-31,20,20,-32,-20,-13,-15,-17,20,-14,-16,]),'TRUE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,37,38,39,40,41,42,43,47,49,50,51,52,53,54,55,56,58,60,61,62,],[21,21,-3,-4,-5,-6,-7,-8,-10,-11,-12,21,-27,-28,-29,-30,21,21,21,-18,-19,-1,21,21,21,21,21,-29,21,21,21,-21,-22,-23,-24,-25,-26,-31,21,21,-32,21,-20,-13,-15,21,-17,21,-14,21,-16,]),'FALSE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,37,38,39,40,41,42,43,47,49,50,51,52,53,54,55,56,58,60,61,62,],[22,22,-3,-4,-5,-6,-7,-8,-10,-11,-12,22,-27,-28,-29,-30,22,22,22,-18,-19,-1,22,22,22,22,22,-29,22,22,22,-21,-22,-23,-24,-25,-26,-31,22,22,-32,22,-20,-13,-15,22,-17,22,-14,22,-16,]),'ELSE':([2,3,4,5,6,7,8,9,10,11,13,14,15,16,21,22,23,30,37,38,39,40,41,42,43,47,49,50,52,53,54,56,58,60,62,],[-2,-3,-4,-5,-6,-7,-8,-10,-11,-12,-27,-28,-29,-30,-18,-19,-1,-29,-21,-22,-23,-24,-25,-26,-31,-35,-35,-32,-20,58,-15,-17,-35,-14,-16,]),'PLUS':([5,13,14,15,16,21,22,29,30,34,35,36,37,38,39,40,41,42,43,45,46,57,59,62,],[24,-27,-28,-29,-30,-18,-19,24,-29,24,24,24,24,24,24,24,24,-26,24,24,24,24,24,24,]),'MINUS':([5,13,14,15,16,21,22,29,30,34,35,36,37,38,39,40,41,42,43,45,46,57,59,62,],[25,-27,-28,-29,-30,-18,-19,25,-29,25,25,25,25,25,25,25,25,-26,25,25,25,25,25,25,]),'TIMES':([5,13,14,15,16,21,22,29,30,34,35,36,37,38,39,40,41,42,43,45,46,57,59,62,],[26,-27,-28,-29,-30,-18,-19,26,-29,26,26,26,26,26,26,26,26,-26,26,26,26,26,26,26,]),'DIVIDE':([5,13,14,15,16,21,22,29,30,34,35,36,37,38,39,40,41,42,43,45,46,57,59,62,],[27,-27,-28,-29,-30,-18,-19,27,-29,27,27,27,27,27,27,27,27,-26,27,27,27,27,27,27,]),'EQUALTO':([5,13,14,15,16,21,22,29,30,34,35,36,37,38,39,40,41,42,43,45,46,57,59,62,],[28,-27,-28,-29,-30,-18,-19,28,-29,28,28,28,28,28,28,28,28,-26,28,28,28,28,28,28,]),'RPAREN':([13,14,16,21,22,29,30,37,38,39,40,41,42,44,45,46,57,],[-27,-28,-30,-18,-19,42,-29,-21,-22,-23,-24,-25,-26,50,-33,52,-34,]),'COLON':([13,14,16,21,22,30,34,36,37,38,39,40,41,42,],[-27,-28,-30,-18,-19,-29,47,49,-21,-22,-23,-24,-25,-26,]),'IN':([13,14,16,21,22,30,35,37,38,39,40,41,42,],[-27,-28,-30,-18,-19,-29,48,-21,-22,-23,-24,-25,-26,]),'COMMA':([13,14,16,21,22,30,37,38,39,40,41,42,44,45,57,59,],[-27,-28,-30,-18,-19,-29,-21,-22,-23,-24,-25,-26,51,-33,-34,61,]),'EQUAL':([15,],[31,]),'RANGE':([48,],[55,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,2,47,49,58,],[1,23,53,56,60,]),'statement':([0,2,47,49,58,],[2,2,2,2,2,]),'empty':([0,2,47,49,58,],[3,3,3,3,3,]),'conditional':([0,2,47,49,58,],[4,4,4,4,4,]),'expression':([0,2,12,18,19,20,24,25,26,27,28,31,32,33,47,49,51,55,58,61,],[5,5,29,34,35,36,37,38,39,40,41,43,45,46,5,5,57,59,5,62,]),'assignment_statement':([0,2,47,49,58,],[6,6,6,6,6,]),'function_call':([0,2,47,49,58,],[7,7,7,7,7,]),'print_statement':([0,2,47,49,58,],[8,8,8,8,8,]),'inline_if_statement':([0,2,47,49,58,],[9,9,9,9,9,]),'for_statement':([0,2,47,49,58,],[10,10,10,10,10,]),'while_statement':([0,2,47,49,58,],[11,11,11,11,11,]),'bool':([0,2,12,18,19,20,24,25,26,27,28,31,32,33,47,49,51,55,58,61,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'argument_list':([32,],[44,]),'range_expression':([48,],[54,]),}

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
  ('statement -> empty','statement',1,'p_statement','newParser.py',31),
  ('conditional -> inline_if_statement','conditional',1,'p_conditional','newParser.py',38),
  ('conditional -> for_statement','conditional',1,'p_conditional','newParser.py',39),
  ('conditional -> while_statement','conditional',1,'p_conditional','newParser.py',40),
  ('inline_if_statement -> IF expression COLON statements','inline_if_statement',4,'p_inline_if_statement','newParser.py',46),
  ('inline_if_statement -> IF expression COLON statements ELSE statements','inline_if_statement',6,'p_inline_if_statement','newParser.py',47),
  ('for_statement -> FOR expression IN range_expression','for_statement',4,'p_for_statement','newParser.py',56),
  ('range_expression -> RANGE expression COMMA expression','range_expression',4,'p_range_expression','newParser.py',63),
  ('while_statement -> WHILE expression COLON statements','while_statement',4,'p_while_statement','newParser.py',70),
  ('bool -> TRUE','bool',1,'p_bool','newParser.py',77),
  ('bool -> FALSE','bool',1,'p_bool','newParser.py',78),
  ('print_statement -> PRINT LPAREN expression RPAREN','print_statement',4,'p_print_statement','newParser.py',85),
  ('expression -> expression PLUS expression','expression',3,'p_expression','newParser.py',92),
  ('expression -> expression MINUS expression','expression',3,'p_expression','newParser.py',93),
  ('expression -> expression TIMES expression','expression',3,'p_expression','newParser.py',94),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','newParser.py',95),
  ('expression -> expression EQUALTO expression','expression',3,'p_expression','newParser.py',96),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','newParser.py',97),
  ('expression -> INTEGER','expression',1,'p_expression','newParser.py',98),
  ('expression -> FLOAT','expression',1,'p_expression','newParser.py',99),
  ('expression -> IDENTIFIER','expression',1,'p_expression','newParser.py',100),
  ('expression -> bool','expression',1,'p_expression','newParser.py',101),
  ('assignment_statement -> IDENTIFIER EQUAL expression','assignment_statement',3,'p_assignment_statement','newParser.py',112),
  ('function_call -> IDENTIFIER LPAREN argument_list RPAREN','function_call',4,'p_function_call','newParser.py',117),
  ('argument_list -> expression','argument_list',1,'p_argument_list','newParser.py',122),
  ('argument_list -> argument_list COMMA expression','argument_list',3,'p_argument_list','newParser.py',123),
  ('empty -> <empty>','empty',0,'p_empty','newParser.py',132),
]
