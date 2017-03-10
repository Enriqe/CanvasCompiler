import ply.lex as lex
import logging

logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)

reserved_words = {
    'int'       : 'INT',
    'dec'       : 'DEC',
    'string'    : 'STRING',
    'yesno'     : 'YESNO',
    #'yes'       : 'YESNO_VAL',
    #'no'        : 'YESNO_VAL',
    'point'     : 'POINT',
    'triangle'  : 'TRIANGLE',
    'circle'    : 'CIRCLE',
    'rectangle' : 'RECTANGLE',
    'canvas'    : 'CANVAS',
    'program'   : 'PROGRAM',
    'function'  : 'FUNCTION',
    'center'    : 'CENTER',
    'width'     : 'WIDTH',
    'height'    : 'HEIGHT',
    'with'      : 'WITH',
    'add'       : 'ADD',
    'paint'     : 'PAINT',
    'print'     : 'PRINT',
    'for'       : 'FOR',
    'each'      : 'EACH',
    'in'        : 'IN',
    'if'        : 'IF',
    'elsif'     : 'ELSIF',
    'else'      : 'ELSE',
    'color'     : 'COLOR',

    #AGREGAR A PROPUESTA
    'while'     : 'WHILE',
    'finish'    : 'FINISH',
    'main'      : 'MAIN',
    'while'     : 'WHILE',
    'read'      : 'READ',
    'return'    : 'RETURN',
    'returns'   : 'RETURNS',
    'red'       : 'RED',
    'green'     : 'GREEN',
    'blue'      : 'BLUE',
    'x'         : 'X',
    'y'         : 'Y',
}

tokens = [
    'EQUALS', 
    'L_BRACKET', 
    'R_BRACKET', 
    'G_THAN', 
    'L_THAN', 
    'NOT_EQUALS',
    'EQUALS_EQUALS', 
    'G_THAN_EQUALS', 
    'L_THAN_EQUALS', 
    'PLUS', 
    'MINUS',
    'DIV', 
    'MULT', 
    'L_PAR', 
    'R_PAR', 
    'COMMA',
    # ADD to TOKENS
    'INT_VAL', 
    'DEC_VAL', 
    'STRING_VAL', 
    'YESNO_VAL', 
    'VAR_IDENTIFIER'] + list(reserved_words.values())

t_ignore  = ' \t'

def t_EQUALS_EQUALS(t):
    r'=='
    return t

def t_EQUALS(t):
    r'\='
    return t

def t_L_PAR(t):
    r'\('
    return t

def t_R_PAR(t):
    r'\)'
    return t

def t_L_BRACKET(t):
    r'\['
    return t

def t_R_BRACKET(t):
    r'\]'
    return t

def t_NOT_EQUALS(t):
    r'!='
    return t

def t_G_THAN_EQUALS(t):
    r'>='
    return t

def t_L_THAN_EQUALS(t):
    r'<='
    return t

def t_G_THAN(t):
    r'>'
    return t

def t_L_THAN(t):
    r'<'
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_MINUS(t):
    r'\-'
    return t

def t_DIV(t):
    r'/'
    return t

def t_MULT(t):
    r'\*'
    return t

def t_COMMA(t):
    r','
    return t

def t_POINT(t):
    r'\.'
    return t

# REGULAR EXPRESSIONS

def t_INT_VAL(t):
    r'[0-9]+'
    return t

def t_DEC_VAL(t):
    r'[0-9]+[\.][0-9]+'
    return t

def t_STRING_VAL(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_YESNO_VAL(t):
    r'[yes|no]'
    return t

def t_VAR_IDENTIFIER (t):
    r'[a-zA-Z]+[a-zA-Z0-9]*(_[a-zA-Z0-9]*)*'
    t.type = reserved_words.get(t.value, 'VAR_IDENTIFIER')
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print "line " + str(t.lexer.lineno) + ": Illegal character " + str(t.value[0])
    t.lexer.skip(1)
    sys.exit(0)
log = logging.getLogger()
lexer = lex.lex(debug=True, debuglog=log)
