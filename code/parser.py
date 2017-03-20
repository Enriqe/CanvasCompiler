import scanner as scanner
import ply.yacc as yacc
import sys
import logging
# Get the token map from the lexer.  This is required.
from scanner import tokens
from classes.var_class import Var
from classes.function_class import Function
from classes.function_directory_class import FunctionDirectory

function_dir = FunctionDirectory()
temp_function = function_dir.global_function

logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)

def p_program_syntax(p):
    '''
    program : PROGRAM VAR_IDENTIFIER globals functions MAIN block_with_declaration FINISH
    '''
    function_dir.print_dir()
    print("hello")

def p_globals(p):
    '''
    globals : declaration globals
            | null
    '''
    print("P_GLOBALS")
    if(p[1] == None):
        temp_function = Function()
    else:
        temp_function.add_variable(p[1])

def p_functions(p):
    '''
    functions : function functions
              | null
    '''
    print("P_FUNCTIONS")
    temp_function = Function()
    if(p[1] == None):
        temp_function.name = "main"
    else:
        temp_function.name = p[1]

    function_dir.add_function(temp_function)


def p_function(p):
    '''
    function : FUNCTION VAR_IDENTIFIER L_PAR function_arguments R_PAR RETURNS type block_with_declaration
    '''
    print("P_FUNCTION")
    # todo: check what to return here
    p[0] = p[2]
    #todo: add name and type to function table

def p_function_arguments(p):
    '''
    function_arguments : type VAR_IDENTIFIER
                       | type VAR_IDENTIFIER COMMA function_arguments
                       | null
    '''

def p_type(p):
    '''
    type : INT
         | DEC
         | STRING
         | YESNO
    '''
    p[0] = p[1]

def p_var(p):
    '''
    var : type VAR_IDENTIFIER list_index EQUALS expression
    '''  
    tempVar = Var(p[2], p[1], p[5])
    p[0] = tempVar

    #todo: add type, name, and value of var to var table

def p_list_index(p):
    '''
    list_index : L_BRACKET INT_VAL R_BRACKET
               | null
    '''
def p_null(p):
    '''
    null :
    '''
    p[0] = None

def p_shape(p):
    '''
    shape : shape_type VAR_IDENTIFIER CENTER EQUALS VAR_IDENTIFIER WIDTH EQUALS expression HEIGHT EQUALS expression COLOR EQUALS VAR_IDENTIFIER
    '''
    #todo: add type, name, and value of var to var table

def p_shape_type(p):
    '''
    shape_type : CIRCLE
               | RECTANGLE
               | TRIANGLE
    '''

def p_block_with_declaration(p):
    '''
    block_with_declaration : L_BRACKET statement_type R_BRACKET
    '''

def p_statement_type(p):
    '''
    statement_type : statement statement_type
                     | declaration statement_type
                     | null
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
              | for_loop
              | while_loop
              | paint
              | read
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
    shape_assignment : VAR_IDENTIFIER shape_assignment_b 
    '''

def p_shape_assignment_b(p):
    '''
    shape_assignment_b : EQUALS VAR_IDENTIFIER
                       | CENTER EQUALS POINT
                       | WIDTH EQUALS expression
                       | HEIGHT EQUALS expression
                       | COLOR EQUALS VAR_IDENTIFIER
    '''

def p_declaration(p):
    '''
    declaration : var
                | shape
                | point
                | canvas
                | color
    '''
    p[0] =  p[1]

def p_point(p):
    '''
    point : POINT VAR_IDENTIFIER X EQUALS expression Y EQUALS expression
    '''
    #todo: add type, name, and value of var to var table

def p_point_assignment(p):
    '''
    point_assignment : VAR_IDENTIFIER point_assignment_b 
    '''

def p_point_assignment_b(p):
    '''
    point_assignment_b : EQUALS VAR_IDENTIFIER
                       | X EQUALS expression
                       | Y EQUALS expression
    '''

