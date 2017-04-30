import scanner as scanner
import ply.yacc as yacc
import sys
import logging
# Get the token map from the lexer.
from scanner import tokens
from classes.var import Var
from classes.function import Function
from classes.function_directory import FunctionDirectory
from classes.quadruple_controller import QuadrupleController
from classes.memory_controller import MemoryController
from classes.semantic_helper import type_dict
from classes.semantic_helper import operator_dict
from classes.memory_map import MemoryMap

ALLOC_SCOPE = "g" # flag used to segment memory between scopes

function_dir = FunctionDirectory()
temp_function = Function()
quad_controller = QuadrupleController()
memory_controller = MemoryController()
temp_args = []

logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)

##############################################
############# PARSER FUNCTIONS ###############
##############################################

def p_program_syntax(p):
    '''
    program : PROGRAM VAR_IDENTIFIER globals globals_finished functions MAIN main_block FINISH
    '''
    function_dir.print_dir()
    #TODO DELETE
    quad_controller.print_quads()
    quad_controller.finish()

def p_globals(p):
    '''
    globals : declaration globals
            | null
    '''
    global temp_function
    if(p[1]):
        print("GLOBALS")
        temp_function = function_dir.get_global_function()
        temp_function.add_variable(p[1])

def p_globals_finished(p):
    '''
    globals_finished :
    '''
    global temp_function, ALLOC_SCOPE
    temp_function.local_map = memory_controller.get_global_map()
    temp_function.temp_map = memory_controller.get_temp_map()
    temp_function = Function()
    memory_controller.clear_local_map()
    memory_controller.clear_temp_map()
    ALLOC_SCOPE = "l" #change to local scope

def p_functions(p):
    '''
    functions : function clear_function_memory functions
              | null
    '''

def p_clear_function_memory(p):
    '''
    clear_function_memory :
    '''
    memory_controller.clear_local_map()
    memory_controller.clear_temp_map()

#TODO add semantic logic to p_function
def p_function(p):
    '''
    function : FUNCTION VAR_IDENTIFIER L_PAR function_arguments R_PAR RETURNS type L_BRACKET count_function block_declarations block_statements R_BRACKET finished_function
    '''
    # todo: check what to return here
    global temp_function
    temp_function.name = p[2]
    temp_function.local_map = memory_controller.get_local_map()
    temp_function.temp_map = memory_controller.get_temp_map()
    function_dir.add_function(temp_function)
    temp_function = Function()

def p_function_arguments(p):
    '''
    function_arguments : type VAR_IDENTIFIER push_operand
                       | type VAR_IDENTIFIER push_operand COMMA function_arguments
                       | null
    '''
    if(p[1]):
        virt_address = p[3]
        tempVar = Var(p[2], p[1], "", virt_address)
        temp_function.add_variable(tempVar)
        temp_function.signature.append(type_dict[p[1]])

def p_type(p):
    '''
    type : INT
         | DEC
         | STRING
         | YESNO
    '''
    p[0] = p[1]

def p_var(p):
    #  WHEN MODYFING RULE : check that p[i] index still calls corresponding argument 
    '''
    var : type VAR_IDENTIFIER push_operand list_index EQUALS push_operator expression
    '''
    # virt_address = memory_controller.generate_var_address(ALLOC_SCOPE, p[1], p[2])
    virt_address = p[3]
    tempVar = Var(p[2], p[1], p[7], virt_address) 
    p[0] = tempVar

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
    # ^         ^           ^          ^      ^          ^          ^     ^       ^         ^       ^        ^       ^     ^          ^          
    #p[0]      p[1]        p[2]       p[3]   p[4]       p[5]      p[6]   p[7]    p[8]      p[9]   p[10]     p[11]   p[12] p[13]      p[14]
    shape_type = p[1]
    shape_id = p[2]
    shape_values = {"center" : p[5], "width" : p[8], "height" : p[11], "color" : p[14]} 
    #TODO add virt_address
    tempVar = Var(shape_id, shape_type, shape_values)
    p[0] = tempVar

