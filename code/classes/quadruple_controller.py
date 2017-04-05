from quadruple import Quadruple
from semantic_cube import SemanticCube

class QuadrupleController:
    quad_list = []
    operator_stack = []
    operand_stack = []
    type_stack = []
    avail = 0
    fake_bottom = '('

    def add_quadruple(self, quad):
        quad_list.append(quad)

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

    def finished_expression(self):
        if(self.operator_stack[-1] == '='):
            right_opnd = self.operand_stack.pop()
            left_opnd = self.operand_stack.pop()
            equals_op = self.operator_stack.pop()
            #TODO do validation of both sides with semantic cube
            # res_type = SemanticCube[left_opnd_type][right_opnd_type]
            quad = Quadruple(equals_op, right_opnd, "", left_opnd)
            res = quad.generate_quad()

            self.quad_list.append(quad)

    def print_quads(self):
        for q in self.quad_list:
            q.print_quad()

    '''
    finished_operand:
    Runs after an operand is read. Checks in the operator_stack if the top
    operator is in the same priority level and genereates quad
    @param operators: List of operators of the priority level we are at
    '''
    def finished_operand(self, operators):
        
        # checks if operator_stack is not empty and top operator is in current priority level
        if(len(self.operator_stack) > 0 and self.operator_stack[-1] in operators):

            # Pops from stacks and generates quad
            self.avail += 1
            result = 't' + str(self.avail)
            curr_op = self.operator_stack.pop()
            right_opnd = self.operand_stack.pop()
            left_opnd = self.operand_stack.pop()

            quad = Quadruple(curr_op, left_opnd, right_opnd, result)

            #TODO: validate with semantic cube before generating quad
            result = quad.generate_quad()

            self.operand_stack.append(result)
            self.quad_list.append(quad)
