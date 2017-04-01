from quadruple import Quadruple

priority = {
        '=' : 0,
        'and' : 1,
        'or' : 1,
        '>' : 2,
        '<' : 2,
        '>=' : 2,
        '<=' : 2,
        '!=' : 2,
        '==' : 2,
        '+' : 3,
        '-' : 3,
        '*' : 4,
        '/' : 4,
        '(' : 5,
        ')' : 5
        }

def has_higher_priority(op1, op2):
    return priority[op1] > priority[op2]

class QuadrupleController:
    quad_list = []
    operator_stack = []
    operand_stack = []

    def add_quadruple(self, quad):
        quad_list.append(quad)

    def read_operand(self, current_opnd):
        self.operand_stack.append(opnd)

    '''
    read_operator:
    Reads current operator in expression and performs corresponding operation
    @param current_op: char of operator that is currently being read
    '''
    def read_operator(self, current_op):
        # checks if operator_stack is empty
        if len(self.operator_stack) == 0:
            self.operator_stack.append(current_op)
        else:
            prev_op = self.operator_stack[-1]

            #TODO: create a priority list/dict/enum/w.e. to compare priorities between ops
            if(has_higher_priority(prev_op, current_op)):
                # loop through operator_stack while a higher-priority operator than the current_op
                # is found
                while(has_higher_priority(prev_op, current_op) and len(self.operator_stack) > 0):
                    #TODO: should we check for a uniary operator?

                    # Pops from stacks and generates Quad
                    temp_op = self.operator_stack.pop()
                    right_opnd = self.operand_stack.pop()
                    left_opnd = self.operand_stack.pop()

                    #TODO: create generate_quad() method
                    temp_quad = Quadruple(left_opnd, right_opnd, temp_op)
                    result = temp_quad.generate_quad()

                    #TODO: check if result is valid
                    if result:
                        self.operand_stack.append(result)
                        self.quad_list.append(temp_quad)
                    else:
                        print "ERROR, operation not valid"

                    prev_op = self.operator_stack[-1]

            self.operator_stack.append(current_op)

    # to run when expression is finished and empty both stacks ops and oprnds
    def finished_expression(self):
        #TODO: check for equals sign
        prev_op = self.operator_stack[-1]
        while( len(self.operator_stack) > 0 and prev_op != '='):
            # Pops from stacks and generates Quad
            temp_op = self.operator_stack.pop()
            right_opnd = self.operand_stack.pop()
            left_opnd = self.operand_stack.pop()

            #TODO: create generate_quad() method
            temp_quad = Quadruple(left_opnd, right_opnd, temp_op)
            result = temp_quad.generate_quad()

            #TODO: check if result is valid
            if result:
                self.operand_stack.append(result)
                self.quad_list.append(temp_quad)
            else:
                #TODO: call error exit
                print "ERROR, operation not valid"
            prev_op = self.operator_stack[-1]
        if(prev_op == '='):
            operand = self.operand_stack.pop()
            op = self.operator
            temp_quad = Quadruple(left_opnd, "", operand)
