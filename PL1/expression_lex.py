import ply.lex as lex
import sys

# List of token names.   This is always required
tokens = (
    'number', 'id', 'and', 'or', 'not'
)
# Literals
literals = ['+', '-', '*', '/', '(', ')',  '!','=','>','<']

 
# A regular expression rule with some action code
def t_number(t):
    r'\d+'
    #t.value = int(t.value)    
    return t

def t_and(t):
    r'(?i)and'
    return t
def t_or(t):
    r'(?i)or'
    return t
def t_not(t):
    r'(?i)not'
    return t
    
def t_id(t):
    r'[a-zA-Z]+'
    return t
#----------------------------------------
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
#----------------------------------------
# Build the lexer
lexer = lex.lex()
