import semantic_helper

class MemoryController:
    M_TEMP_CODE    = "3"
    M_LOCAL_CODE   = "2"
    M_GLOBAL_CODE  = "1"
    
    '''
    formula to generate our virtual addresses:

    ADDRESS = MEM_SEGMENT + VAR_TYPE_CODE + SUBINDEX
    '''
    def set_address(self, var_type, next_avail):
        return M_TEMP_CODE + str(semantic_helper[var_type]) + str(next_avail)
