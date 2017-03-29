from enum import Enum

type_dict = {
    'int' : 0,
    'string' : 1,
    'dec' : 2,
    'yesno' : 3,
    'point' : 4,
    'triangle' : 5,
    'circle' : 6,
    'rectangle' : 7,
    'canvas' : 8,
    'color' : 9,
}

operator_dict = {
    '+' : 0,
    '-' : 1,
    '*' : 2,
    '/' : 3,
    '<' : 4,
    '>' : 5,
    '<=' : 6,
    '>=' : 7,
    '!=' : 8,
    '==' : 9,
}

# http://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
# Cube initialization
SemanticCube = [[[-1 for j in range(len(type_dict))] for k in range(len(type_dict))] for m in range(len(operator_dict))]

math_opers = ['+', '-', '*', '/']

for op in math_opers:
    SemanticCube[type_dict['int']][type_dict['int']][operator_dict[op]] = type_dict['int']
    SemanticCube[type_dict['dec']][type_dict['dec']][operator_dict[op]] = type_dict['dec']
    SemanticCube[type_dict['dec']][type_dict['int']][operator_dict[op]] = type_dict['dec']
    SemanticCube[type_dict['int']][type_dict['dec']][operator_dict[op]] = type_dict['dec']

comp_opers = ['<', '>', '<=', '>=', '!=', '==']

for op in comp_opers:
    SemanticCube[type_dict['int']][type_dict['int']][operator_dict[op]] = type_dict['yesno']
    SemanticCube[type_dict['dec']][type_dict['dec']][operator_dict[op]] = type_dict['yesno']
    SemanticCube[type_dict['dec']][type_dict['int']][operator_dict[op]] = type_dict['yesno']
    SemanticCube[type_dict['int']][type_dict['dec']][operator_dict[op]] = type_dict['yesno']

# OPTIONAL
SemanticCube[type_dict['string']][type_dict['string']][operator_dict['+']] = type_dict['string']

for op in ['!=', '==']:
    SemanticCube[type_dict['string']][type_dict['string']][operator_dict[op]] = type_dict['yesno']

# TESTS
#if (SemanticCube[type_dict['string']][type_dict['string']][operator_dict['+']] != type_dict['string']): print("ERROR 1")
#if (SemanticCube[type_dict['string']][type_dict['string']][operator_dict['-']] != -1): print("ERROR 2")
#if (SemanticCube[type_dict['int']][type_dict['int']][operator_dict['-']] == -1): print("ERROR 3")
#if (SemanticCube[type_dict['int']][type_dict['dec']][operator_dict['<']] == -1): print("ERROR 4")
#if (SemanticCube[type_dict['int']][type_dict['yesno']][operator_dict['*']] != -1): print("ERROR 5")
#if (SemanticCube[type_dict['int']][type_dict['dec']][operator_dict['==']] != type_dict['yesno']): print("ERROR 6")
#if (SemanticCube[type_dict['int']][type_dict['dec']][operator_dict['==']] != type_dict['yesno']): print("ERROR 7")

# SHOULD WE ADD AND and OR?
