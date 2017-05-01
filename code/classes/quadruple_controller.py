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

    def add_quadruple(self, quad):
        self.quad_list.append(quad)
        self.quad_counter = self.quad_counter + 1

    def read_operator(self, current_op):
        self.operator_stack.append(current_op)

    def read_operand(self, current_opnd):
        self.operand_stack.append(current_opnd)

    def read_type(self, type):
        self.type_stack.append(type)

    def read_fake_bottom(self):
        self.operator_stack.append(self.fake_bottom)

    def pop_fake_bottom(self):
        self.operator_stack.pop()

    def fill(self, loc, quad_num):
        quad = self.quad_list[loc]
        quad.add_location(quad_num)
        self.quad_list[loc] = quad 

    def finished_expression(self):
        if(len(self.operator_stack) > 0 and self.operator_stack[-1] == '='):
            right_opnd = self.operand_stack.pop()
            left_opnd = self.operand_stack.pop()
            equals_op = self.operator_stack.pop()
            quad = Quadruple(equals_op, right_opnd, "", left_opnd)
            # res = quad.eval_quad()
            self.add_quadruple(quad)

    def finished_function(self):
        quad = self.quad_list[-1] # peek last quad before return
        return_address = quad.get_result()
        quad = Quadruple("RETURN", return_address)
        self.add_quadruple(quad)
        quad = Quadruple("ENDPROC")
        self.add_quadruple(quad)

    def function_call(self, args, virt_address, jump_to_function_index, res_temp_address, res_type):
        num_args = len(args)
        quad = Quadruple("ERA", virt_address)
        self.add_quadruple(quad)
        for arg in args:
            quad = Quadruple("PARAM", arg)
            self.add_quadruple(quad)
        quad = Quadruple("GOSUB", virt_address, res_temp_address, jump_to_function_index)
        self.add_quadruple(quad)
        self.operand_stack.append(res_temp_address)
        self.type_stack.append(res_type)

################### Canvas Custom Operations ###################

    def print_stmt(self, var_id):
        quad = Quadruple("PRINT", "", "", var_id)
        self.add_quadruple(quad)

    def program_start(self):
        quad = Quadruple("MAIN")
        self.add_quadruple(quad)
        self.jump_stack.append(self.quad_counter - 1)

    def main_start(self):
        main_quad_index = self.jump_stack.pop()
        self.fill(main_quad_index, self.quad_counter)

################### Conditionals ###################

    def finished_conditional(self):
        end = self.jump_stack.pop()
        self.fill(end, self.quad_counter)

    def after_cond_expression(self):
        res = self.operand_stack.pop()
        quad = Quadruple("GOTOF", res)
        self.add_quadruple(quad)
        self.jump_stack.append(self.quad_counter - 1)

    def after_elsif_expression(self):
        wait = self.jump_stack.pop()
        jump = self.jump_stack.pop()
        self.fill(jump, self.quad_counter)
        self.jump_stack.append(wait)

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
    def finished_operand(self, temp_address, operators):
        # checks if operator_stack is not empty and top operator is in current priority level
        if(len(self.operator_stack) > 0 and self.operator_stack[-1] in operators):
            curr_op = self.operator_stack.pop()
            right_opnd = self.operand_stack.pop()
            left_opnd = self.operand_stack.pop()
            left_opnd_type = semantic_helper.type_dict[self.type_stack.pop()]
            right_opnd_type = semantic_helper.type_dict[self.type_stack.pop()]
            # print ("DEBUGING")
            # debug(right_opnd, right_opnd_type, left_opnd, left_opnd_type, curr_op)
            res_type = SemanticCube[left_opnd_type][right_opnd_type][semantic_helper.operator_dict[curr_op]]
            if res_type != -1:
                self.operand_stack.append(temp_address)
                self.type_stack.append(res_type)
                quad = Quadruple(curr_op, left_opnd, right_opnd, temp_address)
                self.add_quadruple(quad)
            else:
                #TODO add error handler, print line no. and two operand mismatches
                print("ERROR, type mismatch")

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
