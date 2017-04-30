import sys
import csv
from classes.function_directory import FunctionDirectory
from classes.quadruple import Quadruple
from classes.semantic_helper import type_converter


class VMManager:
    quads = []
    func_dir = FunctionDirectory()
    #TODO TAMAÑOS DE AR GLOBAL O WATAFAK
    global_mem = ActivationRecord()
    #TODO CONSTANTS?
    ar_stack = Stack()

    def init_quads(file_name):
        with open(file_name, 'rb') as fle:
            reader = csv.reader(fle, delimiter=',', quotechar='|')
            for row in reader:
                print row
                q = Quadruple(row[0],row[1],row[2],row[3])
                self.quads.append(q)

    def get_quad(index):
        return self.quads[index]

    def set_val(address, val):
        scope = address[0]
        #TODO TEST IF EXISTS (OR NOT)
        type1 = type_converter[address[1:3]]
        addr = int(address[3:])
        if (scope == 'g'):
            global_mem.set_val(address, val)
        elif (scope == 'l'):
            ar_stack.top().set_val(address, val)
        elif (scope == 't'):
            if (ar_stack.size() > 0):
                ar_stack.top().set_val(address, val)
            else:
                global_mem.set_val(address, val)


    def get_val(address, val):
        scope = address[0]
        #TODO TEST IF EXISTS (OR NOT)
        type1 = type_converter[address[1:3]]
        addr = int(address[3:])
        if (scope == 'g'):
            return global_mem.get_val(address)
        elif (scope == 'l'):
            return ar_stack.top().get_val(address)
        elif (scope == 't'):
            if (ar_stack.size() > 0):
                ar_stack.top().get_val(address)
            else:
                global_mem.get_val(address)

    def gen_activation_record(func_name):
        func = self.func_dir.get_function(func_name)
        ar = ActivationRecord(func.localMap, func.tempMap)
        ar_stack.push(ar)

    def add_param(address, value):
        #TODO Como saber el address del param
        ar_stack.top().set_val(address, value)

    def call_func(ret_address, ret_index):
        ar_stack.top().set_return_index(ret_index)
        ar_stack.top().set_return_address(ret_address)
        return func.index

    def return_func():
        #TODO RETURN VALUE SHOULD BE SAVED IN GLOBALS
        print("FIX THIS")

    def end_func():
        ar = ar_stack.pop()
        next_index = ar.get_return_index()
        ret_addr = ar.get_return_address()
        #TODO SET CORRECT VALUE
        self.set_val(ret_addr, 0)  
        return next_index

manager = VMManager()

def run():
    index = 0
    while quad:
        quad = manager.get_quad(index)
        oper = quad.operator
        left = quad.left_operand
        right = quad.right_operand
        result = quad.result
        if (oper == '='):
            val = manager.get_val(left)
            manager.set_val(result, val)
            index += 1
        elif (oper in ['+','-','*','/','<','>','<=','>=','==','!=']):
            left_val = manager.get_val(left)
            right_val = manager.get_val(right)
            if (oper == '+'):
                manager.set_val(result, left_val + right_val)
            elif (oper == '-'):
                manager.set_val(result, left_val - right_val)
            elif (oper == '*'):
                manager.set_val(result, left_val * right_val)
            elif (oper == '/'):
                manager.set_val(result, left_val / right_val)
            elif (oper == '<'):
                manager.set_val(result, left_val < right_val)
            elif (oper == '>'):
                manager.set_val(result, left_val > right_val)
            elif (oper == '<='):
                manager.set_val(result, left_val <= right_val)
            elif (oper == '>='):
                manager.set_val(result, left_val >= right_val)
            elif (oper == '=='):
                manager.set_val(result, left_val == right_val)
            elif (oper == '!='):
                manager.set_val(result, left_val != right_val)
            else :
                #TODO THROW ERROR
                print("WAIT WAT")
            index += 1
        elif (oper == 'ERA'):
            manager.gen_activation_record(left)
            index += 1
        elif (oper == 'PARAM'):
            left_val = manager.get_val(left)
            manager.add_param(result, left_val)
            index += 1
        elif (oper == 'GOSUB'):
            #TODO CHECK WHY FUNC NAME IS NEEDED IN QUAD
            index = manager.call_func(result, index+1)
        elif (oper == 'ENDPROC'):
            index = manager.end_func()
        #elif (oper == 'GOTOF'):
        #elif (oper == 'GOTOF'):
        #elif (oper == 'GOTO'):

if __name__ == '__main__':

    if (len(sys.argv) > 1) : file1 = sys.argv[1]
    else : file1 = '../output.obj'
    
    manager.init_quads(file1)
    run()

    for q in quads:
        q.print_quad
    # print data
    # print "End of file"
    print("Successful")
