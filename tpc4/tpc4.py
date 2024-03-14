import ply.lex as lex
import sys

reserved_keywords = {
    'SELECT' : 'SELECT',
    'FROM' : 'FROM',
    'WHERE' : 'WHERE'
}

tokens = (
    'VARIABLE',
    'COMMA',
    'GREATER',
    'LESSER',
    'GREATER_EQUAL',
    'LESSER_EQUAL',
    'EQUAL',
    'NUM'
) + tuple(reserved_keywords.values())


t_SELECT = r'[Ss][Ee][Ll][Ee][Cc][Tt]'
t_WHERE = r'[Ww][Hh][Ee][Rr][Ee]'
t_FROM = r'[Ff][Rr][Oo][Mm]'

def t_VARIABLE (t): 
    r'[A-Za-z_][A-Za-z0-9-_]*'
    t.type = reserved_keywords.get(t.value.upper(), 'VARIABLE')
    return t

t_COMMA = r'\,'
t_GREATER = r'\>'
t_LESSER = r'\<'
t_GREATER_EQUAL = r'\>\='
t_LESSER_EQUAL = r'\<\='
t_EQUAL = r'\='

def t_NUM (t):
    r'\d+'
    t.value = int(t.value)    
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Unsupported character '{t.value[0]}'")
    t.lexer.skip(1)


def main():
    lexer = lex.lex()
    for line in sys.stdin:
        lexer.input(line)
        for tok in lexer:
            print(tok)
            print(tok.type, tok.value, tok.lineno, tok.lexpos)


if __name__ == "__main__":
    main()