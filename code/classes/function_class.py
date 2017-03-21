class Function:

    def __init__(self, name = "", type = ""):
        print(name)
        self.name = name
        self.type = type
        self.variables = {}
        print("FUNCTION CREATED")

    def add_variable(self, var):
        if var.name in self.variables:
            #todo: throw error
            print "error"
        else:
            self.variables[var.name] = var

    def print_function(self):
        print("-"*20)
        print("Function name", self.name, "Return Value", self.type)
        for key, value in self.variables.iteritems():
            value.print_var()
