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
temp_args_count = 0
curr_calling_function = ''

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
    program : PROGRAM VAR_IDENTIFIER program_start globals globals_finished functions MAIN main_start main_block FINISH
    '''
    function_dir.print_dir()
    quad_controller.print_quads()
    quad_controller.finish()
    function_dir.finish()
    memory_controller.print_const_memory()

def p_program_start(p):
    '''
    program_start :
    '''
    quad_controller.program_start()

def p_main_start(p):
    '''
    main_start :
    '''
    quad_controller.main_start()

def p_globals(p):
    '''
    globals : declaration globals
            | null
    '''
    global temp_function
    if(p[1]):
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

def p_function(p):
    '''
    function : FUNCTION VAR_IDENTIFIER L_PAR function_arguments R_PAR RETURNS type function_return_address L_BRACKET count_function block_declarations block_statements return R_BRACKET finished_function
    '''
    global temp_function
    temp_function = Function()

def p_function_arguments(p):
    '''
    function_arguments : type VAR_IDENTIFIER push_argument
                       | type VAR_IDENTIFIER push_argument COMMA function_arguments
                       | null
    '''
    if(p[1]):
        virt_address = p[3]
        tempVar = Var(p[2], p[1], "", virt_address)
        temp_function.add_variable(tempVar)
        temp_function.signature.insert(0, virt_address)

def p_push_argument(p):
    '''
    push_argument :
    '''
    virt_address = memory_controller.generate_var_address(ALLOC_SCOPE, p[-2])
    p[0] = virt_address

def p_function_return_address(p):
    '''
    function_return_address :
    '''
    global temp_function
    temp_function.name = p[-6]
    temp_function.type = p[-1]
    temp_function.local_map = memory_controller.get_local_map()
    temp_function.temp_map = memory_controller.get_temp_map()
    temp_function.virt_address = memory_controller.generate_var_address('g', temp_function.type)
    globalfunc = function_dir.get_global_function()
    func_var = Var(temp_function.name, temp_function.type, "", temp_function.virt_address)
    globalfunc.add_variable(func_var)
    globalfunc.local_map.types[temp_function.type] += 1

    function_dir.add_function(temp_function)

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
    var : type VAR_IDENTIFIER list_index push_operand EQUALS push_operator expression
    '''
    virt_address = p[4]
    tempVar = Var(p[2], p[1], p[7], virt_address) 
    if p[3]:
        tempVar.size = int(p[3])
    p[0] = tempVar

def p_list_index(p):
    '''
    list_index : L_BRACKET INT_VAL R_BRACKET
               | null
    '''
    if p[1]:
        p[0] = p[2]

def p_null(p):
    '''
    null :
    '''
    p[0] = None

def p_shape(p):
    '''
    shape : shape_type VAR_IDENTIFIER left_exp_par expression shape_comma expression shape_comma expression shape_comma expression right_exp_par colors
    '''
    # ^         ^           ^          ^      ^     
    #p[0]      p[1]        p[2]       p[3]   p[4]   
    shape_type = p[1]
    shape_id = p[2]
    shape_h = quad_controller.after_array_check()
    shape_w = quad_controller.after_array_check()
    quad_controller.pop_fake_bottom()
    shape_y = quad_controller.after_array_check()
    shape_x = quad_controller.after_array_check()
    quad_controller.pop_fake_bottom()
    quad_controller.pop_fake_bottom()
    shape_values = [shape_x, shape_y]
    shape_color = p[12]
    addr = memory_controller.generate_var_address(ALLOC_SCOPE, shape_type)
    tempVar = Var(shape_id, shape_type, shape_values, addr)
    p[0] = tempVar
    quad_controller.create_shape(addr, shape_x, shape_y, shape_w, shape_h, shape_type, shape_color)

def p_colors(p):
    '''
    colors : RED
          | GREEN
          | BLUE
          | BROWN
    '''
    p[0] = p[1]

