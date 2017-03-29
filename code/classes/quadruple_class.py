class Quadruple:

    def __init__(self, left_op = "", right_op = "", operator = ""):
        self.left_operand = left_op
        self.right_operand = right_op 
        self.operator = operator

    '''
    generate_quad:
    Validates (with semantic cube) and performs corresponding operation and returns result

    '''
    def generate_quad(self, left_opnd, right_opnd, op):
        
