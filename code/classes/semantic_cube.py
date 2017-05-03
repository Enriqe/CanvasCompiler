from semantic_helper import *

# http://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
# Cube initialization
SemanticCube = [[[-1 for j in range(len(operator_dict))] for k in range(len(type_dict))] for m in range(len(type_dict))]

math_opers = ['+', '-', '*', '/']

for op in math_opers:
    SemanticCube[type_dict['int']][type_dict['int']][operator_dict[op]] = 'int'
    SemanticCube[type_dict['dec']][type_dict['dec']][operator_dict[op]] = 'dec'
    SemanticCube[type_dict['dec']][type_dict['int']][operator_dict[op]] = 'dec'
    SemanticCube[type_dict['int']][type_dict['dec']][operator_dict[op]] = 'dec'

comp_opers = ['<', '>', '<=', '>=', '!=', '==']

for op in comp_opers:
    SemanticCube[type_dict['int']][type_dict['int']][operator_dict[op]] = 'yesno'
    SemanticCube[type_dict['dec']][type_dict['dec']][operator_dict[op]] = 'yesno'
    SemanticCube[type_dict['dec']][type_dict['int']][operator_dict[op]] = 'yesno'
    SemanticCube[type_dict['int']][type_dict['dec']][operator_dict[op]] = 'yesno'

for t in type_dict:
    SemanticCube[type_dict[t]][type_dict[t]][operator_dict['=']] = t
SemanticCube[type_dict['dec']][type_dict['int']][operator_dict['=']] = 'dec'

# OPTIONAL
SemanticCube[type_dict['string']][type_dict['string']][operator_dict['+']] = 'string'

for op in ['!=', '==']:
    SemanticCube[type_dict['string']][type_dict['string']][operator_dict[op]] = 'yesno'
    SemanticCube[type_dict['yesno']][type_dict['yesno']][operator_dict[op]] = 'yesno'

# TESTS
#if (SemanticCube[type_dict['string']][type_dict['string']][operator_dict['+']] != type_dict['string']): print("ERROR 1")
#if (SemanticCube[type_dict['string']][type_dict['string']][operator_dict['-']] != -1): print("ERROR 2")
#if (SemanticCube[type_dict['int']][type_dict['int']][operator_dict['-']] == -1): print("ERROR 3")
#if (SemanticCube[type_dict['int']][type_dict['dec']][operator_dict['<']] == -1): print("ERROR 4")
#if (SemanticCube[type_dict['int']][type_dict['yesno']][operator_dict['*']] != -1): print("ERROR 5")
#if (SemanticCube[type_dict['int']][type_dict['dec']][operator_dict['==']] != type_dict['yesno']): print("ERROR 6")
#if (SemanticCube[type_dict['int']][type_dict['dec']][operator_dict['==']] != type_dict['yesno']): print("ERROR 7")

# SHOULD WE ADD AND and OR?
