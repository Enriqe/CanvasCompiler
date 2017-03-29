class Var:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value 
        
    def print_var(self):
        print("Name", self.name, "Type", self.type, "Value", self.value)