def p_shape_comma(p):
    '''
    shape_comma : COMMA
    '''
    quad_controller.read_fake_bottom()


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
    temp_function.type = "int"
    temp_function.local_map = memory_controller.get_local_map()
    temp_function.temp_map = memory_controller.get_temp_map()
    temp_function.virt_address = memory_controller.generate_var_address('g', temp_function.type)
    function_dir.add_function(temp_function)

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
              | shape
              | read
    '''


def p_assignment(p):
    '''
    assignment : VAR_IDENTIFIER assignment_push_operand assignment_a finished_expression
    '''

def p_assignment_push_operand(p):
    '''
    assignment_push_operand :
    '''
    # TODO put this in a method \/\/\/\/\/
    global temp_function
    if p[-1] not in temp_function.variables:
        aux_function = function_dir.get_global_function()
    else:
        aux_function = temp_function
    if p[-1] not in aux_function.variables:
        #TODO throw ERROR if var is not foudn in global or local scope
        print "Error. variable not found: " + p[-1] +" at line " + str(error_line(p))
        exit(1)

    # TODO put this in a method /\/\/\/\/\
    else:
        temp_var = aux_function.variables[p[-1]]
        var_type = temp_var.type
        quad_controller.read_type(var_type)
        quad_controller.read_operand(temp_var.virt_address)

def p_assignment_a(p):
    '''
    assignment_a : EQUALS push_operator expression
                 | var_assignment
                 | point_assignment
                 | shape_or_canvas_assignment
    '''

def p_var_assignment(p):
    '''
    var_assignment : list_index_exp EQUALS push_operator expression
    '''

def p_list_index_exp(p):
    '''
    list_index_exp : l_index_bracket expression r_index_bracket
                   | null
    '''
    if p[1]:
        p[0] = p[2]

        global temp_function
        if p[-2] not in temp_function.variables:
            aux_function = function_dir.get_global_function()
        else:
            aux_function = temp_function
        if p[-2] not in aux_function.variables:
            print "Error. variable not found: " + str(p[-2]) +" at line " + str(error_line(p))
            exit(1)
        temp_var = aux_function.variables[p[-2]] 
        index = quad_controller.after_array_check()
        temp_address = memory_controller.get_temp_address(temp_var.type)
        temp_address = "*" + temp_address
        quad_controller.array_access(index, temp_var.size, temp_var.virt_address, temp_address)
        quad_controller.read_operand(temp_address)
        quad_controller.read_type(temp_var.type)

def p_l_index_bracket(p):
    '''
    l_index_bracket : L_BRACKET
    '''
    p[0] = p[1]
    quad_controller.read_fake_bottom()

def p_r_index_bracket(p):
    '''
    r_index_bracket : R_BRACKET
    '''
    quad_controller.pop_fake_bottom()

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
                                 | COLOR EQUALS expression
    '''

def p_shape_assignment(p):
    '''
    shape_assignment : CENTER EQUALS POINT
    '''

def p_declaration(p):
    '''
    declaration : var
                | point
                | canvas
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
    addr = memory_controller.generate_var_address(ALLOC_SCOPE, 'point')
    tempVar = Var(point_id, var_type, point_values, addr)
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
    canvas : CANVAS VAR_IDENTIFIER 
    '''
    #TODO add virt_address
    addr = memory_controller.generate_var_address(ALLOC_SCOPE, 'canvas')
    tempVar = Var(p[2], p[1], "", addr)
    p[0] = tempVar
    quad_controller.create_canvas()

def p_canvas_assignment(p):
    '''
    canvas_assignment : ADD VAR_IDENTIFIER
    '''

def p_expression(p):
    '''
    expression : expression_a finished_expression
    '''
    p[0] = p[1]

