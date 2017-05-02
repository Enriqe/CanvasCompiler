class Var:
    def __init__(self, name, type, value, virt_address):
        self.name = name
        self.type = type
        self.value = value 
        self.virt_address = virt_address
        self.size = 1
        
    def print_var(self):
        print("Name", self.name, "Type", self.type, "Virt_Address", self.virt_address, "Value", self.value)