def p_canvas(p):
    '''
    canvas : CANVAS VAR_IDENTIFIER WIDTH EQUALS expression HEIGHT EQUALS expression COLOR EQUALS VAR_IDENTIFIER
    '''
    #todo: add type, name, and value of var to var table

def p_canvas_assignment(p):
    '''
    canvas_assignment : VAR_IDENTIFIER canvas_assignemnt_b 
    '''

def p_canvas_assignemnt_b(p):
    '''
    canvas_assignemnt_b : ADD VAR_IDENTIFIER
                        | EQUALS VAR_IDENTIFIER
                        | WIDTH EQUALS expression
                        | HEIGHT EQUALS expression
                        | COLOR EQUALS expression
    '''

def p_expression(p):
    '''
    expression : exp exp_ops exp
               | exp
    '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        print("else of p_expression")

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
    p[0] = p[1]
    
def p_term(p):
    '''
    term : factor term_loop
    '''
    p[0] = p[1]

def p_term_loop(p):
    '''
    term_loop : DIV term
              | MULT term
              | null
    '''

def p_factor(p):
    '''
    factor : factor_id
           | factor_exp
    '''
    p[0] = p[1]

def p_factor_id(p):
    '''
    factor_id : L_PAR expression R_PAR
    '''

def p_factor_exp(p):
    '''
    factor_exp : factor_sign factor_value list_index
    '''
    if(p[1] == None):
        p[0] = p[2]
    else:
        print "in"
        p[0] = p[2] * -1


def p_factor_sign(p):
    '''
    factor_sign : MINUS
                | PLUS
                | null
    '''
    p[0] = p[1]

def p_factor_value(p):
    '''
    factor_value : VAR_IDENTIFIER
                 | INT_VAL
                 | DEC_VAL
                 | YESNO_VAL
    '''
    p[0] = p[1]

def p_conditional(p):
    '''
    conditional : IF conditional_if conditional_elsif conditional_else
    '''

def p_conditional_if(p):
    '''
    conditional_if : L_PAR expression R_PAR block
    '''

def p_conditional_elsif(p):
    '''
    conditional_elsif : ELSIF conditional_if conditional_elsif
                      | null
    '''

def p_conditional_else(p):
    '''
    conditional_else : ELSE block
                     | null
    '''

def p_print(p):
    '''
    print : PRINT L_PAR print_b print_a R_PAR
    '''

def p_print_a(p):
    '''
    print_a : COMMA print_b print_a
            | null
    '''

def p_print_b(p):
    '''
    print_b : expression
            | VAR_IDENTIFIER
    '''

def p_read(p):
    '''
    read : READ VAR_IDENTIFIER
    '''

def p_paint(p):
    '''
    paint : PAINT VAR_IDENTIFIER
    '''

def p_return(p):
    '''
    return : RETURN expression
    '''

def p_for_loop(p):
    '''
    for_loop : FOR EACH VAR_IDENTIFIER IN VAR_IDENTIFIER block
    '''

def p_while_loop(p):
    '''
    while_loop : WHILE L_PAR expression R_PAR block
    '''

def p_color(p):
    '''
    color : COLOR VAR_IDENTIFIER RED EQUALS expression GREEN EQUALS expression BLUE EQUALS expression
    '''
    #todo: add type, name, and value of var to var table

# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input line: " + str(p.lexer.lineno)
    print "Unexpected token: " + str(p.value)
    sys.exit(0)

# Build the parser
log = logging.getLogger()
parser = yacc.yacc(debug=True, debuglog=log)

if __name__ == '__main__':

    if (len(sys.argv) > 1) : fin = sys.argv[1]
    else : fin = 'input.in'

    f = open(fin, 'r')
    data = f.read()
    # print data
    # print "End of file"

    parser.parse(data, debug=log)
    # parser.parse(data, tracking=True)

    print("Successful")
