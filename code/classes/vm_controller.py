import semantic_helper

class VMController:
    VM_TEMP_CODE    = "3"
    VM_LOCAL_CODE   = "2"
    VM_GLOBAL_CODE  = "1"
    
    '''
    formula to generate our virtual addresses:

    VIRTUAL_ADDRESS = VM_SEGMENT + VAR_TYPE_CODE + SUBINDEX
    '''
    def set_v_address(self, var_type, next_avail):
        return VM_TEMP_CODE + str(semantic_helper[var_type]) + str(next_avail)
