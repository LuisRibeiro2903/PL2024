import sys
import ply.yacc as yacc
from expression_lex import tokens

def p_prg1(p):
    "prg : atribs"
    p[0] = "pushn " + str(parser.id_count) + "\nSTART\n" + p[1] + "STOP\n"
    return p
    
def p_atribs1(p):
    "atribs : atrib"
    p[0] = p[1]
    return p

def p_atribs2(p):
    "atribs : atribs atrib"
    p[0] = p[1] + p[2]
    return p

def p_atrib(p):
    "atrib : id '=' expCond"
    if p[1] not in parser.id_table:
        parser.id_table[p[1]] = parser.id_count
        parser.id_count += 1
    p[0] = p[3] + "storeg " + str(parser.id_table[p[1]]) + "\n"
    return p

def p_expCond1(p):
    "expCond : exp"
    p[0] = p[1]
    return p

def p_expCond2(p):
    "expCond : exp '=' '=' exp"
    p[0] = p[1] + p[4] + "EQUAL\n"
    return p

def p_exp1(p):
    "exp : term"
    p[0] = p[1]
    return p
    
def p_exp2(p):
    "exp : exp '+' term"
    p[0] = p[1] + p[3] + "ADD\n"
    return p
    
def p_exp3(p):
    "exp : exp or term"
    p[0] = p[1] + p[3] + "ADD\npushi 1\nSUPEQ\n"
    return p
    
def p_term1(p):
    "term : fact"
    p[0] = p[1]
    return p
    
def p_term2(p):
    "term : term '*' fact"
    p[0] = p[1] + p[3] + "MUL\n"
    return p

def p_fact1(p):
    "fact : number"
    p[0] = "pushi " + p[1] + "\n"
    return p
    
def p_fact2(p):
    "fact : '(' expCond ')'"
    p[0] = p[2]
    return p
    
def p_fact3(p):
    "fact : id"
    p[0] = "pushg " + str(parser.id_table[p[1]]) + "\n"
    return p

def p_error(p):
    print("Syntax error in input!",p)
    parser.success=False

parser = yacc.yacc()
parser.success = True
parser.id_table = { }
parser.id_count = 0

source = ""
for linha in sys.stdin:
    source += linha
codigo = parser.parse(source)
if parser.success:
    print('Parsing completed!')
    print(codigo)
else:
    print('Parsing failed!')