def p_shape_type(p):
    '''
    shape_type : CIRCLE
               | RECTANGLE
               | TRIANGLE
    '''
    p[0] = p[1]

def p_main_block(p):
    '''
    main_block : L_BRACKET block_declarations block_statements R_BRACKET
    '''
    temp_function.name = "main"
    temp_function.local_map = memory_controller.get_local_map()
    temp_function.temp_map = memory_controller.get_temp_map()
    # temp_function.add_variable(p[1])
    function_dir.add_function(temp_function)

# def p_block_with_declaration(p):
#     '''
#     block_with_declaration : L_BRACKET statement_type R_BRACKET
#     '''
#     p[0] = p[2]

def p_block_declarations(p):
    '''
    block_declarations : declaration declaration_end block_declarations
                       | null
    '''

def p_declaration_end(p):
    '''
    declaration_end : 
    '''
    temp_function.add_variable(p[-1])

def p_statement_type(p):
    '''
    statement_type : statement statement_type
                     | declaration statement_type
                     | null
    '''
    p[0] = p[1]

def p_block(p):
    '''
    block : L_BRACKET block_statements R_BRACKET
    '''

def p_block_statements(p):
    '''
    block_statements : statement block_statements
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
              | function_call
              | return
    '''

def p_function_call(p):
    '''
    function_call : VAR_IDENTIFIER L_PAR args_list calling_args R_PAR
    '''
    func_name = p[1]
    if (func_name not in function_dir.functions):
        #TODO throw error
        print("ERROR: FUNCTION NOT DEFINED")
    else:
        aux_function = function_dir.functions[func_name]
        quad_controller.function_call(temp_args, func_name, aux_function.signature, aux_function.counter)

#TODO think of cleaner version
def p_args_list(p):
    '''
    args_list : 
    '''
    global temp_args
    temp_args = []

def p_calling_args(p):
    '''
    calling_args : expression calling_args_a
                 | null
    '''
    p[0] = p[1]
    temp_args.insert(0, p[1])

def p_calling_args_a(p):
    '''
    calling_args_a : COMMA calling_args
                   | null
    '''
    if(p[1]):
        p[0] = p[2]

def p_assignment(p):
    '''
    assignment : VAR_IDENTIFIER assignment_push_operand assignment_a finished_expression
    '''

def p_assignment_push_operand(p):
    '''
    assignment_push_operand :
    '''
#TODO throw ERROR if var is not foudn in global or local scope
    global temp_function
    if p[-1] not in temp_function.variables:
        aux_function = function_dir.get_global_function()
    else:
        aux_function = temp_function
    temp_var = aux_function.variables[p[-1]]
    var_type = temp_var.type
    quad_controller.read_type(var_type)
    quad_controller.read_operand(temp_var.virt_address)

def p_assignment_a(p):
    #TODO CHECK IF FIXABLE
    '''
    assignment_a : EQUALS push_operator expression
                 | var_assignment
                 | point_assignment
                 | shape_or_canvas_assignment
                 | canvas_assignment
    '''

def p_var_assignment(p):
    '''
    var_assignment : list_index EQUALS expression
    '''

def p_shape_or_canvas_assignment(p):
    '''
    shape_or_canvas_assignment : shape_or_canvas_assignment_a
                               | shape_assignment
                               | canvas_assignment
    '''
def p_shape_or_canvas_assignment_a(p):
    '''
    shape_or_canvas_assignment_a : WIDTH EQUALS expression
                                 | HEIGHT EQUALS expression
                                 | COLOR EQUALS VAR_IDENTIFIER
    '''

