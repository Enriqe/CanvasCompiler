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
    # global_mem = ActivationRecord()
    const_table = ConstantsTable()
    # ar_stack = Stack()

    def print_something(self, string):
        print string

    def init_obj_file(self, file_name):
        row_type = QUAD_BEGIN_FLAG # file always starts with quads
        print "sdf"

        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                print row
                if row[0] == FUNC_BEGIN_FLAG: # switch type of processing to functions
                    row_type = FUNC_BEGIN_FLAG
                    #yield row
                elif row[0] == CONST_TABLE_BEGIN_FLAG: # switch type of processing to read const table
                    row_type = CONST_TABLE_BEGIN_FLAG
                    #yield row
                ##TODO maybe separate into different ifs
                elif row_type == QUAD_BEGIN_FLAG: #processing quad data
                    q = Quadruple(row[0],row[1],row[2],row[3])
                    self.quads.append(q)
                elif row_type == FUNC_BEGIN_FLAG: # processing function data
                    temp_function = Function()
                    temp_function.name = row[0]
                    temp_function.type = row[1]
                    row = reader.next()
                    #yield row # dunno if will work
                    #print "ROWW"
                    temp_function.local_map = ast.literal_eval(row[0])
                    temp_function.print_function()
                    break
                    ## row = reader.next()
                    #yield row
                    #temp_function.temp_map = ast_literal_eval(row)
                    #self.func_dir.add_function(temp_function)
                #elif row_type == CONST_TABLE_BEGIN_FLAG: # reading const table
                    #self.const_table = ast_literal_eval(row)


    # def init_dir_func(file_name):
    #     with open(file_name, 'rb') as file:
    #         reader = csv.reader(file, delimiter=',', quotechar='|')
    #         for row in reader:
    #             if row == CONST_TABLE_BEGIN_FLAG:
    #                 break
    #             print row
    #             temp_function = Function()
    #             temp_function.name = row[0]
    #             temp_function.type = row[1]
    #             # row = reader.next()
    #             yield row
    #             temp_function.local_map = ast_literal_eval(row)
    #             # row = reader.next()
    #             yield row
    #             temp_function.temp_map = ast_literal_eval(row)
    #             self.function_directory.add_function(temp_function)

    # def init_const_table(file_name):
    #     with open(file_name, 'rb') as file:
    #         reader = csv.reader(file, delimiter=',', quotechar='|')
    #         for row in reader:
    #             self.const_table = ast_literal_eval(row)

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
        #TODO TEST IF EXISTS (OR NOT)
        scope = address[0]
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
        elif (oper == 'GOTOF'):
            if (left == 'no'):
                index = int(result)
            else :
                index += 1
        elif (oper == 'GOTO'):
            index = int(result)

if __name__ == '__main__':

    if (len(sys.argv) > 1) : file1 = sys.argv[1]
    else : file1 = '../output.csv'
    print file1

    manager.init_obj_file(file1)
    manager.func_dir.print_dir()
    print manager.const_table.types
    # run()

    # for q in quads:
    #     q.print_quad
    # print data
    # print "End of file"
    print("Successful")
