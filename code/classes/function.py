from memory_map import MemoryMap

class Function:

    def __init__(self, name = "", type = "", virt_address = ""):
        self.name = name
        self.type = type
        self.variables = {}
        self.counter = 0#location of function to store in memory
        self.signature = [] #example of signature: myFunc(int x, dec y) ==> [0, 2]
        self.index = -1
        self.virt_address = virt_address
        self.local_map = MemoryMap() # local var memory map
        self.temp_map = MemoryMap() # local temp var memory map

    def add_variable(self, var):
        if var.name in self.variables:
            #todo: throw error
            print ("Error: , variable", var.name," already defined in this scope")
        else:
            self.variables[var.name] = var

    def print_function(self):
        print("-"*20)
        print("Function name", self.name, "Return Value", self.type, "Virt_Addr", self.virt_address)
        print("Local Map", self.local_map.types)
        print("Temp Map", self.temp_map.types)
        for key, value in self.variables.iteritems():
            value.print_var()

    def get_local_map(self):
        return self.local_map

    def get_temp_map(self):
        return self.temp_map
