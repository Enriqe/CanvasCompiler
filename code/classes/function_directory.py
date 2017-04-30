import csv
from function import Function

class FunctionDirectory:

    ## http://code.activestate.com/recipes/66531/
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state
        self.global_function = Function("globals")
        self.functions = {}
        self.current_function = 0

    def get_global_function(self):
        return self.global_function

    def add_function(self, function):
        if function.name in self.functions:
            print "function exists"
            #todo: throw Error
        else:
            function.id = self.current_function
            self.current_function = self.current_function + 1
            self.functions[function.name] = function

    def get_function(self, func_name):
        if func_name in self.functions:
            return self.functions[func_name]

    def add_var_to_FunctionDirectory(self, var):
        if (self.current_function == var.function):
            print "todo"

    def print_dir(self):
        self.global_function.print_function()
        for key, val in self.functions.iteritems():
            val.print_function()

    def finish(self):
        with open("../output.csv", "a") as file1:
            writer = csv.writer(file1, delimiter=' ')
            writer.writerow([self.global_function.name, self.global_function.type])
            writer.writerow([self.global_function.local_map.types])
            writer.writerow([self.global_function.temp_map.types])
            for key, function in self.functions.iteritems():
                writer.writerow([function.name, function.type])
                writer.writerow([function.local_map.types])
                writer.writerow([function.temp_map.types])