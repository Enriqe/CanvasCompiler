class Function:

    def __init__(self, name = "", type = "", vars = {}):
        self.name = name
        self.type = type
        self.vars = vars
        self.id = -1

    def add_variable(self, var):
        if var.name in self.vars:
            #todo: throw error
            print "error"
        else:
            self.vars[var.name] = var
    
    def print_function(self):
        print("Function name", self.name, "Return Value", self.type)
        print("FUNCTION VARIABLES:")
        for key, value in self.vars.iteritems():
            value.print_var()
