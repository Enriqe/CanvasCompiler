from function_class import Function

class FunctionDirectory:

    ## http://code.activestate.com/recipes/66531/
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state
        self.global_function = Function()
        self.functions = {}
        self.current_function = 0

    def add_function(self, function):
        if function.name in self.functions:
            print "function exists"
            #todo: throw Error
        else:
            function.id = self.current_function
            self.current_function = self.current_function + 1
            self.functions[function.name] = function
    
    def add_var_to_FunctionDirectory(self, var):
        if (self.current_function == var.function):
            print "todo"

    def print_dir(self):
        for key, val in self.functions.iteritems():
            val.print_function()
