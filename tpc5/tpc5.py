import ply.lex as lex
from tabulate import tabulate
import json
import re


class MaquinaVending:

    #stock : Dict[key -> código, value -> (nome, quantidade, preco)]
    def __init__ (self, stock: dict):
        self.lexer = lex.lex(module=self)
        self.saldo = 0
        self.stock = stock
        self.on = True

    

    tokens = [
        'LISTAR',
        'MOEDA',
        'SELECIONAR',
        'SAIR'
    ]

    def t_LISTAR(self, t):
        r'LISTAR'
        
        table_data = []
        for cod, values in self.stock.items():
            table_data.append([cod, values[0], values[1], values[2]])

        print(tabulate(table_data, headers=["Código", "Nome", "Quantidade", "Preço"]))

        return t
    

    def t_MOEDA (self, t):
        r"MOEDA\s+((2|5|10|20|50)c|(1|2)e)(?:\s*,\s*((2|5|10|20|50)c|(1|2)e))*"

        for moeda in re.finditer(r'(?:(?P<cent>2|5|10|20|50)c|(?P<euro>1|2)e)', t.value):
            if moeda.lastgroup == "cent":
                self.saldo += int(moeda.group("cent"))
            else:
                self.saldo += int(moeda.group("euro")) * 100
        printable_euro, printable_cent = divmod(self.saldo, 100)
        print(f"Saldo = {printable_euro}e{printable_cent}c")

        return t


    def t_SELECIONAR (self, t):
        r"SELECIONAR\s+.+"

        codigo = t.value.replace(" ", "")[10:]
        item = self.stock.get(codigo)
        if not item:
            print(f"Não existe nenhum produto com código {codigo}")
        else:
            if item[2] > self.saldo:
                print("Saldo insuficiente para satisfazer o seu pedido")
                printable_euro_saldo, printable_cent_saldo = divmod(self.saldo, 100)
                printable_euro_item, printable_cent_item = divmod(item[2], 100)
                print(f"Saldo = {printable_euro_saldo}e{printable_cent_saldo}c; Pedido = {printable_euro_item}e{printable_cent_item}c")
            else:
                print(f"Pode retirar o produto dispensado \"{item[0]}\"")
                self.saldo -= item[2]
                printable_euro, printable_cent = divmod(self.saldo, 100)
                print(f"Saldo = {printable_euro}e{printable_cent}c")
                if item[1] == 1:
                    del self.stock[codigo]
                else:
                    self.stock[codigo] = (item[0], item[1] - 1, item[2])

        return t


    def t_SAIR (self, t):
        r'SAIR'

        if self.saldo == 0:
            print("Sem troco para dar")
        else:
            output = "Pode retirar o troco: "
            saldo = self.saldo
            moedas = [200, 100, 50, 20, 10, 5, 2]
            i = 0
            while (i < 2 and saldo != 0):
                quoc, resto = divmod(saldo, moedas[i])
                if quoc != 0:
                    output += f"{quoc}x {moedas[i] / 100}e, "
                saldo = resto
                i += 1

            while (saldo != 0):
                quoc, resto = divmod(saldo, moedas[i])
                if quoc != 0:
                    output += f"{quoc}x {moedas[i]}c, "
                saldo = resto
                i += 1
            print(output[:-2])
        print("Até à próxima")
        self.on = False
        return t


    t_ignore = ' \t'

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Unsupported character '{t.value[:-1]}'")
        t.lexer.skip(len(t.value))

def main():
    with open('stock.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
    stock = {}
    for item in data["stock"]:
        key = item['cod']
        value = (item['nome'], int(item['quant']), int(float(item['preco']) * 100))
        stock[key] = value

    maquina = MaquinaVending(stock)

    while(maquina.on):
        line = input()
        maquina.lexer.input(line)
        maquina.lexer.token()


if __name__ == "__main__":
    main()