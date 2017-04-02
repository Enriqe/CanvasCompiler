class Quadruple:

    def __init__(self, operator = "", left_op = "", right_op = "", mem_count = 0):
        #TODO CHECK IF FIXABLE
        if(operator != "="):
            self.mem_count = mem_count
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
        
        #TODO
        if(self.operator == '='):
            result = self.right_operand

        return result
        
