# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from calclex import tokens

def p_program_syntax(p):
    '''
    program : PROGRAM VAR_IDENTIFIER globals MAIN block_with_declaration FINISH
    '''

def p_globals(p):
    '''
    globals : function 
            | declaration
    '''

# TODO: define type
def p_var(p):
    '''
    var : type VAR_IDENTIFIER list_index EQUALS expression
    '''  

def p_list_index(p):
    '''
    list_index : L_BRACKET INT_VAL R_BRACKET
               | null
    '''
def p_null(p):
    '''
    null : 
    '''

def p_shape(p):
    '''
    shape : shape_type VAR_IDENTIFIER CENTER EQUALS point WIDTH EQUALS expression HEIGHT EQUALS expression color
    '''

def p_shape_type(p):
    '''
    shape_type : CIRCLE | RECTANGLE | TRIANGLE
    '''

def p_block_with_declaration(p):
    '''
    block_with_declaration : L_BRACKET declaration_type R_BRACKET
    '''

def p_declaration_type(p):
    '''
    declaration_type : statement
                     | declaration
    '''

def p_block(p):
    '''
    block : L_BRACKET block_contains R_BRACKET
    '''

def p_block_contains(p):
    '''
    block_contains : statement
                   | null
    '''

def p_statement(p):
    '''
    statement : assignment
              | conditional
              | print
              | loop
              | paint
              | read
              | comments
              | return
    '''

def p_assignment(p):
    '''
    assignment : var_assignment
               | shape_assignment
               | point_assignment
               | canvas_assignment
    '''

def p_var_assignment(p):
    '''
    var_assignment : VAR_IDENTIFIER list_index EQUALS var_equals
    '''

def p_var_equals(p):
    '''
    var_equals : expression
              | VAR_IDENTIFIER
    '''

def p_shape_assignment(p):
    '''
    shape_assignment : VAR_IDENTIFIER EQUALS VAR_IDENTIFIER
                     | CENTER EQUALS POINT
                     | WIDTH EQUALS EXPRESSION
                     | HEIGHT EQUALS EXPRESSION
                     | COLOR EQUALS VAR_IDENTIFIER
    '''

def p_declaration(p):
    '''
    declaration : var
                | shape
                | point
                | canvas
    '''

def p_point(p):
    '''
    point : POINT VAR_IDENTIFIER X EQUALS expression Y EQUALS expression
    '''

def p_point_assignment(p):
    '''
    point_assignment : VAR_IDENTIFIER EQUALS VAR_IDENTIFIER
                     | X EQUALS EXPRESSION
                     | Y EQUALS EXPRESSION
    '''

def p_canvas(p):
    '''
    canvas : CANVAS VAR_IDENTIFIER WIDTH EQUALS expression HEIGHT EQUALS expression color
    '''

def p_canvas_assignment(p):
    '''
    canvas_assignment : VAR_IDENTIFIER ADD VAR_IDENTIFIER
                      | VAR_IDENTIFIER EQUALS VAR_IDENTIFIER
                      | WIDTH EQUALS EXPRESSION
                      | HEIGHT EQUALS EXPRESSION
                      | COLOR EQUALS EXPRESSION
    '''

def p_expression(p):
    '''
    expression : exp exp_ops exp
    '''

def p_exp_ops(p):
    '''
    exp_ops : L_THAN
            | G_THAN
            | EQUALS_EQUALS
            | NOT_EQUALS
            | G_THAN_EQUALS
            | L_THAN_EQUALS
    '''

def p_exp(p):
    '''
    exp : term
        | PLUS exp
        | MINUS exp
    '''












def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = raw_input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)