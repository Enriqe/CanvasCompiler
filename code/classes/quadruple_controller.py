import csv
from quadruple import Quadruple
from memory_map import MemoryMap
from memory_controller import MemoryController
from semantic_cube import SemanticCube
import semantic_helper
from memory_controller import MemoryController

TEMP_SEGMENT = "3" # flag used to segment memory between scopes

def debug(right, right_type, left, left_type, op):
        print("DEBUGGING")
        print(right)
        print(right_type)
        print(left)
        print(left_type)
        print(op)
'''
QuadrupleController manages quadruple creation, quaduple filling, jump stack, 
operator stack, type stack, and operand stack. It keeps count of the quads that 
are being added to the quad list
'''
class QuadrupleController:
    quad_list = []
    operator_stack = []
    operand_stack = []
    type_stack = []
    jump_stack = []
    avail = 0
    fake_bottom = '('
    quad_counter = 0
    memory_controller = MemoryController()

    # Adds quadruple to list of quadruples
    def add_quadruple(self, quad):
        self.quad_list.append(quad)
        self.quad_counter = self.quad_counter + 1

    # Reads an operator while pushing it to the operator stack
    def read_operator(self, current_op):
        self.operator_stack.append(current_op)

    #Reads an operand and pushes it to the operand stack
    def read_operand(self, current_opnd):
        self.operand_stack.append(current_opnd)

    # Reads at the same time as an operand, pushes its type to the type stack
    def read_type(self, type):
        self.type_stack.append(type)

    # Pushes a fake bottom to the operator stack. Used for list index and func calling args
    def read_fake_bottom(self):
        self.operator_stack.append(self.fake_bottom)

    # Pops fake bottom from stack
    def pop_fake_bottom(self):
        self.operator_stack.pop()

    # Fills a quad given its location in the list, with its quad_num
    def fill(self, loc, quad_num):
        quad = self.quad_list[loc]
        quad.add_location(quad_num)
        self.quad_list[loc] = quad

    # runs after an expression is finished, performs corresponding operation depending on the operator and operands in the stacks
    def finished_expression(self, lineno):
        if(len(self.operator_stack) > 0 and self.operator_stack[-1] != '('):
            right_opnd = self.operand_stack.pop()
            left_opnd = self.operand_stack.pop()
            equals_op = self.operator_stack.pop()
            right_opnd_type = semantic_helper.type_dict[self.type_stack.pop()]
            left_opnd_type = semantic_helper.type_dict[self.type_stack.pop()]
            res_type = SemanticCube[left_opnd_type][right_opnd_type][semantic_helper.operator_dict[equals_op]]
            if res_type != -1:
                quad = Quadruple(equals_op, right_opnd, "", left_opnd)
                self.add_quadruple(quad)
            else:
                print("ERROR: type mismatch, line " + str(lineno))
                exit()

    # pushes endproc quad to quad list
    def finished_function(self):
        #quad = self.quad_list[-1] # peek last quad before return
        quad = Quadruple("ENDPROC")
        self.add_quadruple(quad)

    # pushes era quad to quad list
    def function_call_init(self, virt_address):
        quad = Quadruple("ERA", virt_address)
        self.add_quadruple(quad)

    # pushes param list to quads
    def function_call_param(self, param_address):
        val_address = self.operand_stack.pop()
        val_type = self.type_stack.pop()
        param_type = semantic_helper.type_converter[param_address[1:3]]
        if (val_type == param_type):
            quad = Quadruple("PARAM", val_address, '', param_address)
            self.add_quadruple(quad)

    # generates gosub quadruple
    def function_gosub(self, virt_address, jump_to_function_index):
        quad = Quadruple("GOSUB", virt_address, '', jump_to_function_index)
        self.add_quadruple(quad)

    # generates quads belonging to array accessing
    def array_access(self, index, arr_size, base_address, next_temp):
        quad = Quadruple("VER", "", index, arr_size)
        self.add_quadruple(quad)
        quad = Quadruple("ADDBASE", index, base_address, next_temp)
        self.operand_stack.pop()
        self.type_stack.pop()
        self.add_quadruple(quad)

    # pops from stacks unwanted base address of array
    def after_array_check(self):
        self.type_stack.pop()
        return self.operand_stack.pop()

