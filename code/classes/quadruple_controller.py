from quadruple import Quadruple

# priority = {
#         '=' : 0,
#         'and' : 1,
#         'or' : 1,
#         '>' : 2,
#         '<' : 2,
#         '>=' : 2,
#         '<=' : 2,
#         '!=' : 2,
#         '==' : 2,
#         '+' : 3,
#         '-' : 3,
#         '*' : 4,
#         '/' : 4,
#         '(' : 5,
#         ')' : 5
#         }

# def has_higher_priority(op1, op2):
#     return priority[op1] > priority[op2]

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

            self.quad_list.append(res)
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





    # '''
    # read_operator:
    # Reads current operator in expression and performs corresponding operation
    # @param current_op: char of operator that is currently being read
    # '''
    # def read_operator(self, current_op):
    #     # checks if operator_stack is empty
    #     if len(self.operator_stack) == 0:
    #         self.operator_stack.append(current_op)
    #     else:
    #         prev_op = self.operator_stack[-1]

    #         #TODO: create a priority list/dict/enum/w.e. to compare priorities between ops
    #         if(has_higher_priority(prev_op, current_op)):
    #             # loop through operator_stack while a higher-priority operator than the current_op
    #             # is found
    #             while(has_higher_priority(prev_op, current_op) and len(self.operator_stack) > 0):
    #                 #TODO: should we check for a uniary operator?

    #                 # Pops from stacks and generates Quad
    #                 temp_op = self.operator_stack.pop()
    #                 right_opnd = self.operand_stack.pop()
    #                 left_opnd = self.operand_stack.pop()

    #                 #TODO: create generate_quad() method
    #                 temp_quad = Quadruple(left_opnd, right_opnd, temp_op)
    #                 result = temp_quad.generate_quad()

    #                 #TODO: check if result is valid
    #                 if result:
    #                     self.operand_stack.append(result)
    #                     self.quad_list.append(temp_quad)
    #                 else:
    #                     print "ERROR, operation not valid"

    #                 prev_op = self.operator_stack[-1]

    #         self.operator_stack.append(current_op)


    # '''
    # finished_expression:
    # To be ran when expression is finished. Empties both operator_stack and operand_stack
    # and generates corresponding quadruples.


    # '''
    # def finished_expression(self):
    #     #TODO: check for equals sign
    #     prev_op = self.operator_stack[-1]
    #     while( len(self.operator_stack) > 0 and prev_op != '='):
    #         # Pops from stacks and generates Quad
    #         temp_op = self.operator_stack.pop()
    #         right_opnd = self.operand_stack.pop()
    #         left_opnd = self.operand_stack.pop()

    #         #TODO: create generate_quad() method
    #         temp_quad = Quadruple(left_opnd, right_opnd, temp_op)
    #         result = temp_quad.generate_quad()

    #         #TODO: check if result is valid
    #         if result:
    #             self.operand_stack.append(result)
    #             self.quad_list.append(temp_quad)
    #         else:
    #             #TODO: call error exit
    #             print "ERROR, operation not valid"

    #         prev_op = self.operator_stack[-1]

    #     if(prev_op == '='):
    #         operand = self.operand_stack.pop()
    #         op = self.operator
    #         temp_quad = Quadruple(left_opnd, "", operand)
