from quadruple import Quadruple

class QuadrupleController:
    quad_list = []
    operator_stack = []
    operand_stack = []
    avail = 0

    def add_quadruple(self, quad):
        quad_list.append(quad)

    def read_operator(self, current_op):
        self.operator_stack.append(current_op)

    def read_operand(self, current_opnd):
        self.operand_stack.append(current_opnd)

    def read_equals(self):
        if(len(self.operator_stack) > 0):
            right_opnd = self.operand_stack.pop()
            left_opnd = self.operand_stack.pop()
            sign = self.operator_stack.pop()
            #TODO do validation of both sides with semantic cube
            quad = Quadruple("=", left_opnd, right_opnd)
            res = quad.generate_quad()

            self.quad_list.append(quad)
            for q in self.quad_list:
                print("quad: ", q.operator, q.left_operand, q.right_operand)
            print("ASGN RES", res)
        else:
            self.operator_stack.append("=")
        

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
            mem_count = self.avail
            curr_op = self.operator_stack.pop()
            right_opnd = self.operand_stack.pop()
            left_opnd = self.operand_stack.pop()

            quad = Quadruple(curr_op, left_opnd, right_opnd, mem_count)

            #TODO: validate with semantic cube before generating quad
            result = quad.generate_quad()

            self.operand_stack.append(result)
            self.quad_list.append(quad)