import sys
import ply.yacc as yacc
from expression_lex import tokens

def p_grammar(p):
    """
    expCond : exp
            | exp OPREL exp
    OPREL : '=' 
          | '!' 
          | '>' 
          | '<'
          | '<' '='
          | '>' '='
    exp : term
        | exp OPAD term
    OPAD : '+' 
         | '-' 
         | or
	term : fact
         | term OPMUL fact
    OPMUL : '*' 
          | '/' 
          | and
    fact : number
         | id
         | '(' expCond ')'
         | not expCond
         | '-' exp
    """
def p_error(p):
    print("Syntax error in input!",p)
    parser.success=False
parser = yacc.yacc()
for linha in sys.stdin:
    parser.success=True
    parser.parse(linha)
    if parser.success:
       print('Parsing completed!')
    else:
       print('Parsing failed!')
