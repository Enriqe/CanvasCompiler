import semantic_helper
from memory_map import MemoryMap

CONST_SEGMENT   = "4"
TEMP_SEGMENT    = "3"
LOCAL_SEGMENT   = "2"
GLOBAL_SEGMENT  = "1"

class MemoryController:

    temp_memory = MemoryMap()
    local_memory = MemoryMap()
    global_memory = MemoryMap()
    const_memory = MemoryMap()
    
    '''
    string which maps our virtual addresses:

    ADDRESS = MEM_SEGMENT + VAR_TYPE_CODE + SUBINDEX
    e.g. "1int23" is global int at index 23
    '''
    def get_address(self, var_type, var_segment):
        next_avail = 0
        if var_segment == TEMP_SEGMENT:
            next_avail = self.temp_memory.types[var_type]
            self.temp_memory.types[var_type] += 1 # CUANDO SEAN ARRAYS HAY QUE CAMBIARLO
        elif var_segment == GLOBAL_SEGMENT:
            next_avail = self.global_memory.types[var_type]
            self.global_memory.types[var_type] += 1
        elif var_segment == LOCAL_SEGMENT:
            next_avail = self.local_memory.types[var_type]
            self.local_memory.types[var_type] += 1
        return var_segment + str(semantic_helper.type_dict[var_type]) + str(next_avail)

    '''
    string which maps our virtual addresses:

    ADDRESS = MEM_SEGMENT + VAR_TYPE_CODE + SUBINDEX
    e.g. "1023" is global int at index 23
    '''
    def generate_var_address(self, var_segment, var_type, var_name):
        next_avail = 0
        if var_segment == TEMP_SEGMENT:
            next_avail = self.temp_memory.types[var_type]
            self.temp_memory.types[var_type] += 1
        elif var_segment == GLOBAL_SEGMENT:
            next_avail = self.global_memory.types[var_type]
            self.global_memory.types[var_type] += 1
        elif var_segment == LOCAL_SEGMENT:
            next_avail = self.local_memory.types[var_type]
            self.local_memory.types[var_type] += 1
        return var_segment + var_type + str(next_avail)

    # TODO: content is similar to generate_var_address, check for integration
    def generate_const_address(self, const_type, const_value):
        next_avail = self.const_memory.types[const_type]
        self.const_memory.types[const_type] += 1
        return CONST_SEGMENT + const_type + str(next_avail)
    
    def get_temp_address(self, temp_type):
        next_avail = self.temp_memory.types[temp_type]
        # TODO should we have to append something to temp memory???
        self.temp_memory.types[temp_type] += 1
        return TEMP_SEGMENT + temp_type + str(next_avail)

    def print_memory(self):
        print( "CONST-MEM", self.const_memory.types)
        print( "TEMP-MEM", self.temp_memory.types)
        print( "LOCAL-MEM", self.local_memory.types)
        print( "GLOBAL-MEM", self.global_memory.types)
