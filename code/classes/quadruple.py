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

    def add_location(self, loc):
        self.result = loc

    def print_quad(self, counter = 0):
        try:
            oper = self.operator
        except:
            oper = '__'
        try:
            left = self.left_operand
        except:
            left = '__'
        try:
            right = self.right_operand
        except:
            right = '__'
        try:
            res = self.result
        except:
            res ='__'

        print(counter, oper, left, right, res)

