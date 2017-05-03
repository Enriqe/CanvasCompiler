from semantic_helper import type_dict

from classes.semantic_helper import type_converter

class ActivationRecord:

    def __init__(self, local_map, temp_map):
        self.local_mem = {}
        self.temp_mem = {}
        self.return_index = -1
        self.return_address = -1
        for key in type_dict:
            self.local_mem[key] = [None] * local_map[key]
            self.temp_mem[key] = [None] * temp_map[key]

    def get_val(self, address):
        #print "GETTING " + address
        scope = address[0]
        type1 = type_converter[address[1:3]]
        addr = int(address[3:])
        if (scope == 'g' or scope == 'l'):
            return self.local_mem[type1][addr]
        elif (scope == 't'):
            return self.temp_mem[type1][addr]
        return 1

    def set_val(self, address, value):
        scope = address[0]
        type1 = type_converter[address[1:3]]
        addr = int(address[3:])
        if (scope == 'g' or scope == 'l'):
            self.local_mem[type1][addr] = value
        elif (scope == 't'):
            self.temp_mem[type1][addr] = value
        #print "SETTING " + address + " WITH " + str(value)
        #print self.local_mem
        #print self.temp_mem

    def set_return_address(self, address):
        self.return_address = address

    def get_return_address(self):
        return self.return_address

    def set_return_index(self, index):
        self.return_index = index

    def get_return_index(self):
        return self.return_index


    #while (foo < 3) [
      #re = arr[foo]
      #foo = foo + 1
      #print(re)
    #]
