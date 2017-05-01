import sys
import csv
import ast
from classes.function_directory import FunctionDirectory
from classes.function import Function
from classes.constants_table import ConstantsTable
from classes.quadruple import Quadruple
from classes.semantic_helper import type_converter
from classes.activation_record import ActivationRecord

FUNC_BEGIN_FLAG = "BEGINFUNCTIONS"
CONST_TABLE_BEGIN_FLAG = "BEGINCONSTTABLE"
QUAD_BEGIN_FLAG = "BEGINQUADS"

class VMManager:
    quads = []
    func_dir = FunctionDirectory()
    #TODO TAMAOS DE AR GLOBAL O WATAFAK
    global_mem = None
    const_table = ConstantsTable()
    ar_stack = []

    def init_obj_file(self, file_name):
        row_type = QUAD_BEGIN_FLAG # file always starts with quads
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ')
            for row in reader:
                if row[0] == FUNC_BEGIN_FLAG: # switch type of processing to functions
                    row_type = FUNC_BEGIN_FLAG
                elif row[0] == CONST_TABLE_BEGIN_FLAG: # switch type of processing to read const table
                    row_type = CONST_TABLE_BEGIN_FLAG
                elif row_type == QUAD_BEGIN_FLAG: #processing quad data
                    q = Quadruple(row[0],row[1],row[2],row[3])
                    self.quads.append(q)
                elif row_type == FUNC_BEGIN_FLAG: # processing function data
                    temp_function = Function()
                    temp_function.type = row[1]
                    temp_function.name = row[0]
                    row = reader.next()
                    temp_function.local_map.types = ast.literal_eval(row[0])
                    row = reader.next()
                    temp_function.temp_map.types = ast.literal_eval(row[0])
                    if temp_function.name == "globals":
                        self.func_dir.global_function = temp_function
                    else:
                        self.func_dir.add_function(temp_function)
                elif row_type == CONST_TABLE_BEGIN_FLAG: # reading const table
                    self.const_table.types = ast.literal_eval(row[0])
        #SET GLOBAL MEM
        glob_func = self.func_dir.get_global_function()
        loc = glob_func.get_local_map()
        temp = glob_func.get_temp_map()
        self.global_mem = ActivationRecord(loc, temp)



    def get_quad(self, index):
        return self.quads[index]

    def set_val(self, address, val):
        scope = address[0]
        #TODO TEST IF EXISTS (OR NOT)
        type1 = type_converter[address[1:3]]
        addr = int(address[3:])
        if (scope == 'g'):
            self.global_mem.set_val(address, val)
        elif (scope == 'l'):
            self.ar_stack[-1].set_val(address, val)
        elif (scope == 't'):
            if (len(self.ar_stack) > 0):
                self.ar_stack[-1].set_val(address, val)
            else:
                self.global_mem.set_val(address, val)


    def get_val(self, address):
        #TODO TEST IF EXISTS (OR NOT)
        scope = address[0]
        type1 = type_converter[address[1:3]]
        addr = int(address[3:])
        if (scope == 'g'):
            return self.global_mem.get_val(address)
        elif (scope == 'l'):
            return self.ar_stack[-1].get_val(address)
        elif (scope == 't'):
            if (len(self.ar_stack) > 0):
                return self.ar_stack[-1].get_val(address)
            else:
                return self.global_mem.get_val(address)
        elif (scope == 'c'):
            return self.const_table.types[type1][addr]


    def gen_activation_record(self, func_name):
        func = self.func_dir.get_function(func_name)
        ar = ActivationRecord(func.get_local_map(), func.get_temp_map())
        self.ar_stack.append(ar)

    def add_param(self, address, value):
        #TODO Como saber el address del param
        self.ar_stack[-1].set_val(address, value)

    def call_func(self, ret_address, ret_index):
        self.ar_stack[-1].set_return_index(ret_index)
        self.ar_stack[-1].set_return_address(ret_address)
        return func.index

    def return_func(self):
        #TODO RETURN VALUE SHOULD BE SAVED IN GLOBALS
        print("FIX THIS")

    def end_func(self):
        ar = self.ar_stack.pop()
        next_index = ar.get_return_index()
        ret_addr = ar.get_return_address()
        #TODO SET CORRECT VALUE
        self.set_val(ret_addr, 0)
        return next_index

manager = VMManager()

def run():
    index = 0
    quad = manager.get_quad(index)
    while quad:
        quad.print_quad()
        oper = quad.operator
        left = quad.left_operand
        right = quad.right_operand
        result = quad.result
        if (oper == 'MAIN'):
            manager.gen_activation_record("main")
            index += 1
        elif (oper == 'PRINT'):
            manager.get_val(
        elif (oper == '='):
            val = manager.get_val(left)
            manager.set_val(result, val)
            index += 1
        elif (oper in ['+','-','*','/','<','>','<=','>=','==','!=']):
            left_val = int(manager.get_val(left))
            right_val = int(manager.get_val(right))
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
        elif (oper == 'GOTOF'):
            if (left == 'no'):
                index = int(result)
            else :
                index += 1
        elif (oper == 'GOTO'):
            index = int(result)

        # Check if last quad
        if (index < len(manager.quads)):
            quad = manager.get_quad(index)
        else :
            break

if __name__ == '__main__':

    if (len(sys.argv) > 1) : file1 = sys.argv[1]
    else : file1 = '../output.csv'
    print file1

    manager.init_obj_file(file1)
    manager.func_dir.print_dir()
    print "CONST TABLE:"
    print manager.const_table.types
    run()

    for q in manager.quads:
        q.print_quad()
    # print data
    print "End of file"
    print("Successful")
