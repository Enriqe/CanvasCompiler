from semantic_helper import type_dict

from classes.semantic_helper import type_converter

"""
ActivationRecords manages the memory of th functions calls during execution.
It contains a local and temporal memory, both which are filled during initialization
"""
class ActivationRecord:

    #Inicializa los tamaños de las memorias locales y temporales de la funcion
    def __init__(self, local_map, temp_map):
        self.local_mem = {}
        self.temp_mem = {}
        self.return_index = -1
        self.return_address = -1
        for key in type_dict:
            self.local_mem[key] = [None] * local_map[key]
            self.temp_mem[key] = [None] * temp_map[key]

    #Returns the value of the address from the correct memory
    def get_val(self, address):
        scope = address[0]
        type1 = type_converter[address[1:3]]
        addr = int(address[3:])
        if (scope == 'g' or scope == 'l'):
            return self.local_mem[type1][addr]
        elif (scope == 't'):
            return self.temp_mem[type1][addr]
        return 1

    #Decomposes de address and set its content to value
    def set_val(self, address, value):
        scope = address[0]
        type1 = type_converter[address[1:3]]
        addr = int(address[3:])
        if (scope == 'g' or scope == 'l'):
            self.local_mem[type1][addr] = value
        elif (scope == 't'):
            self.temp_mem[type1][addr] = value

    def set_return_address(self, address):
        self.return_address = address

    def get_return_address(self):
        return self.return_address

    def set_return_index(self, index):
        self.return_index = index

    def get_return_index(self):
        return self.return_index
