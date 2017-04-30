from semantic_helper import type_dict

class ActivationRecord:
    local_mem = {}
    temp_mem = {}
    return_index = -1
    return_address = -1

    def __init__(local_map, temp_map):
        for key in type_dict:
            local_mem[key] = [None] * local_map[key]
            temp_mem[key] = [None] * temp_map[key]

    def get_val(ºaddress):
        return 0

    def set_val(address, value):
        return 0

    def set_return_address(address):
        return_address = address

    def get_return_address():
        return return_address

    def set_return_index(address):
        return_address = address

    def get_return_index():
        return return_index
