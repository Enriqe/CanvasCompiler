class Function:
    def __init__(self, name, type, vars):
        self.name = name
        self.type = type
        self.vars = vars
        self.id = -1

    def add_variable(var):
        if var.name in self.vars:
            #todo: throw error
        else:
            self.vars[var.name] = var