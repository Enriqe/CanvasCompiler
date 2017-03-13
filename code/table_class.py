class Table:
    def __init__(self):
        self.functions = {}
        self.current_function = 0
    
    def add_function(function):
        if function.name in self.functions:
            #todo: throw Error
        else:
            function.id = self.current_function
            self.current_function = self.current_function + 1
            self.functions[function.name] = function


    
    def add_var_to_table(var):
        if (self.current_function == var.function)
