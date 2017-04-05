class Quadruple:

    def __init__(self, operator = "", left_op = "", right_op = "", result = ""):
        #TODO CHECK IF FIXABLE
        self.result = result
        self.left_operand = left_op
        self.right_operand = right_op 
        self.operator = operator

    '''
    generate_quad:
    Validates (with semantic cube) and performs corresponding operation and returns result

    '''
    def generate_quad(self):
        #TODO: check if operand is a value or a variable
        if(self.operator == '*'):
            result = float(self.left_operand) * float(self.right_operand)
        if(self.operator == '/'):
            result = float(self.left_operand) / float(self.right_operand)
        if(self.operator == '+'):
            result = float(self.left_operand) + float(self.right_operand)
        if(self.operator == '-'):
            result = float(self.left_operand) - float(self.right_operand)
        if(self.operator == '<'):
            result = float(self.left_operand) < float(self.right_operand)
        if(self.operator == '>'):
            result = float(self.left_operand) > float(self.right_operand)
        if(self.operator == '<='):
            result = float(self.left_operand) <= float(self.right_operand)
        if(self.operator == '>='):
            result = float(self.left_operand) >= float(self.right_operand)
        if(self.operator == '=='):
            result = float(self.left_operand) == float(self.right_operand)
        if(self.operator == '!='):
            result = float(self.left_operand) != float(self.right_operand)
        
        #TODO
        if(self.operator == '='):
            result = self.right_operand

        return result
        
    def print_quad(self):
        oper = self.operator if self.operator else '__'
        left = self.left_operand if self.left_operand else '__'
        right = self.right_operand if self.right_operand else '__'
        res = self.result if self.result else '__'
        print(oper, left, right, res)

