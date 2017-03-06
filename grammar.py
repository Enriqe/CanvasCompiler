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
    block_with_declaration : L_BRACKET statement R_BRACKET
                           | L_BRACKET declaration R_BRACKET
    '''

def p_block(p):

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