################### Canvas Custom Operations ###################

    # prints a statment
    def print_stmt(self):
        addr = self.operand_stack.pop()
        self.type_stack.pop()
        quad = Quadruple("PRINT", "", "", addr)
        self.add_quadruple(quad)

    # generates main quad for later filling
    def program_start(self):
        quad = Quadruple("MAIN")
        self.add_quadruple(quad)
        self.jump_stack.append(self.quad_counter - 1)

    # main quad is now filled with index of quad where main function starts
    def main_start(self):
        main_quad_index = self.jump_stack.pop()
        self.fill(main_quad_index, self.quad_counter)
    
    # generates quad for canvas
    def create_canvas(self):
        quad = Quadruple("CANVAS")
        self.add_quadruple(quad)

    # genertes quad for paint
    def paint_canvas(self):
        quad = Quadruple("PAINT")
        self.add_quadruple(quad)

    # generates quad for shapes
    def create_shape(self, addr, x, y, width, height, shape_type, shape_color):
        if shape_type == "circle":
            quad = Quadruple("CIRCLE", addr, x, y)
            quad2 = Quadruple("CIRC2", addr, width, height)
            quad3 = Quadruple("CIRC3", shape_color)
        elif shape_type == "rectangle":
            quad = Quadruple("RECTANGLE", addr, x, y)
            quad2 = Quadruple("RECT2", addr, width, height)
            quad3 = Quadruple("RECT3", shape_color)
        self.add_quadruple(quad)
        self.add_quadruple(quad2)
        self.add_quadruple(quad3)


################### Conditionals ###################

    def finished_conditional(self): #f finished condition
        end = self.jump_stack.pop()
        self.fill(end, self.quad_counter)

    # after condition expression quad
    def after_cond_expression(self):
        res = self.operand_stack.pop()
        self.type_stack.pop()
        quad = Quadruple("GOTOF", res)
        self.add_quadruple(quad)
        self.jump_stack.append(self.quad_counter - 1)

    #after else if condition expression quad
    def after_elsif_expression(self):
        wait = self.jump_stack.pop()
        jump = self.jump_stack.pop()
        self.fill(jump, self.quad_counter)
        self.jump_stack.append(wait)

    # after else condition expression quad
    def after_else(self):
        quad = Quadruple("GOTO")
        self.add_quadruple(quad)
        false = self.jump_stack.pop()
        self.fill(false, self.quad_counter)
        self.jump_stack.append(self.quad_counter - 1)

    def before_while(self):
        self.jump_stack.append(self.quad_counter)

    def after_while(self):
        end = self.jump_stack.pop()
        jump = self.jump_stack.pop()
        quad = Quadruple("GOTO", "", "", jump)
        self.add_quadruple(quad)
        self.fill(end, self.quad_counter)

####################################################

    def print_quads(self):
        counter = 0
        for q in self.quad_list:
            q.print_quad(counter)
            counter = counter + 1

    '''
    finished_operand:
    Runs after an operand is read. Checks in the operator_stack if the top
    operator is in the same priority level and genereates quad
    @param operators: List of operators of the priority level we are at
    '''
    def finished_operand(self, temp_address, operators, lineno):
        # checks if operator_stack is not empty and top operator is in current priority level
        if(len(self.operator_stack) > 0 and self.operator_stack[-1] in operators):
            curr_op = self.operator_stack.pop()
            right_opnd = self.operand_stack.pop()
            left_opnd = self.operand_stack.pop()
            left_opnd_type = semantic_helper.type_dict[self.type_stack.pop()]
            right_opnd_type = semantic_helper.type_dict[self.type_stack.pop()]
            res_type = SemanticCube[left_opnd_type][right_opnd_type][semantic_helper.operator_dict[curr_op]]
            if res_type != -1:
                self.operand_stack.append(temp_address)
                self.type_stack.append(res_type)
                quad = Quadruple(curr_op, left_opnd, right_opnd, temp_address)
                self.add_quadruple(quad)
            else:
                #TODO add error handler, print line no. and two operand mismatches
                print("ERROR: type mismatch, line " + str(lineno))
                exit()

    def finish(self):
        with open("../output.csv", "w+") as file1:
            writer = csv.writer(file1, delimiter=' ', quotechar='|')
            for q in self.quad_list:
                writer.writerow([q.operator, q.left_operand, q.right_operand, q.result])

    # Used in parser for temp vars
    def peek_res_type(self, operators):
        if(len(self.operator_stack) > 0 and self.operator_stack[-1] in operators):
            curr_op = self.operator_stack[-1]
            left_opnd_type = semantic_helper.type_dict[self.type_stack[-1]]
            right_opnd_type = semantic_helper.type_dict[self.type_stack[-1]]
            return SemanticCube[left_opnd_type][right_opnd_type][semantic_helper.operator_dict[curr_op]]
        return -1
