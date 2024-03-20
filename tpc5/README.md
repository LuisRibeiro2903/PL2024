# TPC5

**Título** Implementação básica de uma Máquina de Vending \
**Autor** Luís de Sá Ribeiro, A100608

## Objetivos

Construir um programa que simule uma máquina de vending. A máquina tem um stock de produtos: uma lista de triplos, nome do produto, quantidade e preço.


## Resolução

Começamos por definir os tokens possíveis presentes: 
* `LISTAR`,
*  `MOEDA`,
* `SELECIONAR`,
* `SAIR`,

Desta vez, o lexer estará encapsulado numa classe `MáquinaVending`, onde guardamos também o saldo, os produtos existentes e o estado de on/off

Cada função de cada token terá um comportamento diferente:

* `t_LISTAR` apenas imprime os produtos existentes com ajuda da biblioteca ***tabulate*** (Ver **NOTA**).
* `t_MOEDA` será talvez a mais complexa, e trata de validar e atualizar o montante inserido, podendo este vir numa sequência separada por virgulas e um número indefinido de *whitespaces*.
* `t_SELECIONAR` atualiza o estado tanto do stock como do saldo do utilizador, conforme este tenha suficiente para comprar o produto selecionado (e também se este existe)
* `t_SAIR` acaba o programa definindo a flag de on para `False` e imprime o troco dividindo-o pelas moedas.

**NOTA**: É preciso instalar a biblioteca tabulate: `pip install tabulate`
