from quadruple import Quadruple
from semantic_cube import SemanticCube
import semantic_helper

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
        self.quad_list[loc] = quad # faltaba actualizar el quad en la lista

    def finished_expression(self):
        if(len(self.operator_stack) > 0 and self.operator_stack[-1] == '='):
            right_opnd = self.operand_stack.pop()
            left_opnd = self.operand_stack.pop()
            equals_op = self.operator_stack.pop()
            quad = Quadruple(equals_op, right_opnd, "", left_opnd)
            res = quad.eval_quad()
            self.add_quadruple(quad)

    def finished_function(self):
        quad = Quadruple("ENDPROC")
        self.add_quadruple(quad)

    def function_call(self, args, name, original_signature, count):
        #TODO check types of args in function call against original_signature

        # print("ARGS", args)
        # print("name", name)
        # print("og", original_signature)
        num_args = len(args)
        quad = Quadruple("ERA", num_args, name)
        self.add_quadruple(quad)
        for arg in args:
            quad = Quadruple("PARAM", arg)
            self.add_quadruple(quad)
        quad = Quadruple("GOSUB", name, count)
        self.add_quadruple(quad)

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
    def finished_operand(self, operators):
        # checks if operator_stack is not empty and top operator is in current priority level
        if(len(self.operator_stack) > 0 and self.operator_stack[-1] in operators):
            # Pops from stacks and evals quad
            self.avail += 1
            result = 't' + str(self.avail)
            curr_op = self.operator_stack.pop()
            right_opnd = self.operand_stack.pop()
            left_opnd = self.operand_stack.pop()
            left_opnd_type = semantic_helper.type_dict[self.type_stack.pop()]
            right_opnd_type = semantic_helper.type_dict[self.type_stack.pop()]
            # debug(right_opnd, right_opnd_type, left_opnd, left_opnd_type, curr_op)

            res_type = SemanticCube[left_opnd_type][right_opnd_type][semantic_helper.operator_dict[curr_op]]
            if res_type != -1:
                quad = Quadruple(curr_op, left_opnd, right_opnd, result)
                result = quad.eval_quad()
                self.operand_stack.append(result)
                self.type_stack.append(res_type)
                self.add_quadruple(quad)
            else:
                #TODO add error handler, print line no. and two operand mismatches
                print("ERROR, type mismatch")