def p_shape_assignment(p):
    '''
    shape_assignment : CENTER EQUALS POINT
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
    #  ^      ^       ^          ^    ^      ^       ^    ^      ^
    # p[0]   p[1]    p[2]      p[3]  p[4]   p[5]    p[6] p[7]   p[8]
    var_type = p[1]
    point_id = p[2]
    point_values = {"x" : p[5], "y" : p[8]}
    #TODO add virt_address
    tempVar = Var(point_id, var_type, point_values)
    p[0] = tempVar

def p_point_assignment(p):
    '''
    point_assignment : point_assignment_b 
    '''

def p_point_assignment_b(p):
    '''
    point_assignment_b : X EQUALS expression
                       | Y EQUALS expression
    '''


def p_canvas(p):
    '''
    canvas : CANVAS VAR_IDENTIFIER WIDTH EQUALS expression HEIGHT EQUALS expression COLOR EQUALS VAR_IDENTIFIER
    '''
    val = { 'width' : p[5], 'height' : p[8], 'color' : p[11] }
    #TODO add virt_address
    tempVar = Var(p[2], p[1], val)
    p[0] = tempVar

def p_canvas_assignment(p):
    '''
    canvas_assignment : ADD VAR_IDENTIFIER
    '''

def p_expression(p):
    '''
    expression : expression_a finished_expression
    '''
    p[0] = p[1]

# def p_debug(p):
#     '''
#     debug :
#     '''
#     print "DEBUGG"
#     print len(quad_controller.operand_stack)

# ADDED so finished_expression only executes once per expression
def p_expression_a(p):
    '''
    expression_a : exp after_exp_check expression_b
                 | null
    '''
    p[0] = p[1]

def p_expression_b(p):
    '''
    expression_b : expression_ops expression_a
                 | null
    '''

def p_expression_ops(p):
    '''
    expression_ops : L_THAN push_operator
                   | G_THAN push_operator
                   | EQUALS_EQUALS push_operator
                   | NOT_EQUALS push_operator
                   | G_THAN_EQUALS push_operator
                   | L_THAN_EQUALS push_operator
    '''

def p_exp(p):
    '''
    exp : term after_term_check exp_a
    '''
    p[0] = p[1]

def p_exp_a(p):
    '''
    exp_a : PLUS push_operator exp
         | MINUS push_operator exp
         | null
    '''

def p_term(p):
    '''
    term : factor after_factor_check term_loop
    '''
    p[0] = p[1]

def p_term_loop(p):
    '''
    term_loop : DIV push_operator term
              | MULT push_operator term
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
    factor_id : left_exp_par expression right_exp_par
    '''

def p_left_exp_par(p):
    '''
    left_exp_par : L_PAR
    '''
    quad_controller.read_fake_bottom()

def p_right_exp_par(p):
    '''
    right_exp_par : R_PAR
    '''
    quad_controller.pop_fake_bottom()

def p_factor_exp(p):
    '''
    factor_exp : factor_sign factor_value list_index
    '''
    if(p[1] == "-"):
        p[0] = p[2] * -1
    else:
        p[0] = p[2]

def p_factor_sign(p):
    '''
    factor_sign : MINUS
                | PLUS
                | null
    '''
    p[0] = p[1]

#since parser pushes everything in p[..] as a string, we have to retrieve type somehow (type_stack in quad_controller)
def p_factor_value(p):
    '''
    factor_value : factor_var
                 | factor_int
                 | factor_dec
                 | factor_yesno
                 | factor_string
    '''
    p[0] = p[1]
    #TODO check if able to integrate to p_push_operand helper function
    # address = memory_controller.get_address(p[1], ALLOC_SCOPE)

def p_factor_var(p):
    '''
    factor_var : VAR_IDENTIFIER
    '''
    p[0] = p[1]
    #TODO throw ERROR if var is not found in global or local scope
    global temp_function
    if p[1] not in temp_function.variables:
        aux_function = function_dir.get_global_function()
    else:
        aux_function = temp_function
    temp_var = aux_function.variables[p[1]]
    var_type = temp_var.type
    quad_controller.read_type(var_type)
    quad_controller.read_operand(temp_var.virt_address)

def p_factor_int(p):
    '''
    factor_int : INT_VAL
    '''
    p[0] = p[1]
    #TODO repeated code
    quad_controller.read_type('int')
    virt_address = memory_controller.generate_const_address('int', p[1])
    quad_controller.read_operand(virt_address)

