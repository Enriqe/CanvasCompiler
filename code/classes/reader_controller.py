from cuadruple import Quadruple

class ReaderController:
    quad_list = []
    operator_stack = []
    operand_stack = []

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
            top_op = self.operator_stack[-1]

            #TODO: create a priority list/dict/enum/w.e. to compare priorities between ops
            if(priority[current_op] > priority[top_op]):
                self.operator_stack.append(current_op)
            else:
                # loop through operator_stack while a higher-priority operator than the current_op
                # is found
                while(priority[top_op] > priority[current_op] and len(self.operator_stack) > 0):
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

                    top_op = self.operator_stack[-1]

                # TODO: clean up this mess
                self.operator_stack.append(current_op)


    '''
    finished_expression:
    To be ran when expression is finished. Empties both operator_stack and operand_stack
    and generates corresponding quadruples.


    '''
    def finished_expression(self):
        #TODO: check for equals sign
        top_op = self.operator_stack[-1]
        while( len(self.operator_stack) > 0 and top_op != '='):
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
            top_op = self.operator_stack[-1]

        if(top_op == '='):
            operand = self.operand_stack.pop()
            op = self.operator
            temp_quad = Quadruple(left_opnd, "", operand)
