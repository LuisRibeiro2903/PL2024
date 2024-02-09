import sys

def ParseLinha (linha):
    parametros = linha.strip().split(',')
    return parametros[8], parametros[13]

if __name__ == '__main__':
    modalidades = set()
    entradas = 0
    aptos = 0
    header = sys.stdin.readline()
    for linha in sys.stdin:
        modalidade, apto = ParseLinha(linha)
        modalidades.add(modalidade)
        if apto:
            aptos = aptos + 1
        entradas = entradas + 1
    
    print(sorted(modalidades))
    print()
    