def p_expression_a(p):
    '''
    expression_a : exp after_exp_check expression_b
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
           | factor_value
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


def p_factor_value(p):
    '''
    factor_value : factor_var
                 | factor_num
                 | factor_yesno
                 | factor_string
    '''
    p[0] = p[1]

def p_factor_num(p):
    '''
    factor_num : factor_sign factor_num_a
    '''
    if(p[1] == "-"):
        p[0] = int(p[2]) * -1
    else:
        p[0] = p[2]

def p_factor_num_a(p):
    '''
    factor_num_a : factor_int
                 | factor_dec
    '''
    p[0] = p[1]

def p_factor_sign(p):
    '''
    factor_sign : MINUS
                | PLUS
                | null
    '''
    p[0] = p[1]

def p_factor_var(p):
    '''
    factor_var : VAR_IDENTIFIER function_call list_index_exp 
    '''

def p_function_call(p):
    '''
    function_call : left_exp_par init_function_call calling_args right_exp_par function_gosub
                  | null
    '''
    if(not p[1]):
        # p[0] = p[1]
        # TODO put this in a method \/\/\/\/\/
        global temp_function
        if p[-1] not in temp_function.variables:
            aux_function = function_dir.get_global_function()
        else:
            aux_function = temp_function
        if p[-1] not in aux_function.variables:
            raise NameError("Var not defined: ", p[-1])
            print "VAR NOT FOUND - factorvar"
        # TODO put this in a method /\/\/\/\/\
        else:
            temp_var = aux_function.variables[p[-1]]
            var_type = temp_var.type
            quad_controller.read_type(var_type)
            quad_controller.read_operand(temp_var.virt_address)


def p_init_function_call(p):
    '''
    init_function_call :
    '''
    global curr_calling_function
    curr_calling_function = p[-2]
    func_name = curr_calling_function
    if (func_name not in function_dir.functions):
        print("Error: function not defined '" +func_name + "'")
        exit(1)
    else :
        quad_controller.function_call_init(func_name)

def p_calling_args(p):
    '''
    calling_args : function_call_param calling_args_a
                 | null
    '''

def p_function_call_param(p):
    '''
    function_call_param : expression
    '''
    global temp_args_count
    aux_function = function_dir.functions[curr_calling_function]
    if (temp_args_count >= len(aux_function.signature)):
        raise AttributeError("Wrong number of arguments in function: ", curr_calling_function) 
    else:
        param_address = aux_function.signature[temp_args_count]
        quad_controller.function_call_param(param_address)
        temp_args_count = temp_args_count + 1

def p_calling_args_a(p):
    '''
    calling_args_a : COMMA calling_args
                   | null
    '''

def p_function_gosub(p):
    '''
    function_gosub :
    '''
    global curr_calling_function
    global temp_args_count
    aux_function = function_dir.functions[curr_calling_function]
    if (temp_args_count != len(aux_function.signature)):
        raise AttributeError("Wrong number of arguments in function: ", curr_calling_function) 
        exit(1)
    else:
        quad_controller.function_gosub(aux_function.virt_address, aux_function.counter)
        curr_calling_function = ''
        temp_args_count = 0

def p_factor_int(p):
    '''
    factor_int : INT_VAL
    '''
    p[0] = p[1]
    if (p[-1] == '-'):
        p[1] = -1 * int(p[1])
    quad_controller.read_type('int')
    virt_address = memory_controller.generate_const_address('int', p[1])
    quad_controller.read_operand(virt_address)

def p_factor_dec(p):
    '''
    factor_dec : DEC_VAL
    '''
    p[0] = p[1]
    quad_controller.read_type('dec')
    virt_address = memory_controller.generate_const_address('dec', p[1])
    quad_controller.read_operand(virt_address)

def p_factor_yesno(p):
    '''
    factor_yesno : YESNO_VAL
    '''
    p[0] = p[1]
    quad_controller.read_type('yesno')
    virt_address = memory_controller.generate_const_address('yesno', p[1])
    quad_controller.read_operand(virt_address)

def p_factor_string(p):
    '''
    factor_string : STRING_VAL
    '''
    st1 = p[1]
    p[0] = st1[1:-1]
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
    print : PRINT left_exp_par expression print_a right_exp_par
    '''

def p_print_a(p):
    '''
    print_a :
    '''
    global temp_function
    quad_controller.print_stmt()

def p_read(p):
    '''
    read : READ VAR_IDENTIFIER
    '''

def p_paint(p):
    '''
    paint : PAINT VAR_IDENTIFIER
    '''
    quad_controller.paint_canvas()


def p_return(p):
    '''
    return : RETURN return_assign expression
           | null
    '''
def p_return_assign(p):
    '''
    return_assign :
    '''
    #TODO CMON GUYS
    quad_controller.read_operand(temp_function.virt_address)
    quad_controller.read_type(temp_function.type)
    quad_controller.read_operator('=')

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
        quad_controller.finished_operand(temp_address, ops, error_line(p))

def p_after_term_check(p):
    '''
    after_term_check :
    '''
    ops = ["+", "-"]
    res_type = quad_controller.peek_res_type(ops)
    if res_type != -1:
        temp_address = memory_controller.get_temp_address(res_type)
        quad_controller.finished_operand(temp_address, ops, error_line(p))

# neuralgic point for factors
def p_after_factor_check(p):
    '''
    after_factor_check :
    '''
    ops = ["*", "/"]
    res_type = quad_controller.peek_res_type(ops)
    if res_type != -1:
        temp_address = memory_controller.get_temp_address(res_type)
        quad_controller.finished_operand(temp_address, ops, error_line(p))

def p_push_operand(p):
    '''
    push_operand :
    '''
    var_name = p[-2]
    var_type = p[-3]
    if var_name in function_dir.global_function.variables:
        raise NameError("Name already defined", var_name)
    else:
        if p[-1]: #array definition
            virt_address = memory_controller.generate_arr_address(ALLOC_SCOPE, var_type, p[-1])
        else:
            virt_address = memory_controller.generate_var_address(ALLOC_SCOPE, var_type)
        quad_controller.read_operand(virt_address)
        quad_controller.read_type(var_type)
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
    quad_controller.finished_expression(error_line(p))

def p_finished_function(p):
    '''
    finished_function :
    '''
    quad_controller.finished_function()

def p_count_function(p):
    '''
    count_function :
    '''
    temp_function.counter = quad_controller.quad_counter

# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input line: " + str(p.lexer.lineno)
    print "Unexpected token: " + str(p.value)
    sys.exit(0)

def error_line(p):
    return p.lexer.lineno - 1

# Build the parser
log = logging.getLogger()
parser = yacc.yacc(debug=True, debuglog=log)

if __name__ == '__main__':

    if (len(sys.argv) > 1) : fin = sys.argv[1]
    else : fin = 'input.in'

    f = open(fin, 'r')
    data = f.read()

    parser.parse(data, debug=log)

    print("Successful")
