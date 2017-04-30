from semantic_helper import type_dict
from classes.semantic_helper import type_converter

class ActivationRecord:
    local_mem = {}
    temp_mem = {}
    return_index = -1
    return_address = -1

    def __init__(local_map, temp_map):
        for key in type_dict:
            local_mem[key] = [None] * local_map[key]
            temp_mem[key] = [None] * temp_map[key]

    def get_val(address):
        scope = address[0]
        type1 = type_converter[address[1:3]]
        addr = int(address[3:])
        #TODO USE TYPE CONVERTER TO GET VAL
        #IF g OR l RETURN FROM LOCAL
        #IF t RETURN FROM TEMP
        if (scope == 'g' or scope == 'l'):
            return local_mem[type1][addr]
        elif (scope == 't'):
            return temp_mem[type1][addr]
        return -1

    def set_val(address, value):
        scope = address[0]
        type1 = type_converter[address[1:3]]
        addr = int(address[3:])
        #TODO USE TYPE CONVERTER TO GET VAL
        if (scope == 'g' or scope == 'l'):
            local_mem[type1][addr] = value
        elif (scope == 't'):
            temp_mem[type1][addr] = value

    def set_return_address(address):
        return_address = address

    def get_return_address():
        return return_address

    def set_return_index(address):
        return_address = address

    def get_return_index():
        return return_index
