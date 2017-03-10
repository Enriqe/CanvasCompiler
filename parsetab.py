
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'EQUALS L_BRACKET R_BRACKET G_THAN L_THAN NOT_EQUALS EQUALS_EQUALS G_THAN_EQUALS L_THAN_EQUALS PLUS MINUS DIV MULT L_PAR R_PAR COMMA INT_VAL DEC_VAL STRING_VAL YESNO_VAL VAR_IDENTIFIER FUNCTION RETURNS FINISH TRIANGLE STRING POINT INT HEIGHT Y IF IN RETURN ELSE WITH COLOR YESNO BLUE CANVAS MAIN CENTER FOR PAINT READ WHILE WIDTH ADD PROGRAM GREEN RED ELSIF EACH PRINT X CIRCLE DEC RECTANGLE\n    program : PROGRAM VAR_IDENTIFIER globals MAIN block_with_declaration FINISH\n    \n    globals : function \n            | declaration\n    \n    function : FUNCTION VAR_IDENTIFIER L_PAR function_arguments R_PAR RETURNS type block_with_declaration\n    \n    function_arguments : type VAR_IDENTIFIER\n                       | type VAR_IDENTIFIER COMMA function_arguments\n                       | null\n    \n    type : INT\n         | DEC\n         | STRING\n         | YESNO\n    \n    var : type VAR_IDENTIFIER list_index EQUALS expression\n    \n    list_index : L_BRACKET INT_VAL R_BRACKET\n               | null\n    \n    null :\n    \n    shape : shape_type VAR_IDENTIFIER CENTER EQUALS point WIDTH EQUALS expression HEIGHT EQUALS expression color\n    \n    shape_type : CIRCLE\n               | RECTANGLE\n               | TRIANGLE\n    \n    block_with_declaration : L_BRACKET declaration_type R_BRACKET\n    \n    declaration_type : statement\n                     | declaration\n    \n    block : L_BRACKET block_contains R_BRACKET\n    \n    block_contains : statement\n                   | null\n    \n    statement : assignment\n              | conditional\n              | print\n              | for_loop\n              | while_loop\n              | paint\n              | read\n              | return\n    \n    assignment : var_assignment\n               | shape_assignment\n               | point_assignment\n               | canvas_assignment\n    \n    var_assignment : VAR_IDENTIFIER list_index EQUALS var_equals\n    \n    var_equals : expression\n              | VAR_IDENTIFIER\n    \n    shape_assignment : VAR_IDENTIFIER EQUALS VAR_IDENTIFIER\n                     | CENTER EQUALS POINT\n                     | WIDTH EQUALS expression\n                     | HEIGHT EQUALS expression\n                     | COLOR EQUALS VAR_IDENTIFIER\n    \n    declaration : var\n                | shape\n                | point\n                | canvas\n    \n    point : POINT VAR_IDENTIFIER X EQUALS expression Y EQUALS expression\n    \n    point_assignment : VAR_IDENTIFIER EQUALS VAR_IDENTIFIER\n                     | X EQUALS expression\n                     | Y EQUALS expression\n    \n    canvas : CANVAS VAR_IDENTIFIER WIDTH EQUALS expression HEIGHT EQUALS expression color\n    \n    canvas_assignment : VAR_IDENTIFIER ADD VAR_IDENTIFIER\n                      | VAR_IDENTIFIER EQUALS VAR_IDENTIFIER\n                      | WIDTH EQUALS expression\n                      | HEIGHT EQUALS expression\n                      | COLOR EQUALS expression\n    \n    expression : exp exp_ops exp\n    \n    exp_ops : L_THAN\n            | G_THAN\n            | EQUALS_EQUALS\n            | NOT_EQUALS\n            | G_THAN_EQUALS\n            | L_THAN_EQUALS\n    \n    exp : term\n        | PLUS exp\n        | MINUS exp\n    \n    term : factor term_loop\n    \n    term_loop : DIV term\n              | MULT term\n              | null\n    \n    factor : factor_id\n           | factor_exp\n    \n    factor_id : L_PAR expression R_PAR\n    \n    factor_exp : factor_sign VAR_IDENTIFIER list_index\n    \n    factor_sign : MINUS\n                | PLUS\n                | null\n    \n    conditional : IF conditional_if conditional_elsif conditional_else\n    \n    conditional_if : L_PAR expression R_PAR block\n    \n    conditional_elsif : ELSIF conditional_if conditional_elsif\n                      | null\n    \n    conditional_else : ELSE block\n                     | null\n    \n    print : PRINT L_PAR print_b print_a R_PAR\n    \n    print_a : COMMA print_b print_a\n            | null\n    \n    print_b : expression\n            | VAR_IDENTIFIER\n    \n    read : READ VAR_IDENTIFIER\n    \n    paint : PAINT VAR_IDENTIFIER\n    \n    return : RETURN expression\n    \n    for_loop : FOR EACH VAR_IDENTIFIER IN VAR_IDENTIFIER block\n    \n    while_loop : WHILE L_PAR expression R_PAR block\n    \n    color : COLOR VAR_IDENTIFIER RED EQUALS expression GREEN EQUALS expression BLUE EQUALS expression\n    expression : expression PLUS term'
    
