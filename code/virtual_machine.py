import sys
import csv
from classes.quadruple import Quadruple


quads = []

def equals(q):
    q.result = q.left_operand
    return q.

def add(q):
    q.result = q.left_operand + q.right_operand

def subt(q):
    q.result = q.left_operand - q.right_operand

def mult(q):
    q.result = q.left_operand * q.right_operand

def div(q):
    q.result = q.left_operand / q.right_operand


def init_quads(file_name):
    with open(file_name, 'rb') as fle:
        reader = csv.reader(fle, delimiter=',', quotechar='|')
        for row in reader:
            print row
            q = Quadruple(row[0],row[1],row[2],row[3])
            quads.append(q)

def run():
    quad = quads[0]
    while quad:
        oper = quad.operator
        if (oper == '='):


if __name__ == '__main__':

    if (len(sys.argv) > 1) : file1 = sys.argv[1]
    else : file1 = '../output.obj'

    init_quads(file1)
    run()

    for q in quads:
        q.print_quad
    # print data
    # print "End of file"


    print("Successful")
