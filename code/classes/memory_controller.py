import csv
import semantic_helper
from memory_map import MemoryMap
from constants_table import ConstantsTable

CONST_TABLE_BEGIN_FLAG = "BEGINCONSTTABLE"
CONST_SEGMENT   = "c"
TEMP_SEGMENT    = "t"
LOCAL_SEGMENT   = "l"
GLOBAL_SEGMENT  = "g"

class MemoryController:

    temp_memory = MemoryMap()
    local_memory = MemoryMap()
    global_memory = MemoryMap()
    const_memory = ConstantsTable()

    '''
    string which maps our virtual addresses:

    ADDRESS = MEM_SEGMENT + VAR_TYPE_CODE + SUBINDEX
    e.g. "gin23" is global int at index 23
    '''
    def generate_var_address(self, var_segment, var_type):
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
        return var_segment + var_type[0:2] + str(next_avail)

    def generate_arr_address(self, var_segment, var_type, arr_size):
        arr_size = int(arr_size)
        if var_segment == LOCAL_SEGMENT:
            next_avail = self.local_memory.types[var_type]
            self.local_memory.types[var_type] += arr_size
        elif var_segment == GLOBAL_SEGMENT:
            next_avail = self.global_memory.types[var_type]
            self.global_memory.types[var_type] += arr_size
        else:
            raise TypeError("Temp can't be an array")
        return var_segment + var_type[0:2] + str(next_avail)

    # TODO: content is similar to generate_var_address
    # TODO instead of saving a new constant each time, check if it already exists
    def generate_const_address(self, const_type, const_value):
        next_avail = len(self.const_memory.types[const_type])
        self.const_memory.types[const_type].append(const_value)
        return CONST_SEGMENT + const_type[0:2] + str(next_avail)
    
    def get_temp_address(self, temp_type):
        next_avail = self.temp_memory.types[temp_type]
        self.temp_memory.types[temp_type] += 1
        return TEMP_SEGMENT + temp_type[0:2] + str(next_avail)

    def print_memory(self):
        print( "CONST-MEM", self.const_memory.types)
        print( "TEMP-MEM", self.temp_memory.types)
        print( "LOCAL-MEM", self.local_memory.types)
        print( "GLOBAL-MEM", self.global_memory.types)

    def get_local_map(self):
        return self.local_memory
    
    def get_temp_map(self):
        return self.temp_memory
    
    def get_global_map(self):
        return self.global_memory

    def clear_local_map(self):
        self.local_memory = MemoryMap()

    def clear_temp_map(self):
        self.temp_memory = MemoryMap()
    
    def print_const_memory(self):
        with open("../output.csv", "a") as file1:
            writer = csv.writer(file1, delimiter=' ')
            writer.writerow([CONST_TABLE_BEGIN_FLAG])
            writer.writerow([self.const_memory.types])