_lr_action_items = {'TRIANGLE':([3,31,],[5,5,]),'READ':([31,180,],[53,53,]),'R_BRACKET':([6,7,10,11,34,43,45,48,51,52,54,55,56,57,58,59,61,62,69,70,72,78,79,80,85,87,95,104,105,106,107,113,115,123,125,128,129,135,136,138,139,140,141,142,143,145,147,153,154,155,156,159,160,166,167,168,170,172,173,179,180,181,183,184,185,187,190,191,192,193,194,197,203,210,],[-48,-47,-49,-46,-14,-27,90,-34,-31,-36,-29,-33,-21,-30,-32,-26,-28,-22,-35,-37,107,-67,-74,-75,-15,-94,-92,-15,-93,-12,-13,-15,-68,-70,-73,-69,-43,-45,-59,-41,-55,-53,-52,-44,-42,-15,-84,-77,-76,-60,-71,-72,-98,-38,-40,-39,-81,-86,-15,-87,-15,-96,-82,-85,-83,-50,197,-25,-24,-95,-54,-23,-16,-97,]),'EQUALS_EQUALS':([34,78,79,80,84,85,107,113,115,123,125,128,153,154,156,159,],[-14,-67,-74,-75,120,-15,-13,-15,-68,-70,-73,-69,-77,-76,-71,-72,]),'WIDTH':([26,31,34,78,79,80,85,107,110,113,115,123,125,128,153,154,155,156,159,160,180,187,],[35,44,-14,-67,-74,-75,-15,-13,150,-15,-68,-70,-73,-69,-77,-76,-60,-71,-72,-98,44,-50,]),'WHILE':([31,180,],[47,47,]),'PROGRAM':([0,],[2,]),'GREEN':([34,78,79,80,85,107,113,115,123,125,128,153,154,155,156,159,160,204,],[-14,-67,-74,-75,-15,-13,-15,-68,-70,-73,-69,-77,-76,-60,-71,-72,-98,205,]),'R_PAR':([29,34,38,39,77,78,79,80,85,107,112,113,114,115,123,125,128,130,131,132,133,144,152,153,154,155,156,159,160,162,163,178,189,],[-15,-14,76,-7,-5,-67,-74,-75,-15,-13,-15,-15,154,-68,-70,-73,-69,-91,-90,-15,164,169,-6,-77,-76,-60,-71,-72,-98,-89,179,-15,-88,]),'PRINT':([31,180,],[46,46,]),'RETURN':([31,180,],[42,42,]),'DIV':([34,79,80,85,107,113,153,154,],[-14,-74,-75,124,-13,-15,-77,-76,]),'DEC':([3,29,31,111,112,],[9,9,9,9,9,]),'MINUS':([42,71,73,74,82,83,88,89,91,92,94,99,100,101,103,116,117,118,119,120,121,122,124,126,127,137,161,174,175,176,199,202,206,209,],[88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,-62,88,-64,-66,-63,-61,-65,158,158,158,88,88,88,88,88,88,88,88,88,]),'MULT':([34,79,80,85,107,113,153,154,],[-14,-74,-75,126,-13,-15,-77,-76,]),'YESNO':([3,29,31,111,112,],[17,17,17,17,17,]),'POINT':([3,31,75,102,],[20,20,20,143,]),'COLOR':([31,34,78,79,80,85,107,113,115,123,125,128,153,154,155,156,159,160,180,186,201,],[50,-14,-67,-74,-75,-15,-13,-15,-68,-70,-73,-69,-77,-76,-60,-71,-72,-98,50,195,195,]),'ELSE':([104,145,147,173,183,185,197,],[-15,171,-84,-15,-82,-83,-23,]),'PLUS':([34,42,71,73,74,78,79,80,82,83,85,87,88,89,91,92,94,99,100,101,103,106,107,108,109,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,131,133,136,137,140,141,142,144,153,154,155,156,159,160,161,168,174,175,176,186,187,188,199,201,202,204,206,207,209,210,],[-14,83,83,83,83,-67,-74,-75,83,83,-15,127,83,83,83,83,83,83,83,83,83,127,-13,127,127,-15,127,-68,-62,83,-64,-66,-63,-61,-65,-70,157,-73,157,157,-69,127,127,127,127,83,127,127,127,127,-77,-76,-60,-71,-72,-98,83,127,83,83,83,127,127,127,83,127,83,127,83,127,83,127,]),'L_BRACKET':([9,14,17,19,24,25,60,113,151,164,169,171,182,],[-9,-10,-11,-8,31,33,33,33,31,180,180,180,180,]),'RED':([198,],[200,]),'COMMA':([34,77,78,79,80,85,107,113,115,123,125,128,130,131,132,153,154,155,156,159,160,178,],[-14,112,-67,-74,-75,-15,-13,-15,-68,-70,-73,-69,-91,-90,161,-77,-76,-60,-71,-72,-98,161,]),'IF':([31,180,],[67,67,]),'G_THAN_EQUALS':([34,78,79,80,84,85,107,113,115,123,125,128,153,154,156,159,],[-14,-67,-74,-75,122,-15,-13,-15,-68,-70,-73,-69,-77,-76,-71,-72,]),'$end':([1,41,],[0,-1,]),'FUNCTION':([3,],[4,]),'G_THAN':([34,78,79,80,84,85,107,113,115,123,125,128,153,154,156,159,],[-14,-67,-74,-75,116,-15,-13,-15,-68,-70,-73,-69,-77,-76,-71,-72,]),'FINISH':([30,90,],[41,-20,]),'STRING':([3,29,31,111,112,],[14,14,14,14,14,]),'FOR':([31,180,],[49,49,]),'VAR_IDENTIFIER':([2,4,5,9,12,14,16,17,18,19,20,21,22,31,40,42,53,68,71,73,74,81,82,83,86,88,89,91,92,93,94,97,98,99,100,101,103,116,117,118,119,120,121,122,124,126,127,137,157,158,161,165,174,175,176,180,195,199,202,206,209,],[3,23,-19,-9,25,-10,-18,-11,26,-8,27,28,-17,60,77,-15,95,105,-15,-15,-15,113,-15,-15,-80,-15,-15,130,-15,134,135,138,139,-15,-15,-15,-15,-62,-15,-64,-66,-63,-61,-65,-15,-15,-15,167,-79,-78,130,182,-15,-15,-15,60,198,-15,-15,-15,-15,]),'EQUALS':([25,32,34,35,36,37,44,50,60,63,64,65,66,96,107,148,149,150,196,200,205,208,],[-15,71,-14,73,74,75,89,94,97,99,100,101,102,137,-13,174,175,176,199,202,206,209,]),'PAINT':([31,180,],[68,68,]),'ADD':([60,],[98,]),'L_THAN':([34,78,79,80,84,85,107,113,115,123,125,128,153,154,156,159,],[-14,-67,-74,-75,121,-15,-13,-15,-68,-70,-73,-69,-77,-76,-71,-72,]),'ELSIF':([104,173,183,197,],[146,146,-82,-23,]),'IN':([134,],[165,]),'Y':([31,34,78,79,80,85,107,109,113,115,123,125,128,153,154,155,156,159,160,180,],[63,-14,-67,-74,-75,-15,-13,149,-15,-68,-70,-73,-69,-77,-76,-60,-71,-72,-98,63,]),'X':([27,31,180,],[36,64,64,]),'HEIGHT':([31,34,78,79,80,85,107,108,113,115,123,125,128,153,154,155,156,159,160,180,188,],[65,-14,-67,-74,-75,-15,-13,148,-15,-68,-70,-73,-69,-77,-76,-60,-71,-72,-98,65,196,]),'RECTANGLE':([3,31,],[16,16,]),'CENTER':([28,31,180,],[37,66,66,]),'BLUE':([34,78,79,80,85,107,113,115,123,125,128,153,154,155,156,159,160,207,],[-14,-67,-74,-75,-15,-13,-15,-68,-70,-73,-69,-77,-76,-60,-71,-72,-98,208,]),'CANVAS':([3,31,],[18,18,]),'INT_VAL':([33,],[72,]),'INT':([3,29,31,111,112,],[19,19,19,19,19,]),'NOT_EQUALS':([34,78,79,80,84,85,107,113,115,123,125,128,153,154,156,159,],[-14,-67,-74,-75,118,-15,-13,-15,-68,-70,-73,-69,-77,-76,-71,-72,]),'RETURNS':([76,],[111,]),'L_THAN_EQUALS':([34,78,79,80,84,85,107,113,115,123,125,128,153,154,156,159,],[-14,-67,-74,-75,119,-15,-13,-15,-68,-70,-73,-69,-77,-76,-71,-72,]),'L_PAR':([23,42,46,47,67,71,73,74,82,83,88,89,91,92,94,99,100,101,103,116,117,118,119,120,121,122,124,126,127,137,146,161,174,175,176,199,202,206,209,],[29,82,91,92,103,82,82,82,82,82,82,82,82,82,82,82,82,82,82,-62,82,-64,-66,-63,-61,-65,82,82,82,82,103,82,82,82,82,82,82,82,82,]),'EACH':([49,],[93,]),'CIRCLE':([3,31,],[22,22,]),'MAIN':([6,7,8,10,11,13,15,34,78,79,80,85,90,106,107,113,115,123,125,128,153,154,155,156,159,160,177,187,194,203,210,],[-48,-47,24,-49,-46,-2,-3,-14,-67,-74,-75,-15,-20,-12,-13,-15,-68,-70,-73,-69,-77,-76,-60,-71,-72,-98,-4,-50,-54,-16,-97,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'list_index':([25,60,113,],[32,96,153,]),'point':([3,31,75,],[6,6,110,]),'conditional_else':([145,],[170,]),'conditional':([31,180,],[43,43,]),'factor_sign':([42,71,73,74,82,83,88,89,91,92,94,99,100,101,103,117,124,126,127,137,161,174,175,176,199,202,206,209,],[81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,]),'shape':([3,31,],[7,7,]),'globals':([3,],[8,]),'null':([25,29,42,60,71,73,74,82,83,85,88,89,91,92,94,99,100,101,103,104,112,113,117,124,126,127,132,137,145,161,173,174,175,176,178,180,199,202,206,209,],[34,39,86,34,86,86,86,86,86,125,86,86,86,86,86,86,86,86,86,147,39,34,86,86,86,86,162,86,172,86,147,86,86,86,162,191,86,86,86,86,]),'exp_ops':([84,],[117,]),'print_b':([91,161,],[132,178,]),'print_a':([132,178,],[163,189,]),'canvas':([3,31,],[10,10,]),'var_assignment':([31,180,],[48,48,]),'function_arguments':([29,112,],[38,152,]),'paint':([31,180,],[51,51,]),'program':([0,],[1,]),'statement':([31,180,],[56,192,]),'factor':([42,71,73,74,82,83,88,89,91,92,94,99,100,101,103,117,124,126,127,137,161,174,175,176,199,202,206,209,],[85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,]),'print':([31,180,],[61,61,]),'type':([3,29,31,111,112,],[12,40,12,151,40,]),'function':([3,],[13,]),'for_loop':([31,180,],[54,54,]),'conditional_elsif':([104,173,],[145,185,]),'return':([31,180,],[55,55,]),'point_assignment':([31,180,],[52,52,]),'while_loop':([31,180,],[57,57,]),'read':([31,180,],[58,58,]),'assignment':([31,180,],[59,59,]),'factor_id':([42,71,73,74,82,83,88,89,91,92,94,99,100,101,103,117,124,126,127,137,161,174,175,176,199,202,206,209,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'factor_exp':([42,71,73,74,82,83,88,89,91,92,94,99,100,101,103,117,124,126,127,137,161,174,175,176,199,202,206,209,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'var':([3,31,],[11,11,]),'term_loop':([85,],[123,]),'declaration':([3,31,],[15,62,]),'block_contains':([180,],[190,]),'color':([186,201,],[194,203,]),'term':([42,71,73,74,82,83,88,89,91,92,94,99,100,101,103,117,124,126,127,137,161,174,175,176,199,202,206,209,],[78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,156,159,160,78,78,78,78,78,78,78,78,78,]),'var_equals':([137,],[166,]),'block_with_declaration':([24,151,],[30,177,]),'canvas_assignment':([31,180,],[70,70,]),'shape_type':([3,31,],[21,21,]),'declaration_type':([31,],[45,]),'conditional_if':([67,146,],[104,173,]),'exp':([42,71,73,74,82,83,88,89,91,92,94,99,100,101,103,117,137,161,174,175,176,199,202,206,209,],[84,84,84,84,84,115,128,84,84,84,84,84,84,84,84,155,84,84,84,84,84,84,84,84,84,]),'shape_assignment':([31,180,],[69,69,]),'expression':([42,71,73,74,82,89,91,92,94,99,100,101,103,137,161,174,175,176,199,202,206,209,],[87,106,108,109,114,129,131,133,136,140,141,142,144,168,131,186,187,188,201,204,207,210,]),'block':([164,169,171,182,],[181,183,184,193,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM VAR_IDENTIFIER globals MAIN block_with_declaration FINISH','program',6,'p_program_syntax','grammar.py',10),
  ('globals -> function','globals',1,'p_globals','grammar.py',15),
  ('globals -> declaration','globals',1,'p_globals','grammar.py',16),
  ('function -> FUNCTION VAR_IDENTIFIER L_PAR function_arguments R_PAR RETURNS type block_with_declaration','function',8,'p_function','grammar.py',21),
  ('function_arguments -> type VAR_IDENTIFIER','function_arguments',2,'p_function_arguments','grammar.py',26),
  ('function_arguments -> type VAR_IDENTIFIER COMMA function_arguments','function_arguments',4,'p_function_arguments','grammar.py',27),
  ('function_arguments -> null','function_arguments',1,'p_function_arguments','grammar.py',28),
  ('type -> INT','type',1,'p_type','grammar.py',33),
  ('type -> DEC','type',1,'p_type','grammar.py',34),
  ('type -> STRING','type',1,'p_type','grammar.py',35),
  ('type -> YESNO','type',1,'p_type','grammar.py',36),
  ('var -> type VAR_IDENTIFIER list_index EQUALS expression','var',5,'p_var','grammar.py',41),
  ('list_index -> L_BRACKET INT_VAL R_BRACKET','list_index',3,'p_list_index','grammar.py',46),
  ('list_index -> null','list_index',1,'p_list_index','grammar.py',47),
  ('null -> <empty>','null',0,'p_null','grammar.py',51),
  ('shape -> shape_type VAR_IDENTIFIER CENTER EQUALS point WIDTH EQUALS expression HEIGHT EQUALS expression color','shape',12,'p_shape','grammar.py',56),
  ('shape_type -> CIRCLE','shape_type',1,'p_shape_type','grammar.py',61),
  ('shape_type -> RECTANGLE','shape_type',1,'p_shape_type','grammar.py',62),
  ('shape_type -> TRIANGLE','shape_type',1,'p_shape_type','grammar.py',63),
  ('block_with_declaration -> L_BRACKET declaration_type R_BRACKET','block_with_declaration',3,'p_block_with_declaration','grammar.py',68),
  ('declaration_type -> statement','declaration_type',1,'p_declaration_type','grammar.py',73),
  ('declaration_type -> declaration','declaration_type',1,'p_declaration_type','grammar.py',74),
  ('block -> L_BRACKET block_contains R_BRACKET','block',3,'p_block','grammar.py',79),
  ('block_contains -> statement','block_contains',1,'p_block_contains','grammar.py',84),
  ('block_contains -> null','block_contains',1,'p_block_contains','grammar.py',85),
  ('statement -> assignment','statement',1,'p_statement','grammar.py',90),
  ('statement -> conditional','statement',1,'p_statement','grammar.py',91),
  ('statement -> print','statement',1,'p_statement','grammar.py',92),
  ('statement -> for_loop','statement',1,'p_statement','grammar.py',93),
  ('statement -> while_loop','statement',1,'p_statement','grammar.py',94),
  ('statement -> paint','statement',1,'p_statement','grammar.py',95),
  ('statement -> read','statement',1,'p_statement','grammar.py',96),
  ('statement -> return','statement',1,'p_statement','grammar.py',97),
  ('assignment -> var_assignment','assignment',1,'p_assignment','grammar.py',102),
  ('assignment -> shape_assignment','assignment',1,'p_assignment','grammar.py',103),
  ('assignment -> point_assignment','assignment',1,'p_assignment','grammar.py',104),
  ('assignment -> canvas_assignment','assignment',1,'p_assignment','grammar.py',105),
  ('var_assignment -> VAR_IDENTIFIER list_index EQUALS var_equals','var_assignment',4,'p_var_assignment','grammar.py',110),
  ('var_equals -> expression','var_equals',1,'p_var_equals','grammar.py',115),
  ('var_equals -> VAR_IDENTIFIER','var_equals',1,'p_var_equals','grammar.py',116),
  ('shape_assignment -> VAR_IDENTIFIER EQUALS VAR_IDENTIFIER','shape_assignment',3,'p_shape_assignment','grammar.py',121),
  ('shape_assignment -> CENTER EQUALS POINT','shape_assignment',3,'p_shape_assignment','grammar.py',122),
  ('shape_assignment -> WIDTH EQUALS expression','shape_assignment',3,'p_shape_assignment','grammar.py',123),
  ('shape_assignment -> HEIGHT EQUALS expression','shape_assignment',3,'p_shape_assignment','grammar.py',124),
  ('shape_assignment -> COLOR EQUALS VAR_IDENTIFIER','shape_assignment',3,'p_shape_assignment','grammar.py',125),
  ('declaration -> var','declaration',1,'p_declaration','grammar.py',130),
  ('declaration -> shape','declaration',1,'p_declaration','grammar.py',131),
  ('declaration -> point','declaration',1,'p_declaration','grammar.py',132),
  ('declaration -> canvas','declaration',1,'p_declaration','grammar.py',133),
  ('point -> POINT VAR_IDENTIFIER X EQUALS expression Y EQUALS expression','point',8,'p_point','grammar.py',138),
  ('point_assignment -> VAR_IDENTIFIER EQUALS VAR_IDENTIFIER','point_assignment',3,'p_point_assignment','grammar.py',143),
  ('point_assignment -> X EQUALS expression','point_assignment',3,'p_point_assignment','grammar.py',144),
  ('point_assignment -> Y EQUALS expression','point_assignment',3,'p_point_assignment','grammar.py',145),
  ('canvas -> CANVAS VAR_IDENTIFIER WIDTH EQUALS expression HEIGHT EQUALS expression color','canvas',9,'p_canvas','grammar.py',150),
  ('canvas_assignment -> VAR_IDENTIFIER ADD VAR_IDENTIFIER','canvas_assignment',3,'p_canvas_assignment','grammar.py',155),
  ('canvas_assignment -> VAR_IDENTIFIER EQUALS VAR_IDENTIFIER','canvas_assignment',3,'p_canvas_assignment','grammar.py',156),
  ('canvas_assignment -> WIDTH EQUALS expression','canvas_assignment',3,'p_canvas_assignment','grammar.py',157),
  ('canvas_assignment -> HEIGHT EQUALS expression','canvas_assignment',3,'p_canvas_assignment','grammar.py',158),
  ('canvas_assignment -> COLOR EQUALS expression','canvas_assignment',3,'p_canvas_assignment','grammar.py',159),
  ('expression -> exp exp_ops exp','expression',3,'p_expression','grammar.py',164),
  ('exp_ops -> L_THAN','exp_ops',1,'p_exp_ops','grammar.py',169),
  ('exp_ops -> G_THAN','exp_ops',1,'p_exp_ops','grammar.py',170),
  ('exp_ops -> EQUALS_EQUALS','exp_ops',1,'p_exp_ops','grammar.py',171),
  ('exp_ops -> NOT_EQUALS','exp_ops',1,'p_exp_ops','grammar.py',172),
  ('exp_ops -> G_THAN_EQUALS','exp_ops',1,'p_exp_ops','grammar.py',173),
  ('exp_ops -> L_THAN_EQUALS','exp_ops',1,'p_exp_ops','grammar.py',174),
  ('exp -> term','exp',1,'p_exp','grammar.py',179),
  ('exp -> PLUS exp','exp',2,'p_exp','grammar.py',180),
  ('exp -> MINUS exp','exp',2,'p_exp','grammar.py',181),
  ('term -> factor term_loop','term',2,'p_term','grammar.py',186),
  ('term_loop -> DIV term','term_loop',2,'p_term_loop','grammar.py',191),
  ('term_loop -> MULT term','term_loop',2,'p_term_loop','grammar.py',192),
  ('term_loop -> null','term_loop',1,'p_term_loop','grammar.py',193),
  ('factor -> factor_id','factor',1,'p_factor','grammar.py',198),
  ('factor -> factor_exp','factor',1,'p_factor','grammar.py',199),
  ('factor_id -> L_PAR expression R_PAR','factor_id',3,'p_factor_id','grammar.py',204),
  ('factor_exp -> factor_sign VAR_IDENTIFIER list_index','factor_exp',3,'p_factor_exp','grammar.py',209),
  ('factor_sign -> MINUS','factor_sign',1,'p_factor_sign','grammar.py',214),
  ('factor_sign -> PLUS','factor_sign',1,'p_factor_sign','grammar.py',215),
  ('factor_sign -> null','factor_sign',1,'p_factor_sign','grammar.py',216),
  ('conditional -> IF conditional_if conditional_elsif conditional_else','conditional',4,'p_conditional','grammar.py',222),
  ('conditional_if -> L_PAR expression R_PAR block','conditional_if',4,'p_conditional_if','grammar.py',227),
  ('conditional_elsif -> ELSIF conditional_if conditional_elsif','conditional_elsif',3,'p_conditional_elsif','grammar.py',232),
  ('conditional_elsif -> null','conditional_elsif',1,'p_conditional_elsif','grammar.py',233),
  ('conditional_else -> ELSE block','conditional_else',2,'p_conditional_else','grammar.py',238),
  ('conditional_else -> null','conditional_else',1,'p_conditional_else','grammar.py',239),
  ('print -> PRINT L_PAR print_b print_a R_PAR','print',5,'p_print','grammar.py',244),
  ('print_a -> COMMA print_b print_a','print_a',3,'p_print_a','grammar.py',249),
  ('print_a -> null','print_a',1,'p_print_a','grammar.py',250),
  ('print_b -> expression','print_b',1,'p_print_b','grammar.py',255),
  ('print_b -> VAR_IDENTIFIER','print_b',1,'p_print_b','grammar.py',256),
  ('read -> READ VAR_IDENTIFIER','read',2,'p_read','grammar.py',261),
  ('paint -> PAINT VAR_IDENTIFIER','paint',2,'p_paint','grammar.py',266),
  ('return -> RETURN expression','return',2,'p_return','grammar.py',271),
  ('for_loop -> FOR EACH VAR_IDENTIFIER IN VAR_IDENTIFIER block','for_loop',6,'p_for_loop','grammar.py',276),
  ('while_loop -> WHILE L_PAR expression R_PAR block','while_loop',5,'p_while_loop','grammar.py',281),
  ('color -> COLOR VAR_IDENTIFIER RED EQUALS expression GREEN EQUALS expression BLUE EQUALS expression','color',11,'p_color','grammar.py',286),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','grammar.py',290),
]