def p_factor_dec(p):
    '''
    factor_dec : DEC_VAL
    '''
    p[0] = p[1]
    #TODO repeated code
    quad_controller.read_type('dec')
    virt_address = memory_controller.generate_const_address('dec', p[1])
    quad_controller.read_operand(virt_address)

def p_factor_yesno(p):
    '''
    factor_yesno : YESNO_VAL
    '''
    p[0] = p[1]
    #TODO repeated code
    quad_controller.read_type('yesno')
    virt_address = memory_controller.generate_const_address('yesno', p[1])
    quad_controller.read_operand(virt_address)

def p_factor_string(p):
    '''
    factor_string : STRING_VAL
    '''
    p[0] = p[1]
    #TODO repeated code
    quad_controller.read_type('string')
    virt_address = memory_controller.generate_const_address('string', p[1])
    quad_controller.read_operand(virt_address)

def p_conditional(p):
    '''
    conditional : IF conditional_if conditional_elsif conditional_else
    '''

def p_conditional_if(p):
    '''
    conditional_if : L_PAR expression R_PAR after_cond_expression block
    '''

def p_after_cond_expression(p):
    '''
    after_cond_expression :
    '''
    quad_controller.after_cond_expression()

def p_conditional_elsif(p):
    '''
    conditional_elsif : ELSIF after_else conditional_if after_elsif_expression conditional_elsif
                      | null
    '''

def p_after_elsif_expression(p):
    '''
    after_elsif_expression :
    '''
    quad_controller.after_elsif_expression()

def p_conditional_else(p):
    '''
    conditional_else : ELSE after_else block
                     | null
    '''
    quad_controller.finished_conditional()

def p_after_else(p):
    '''
    after_else :
    '''
    quad_controller.after_else()

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
    while_loop : while L_PAR expression R_PAR after_cond_expression block
    '''
    quad_controller.after_while()

def p_while(p):
    '''
    while : WHILE
    '''
    quad_controller.before_while()

def p_color(p):
    '''
    color : COLOR VAR_IDENTIFIER RED EQUALS expression GREEN EQUALS expression BLUE EQUALS expression
    '''
    #todo: add type, name, and value of var to var table
    val = { 'red' : p[5], 'green' : p[8], 'blue' : p[11] }
    #TODO add virt_address
    tempVar = Var(p[2], p[1], val)
    p[0] = tempVar

##############################################
############# HELPER FUNCTIONS ###############
##############################################


# neuralgic point for terms
def p_after_exp_check(p):
    '''
    after_exp_check :
    '''
    ops = ["<", ">", "<=", ">=", "==", "!="] 
    res_type = quad_controller.peek_res_type(ops)
    if res_type != -1:
        temp_address = memory_controller.get_temp_address(res_type)
        quad_controller.finished_operand(temp_address, ops)

def p_after_term_check(p):
    '''
    after_term_check :
    '''
    ops = ["+", "-"]
    res_type = quad_controller.peek_res_type(ops)
    if res_type != -1:
        temp_address = memory_controller.get_temp_address(res_type)
        quad_controller.finished_operand(temp_address, ops)

# neuralgic point for factors
def p_after_factor_check(p):
    '''
    after_factor_check :
    '''
    ops = ["*", "/"]
    res_type = quad_controller.peek_res_type(ops)
    if res_type != -1:
        temp_address = memory_controller.get_temp_address(res_type)
        quad_controller.finished_operand(temp_address, ops)

def p_push_operand(p):
    '''
    push_operand :
    '''
    virt_address = memory_controller.generate_var_address(ALLOC_SCOPE, p[-2], p[-1])
    quad_controller.read_operand(virt_address)
    quad_controller.read_type(p[-2])
    p[0] = virt_address

def p_push_operator(p):
    '''
    push_operator :
    '''
    quad_controller.read_operator(p[-1])

def p_finished_expression(p):
    '''
    finished_expression :
    '''
    quad_controller.finished_expression()

def p_finished_function(p):
    '''
    finished_function :
    '''
    quad_controller.finished_function()

def p_count_function(p):
    '''
    count_function :
    '''
    temp_function.counter = quad_controller.quad_counter #TODO: Verify counter is accurate

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
