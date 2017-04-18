class Function:

    def __init__(self, name = "", type = ""):
        self.name = name
        self.type = type
        self.variables = {}
        self.counter = 0#location of function to store in memory
        self.signature = [] #example of signature: myFunc(int x, dec y) ==> [0, 2]

    def add_variable(self, var):
        if var.name in self.variables:
            #todo: throw error
            print ("Error: , variable", var.name," already defined in this scope")
        else:
            self.variables[var.name] = var

    def print_function(self):
        print("-"*20)
        print("Function name", self.name, "Return Value", self.type)
        for key, value in self.variables.iteritems():
            value.print_var()
