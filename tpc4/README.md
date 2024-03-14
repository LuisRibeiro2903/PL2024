# TPC4

**Título** Analisador léxico simples de SQL \
**Autor** Luís de Sá Ribeiro, A100608

## Objetivos

Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:

> Select id, nome, salario From empregados Where salario >= 820

## Resolução

Começamos por definir os tokens possíveis presentes: 
* `VARIABLE`,
*  `COMMA`,
* `GREATER`,
* `LESSER`,
* `GREATER_EQUAL`,
* `LESSER_EQUAL`,
* `EQUAL`,
* `NUM`

Aos quais juntamos as ***keywords reservadas***:

* `SELECT`
* `FROM` 
* `WHERE`

Depois disto, o processor é semelhante ao exemplos vistos nas aulas. A única coisa a ter em atenção é a *tokenizing fucntion* das variáveis, pois esta vai apanhar também as *reserved keywords* já que estas encaixam na expressão regular das variáveis (`[A-Za-z_][A-Za-z0-9-_]*`). Para prevenir isto, definiu-se em cima o dicionário das *keywords*, e ao definir o tipo dos tokens que entram na função das variáveis vai-se fazer um get no dicionário caso seja as tais *keywords*, caso contrário o valor *default* será `VARIABLE`

## Conclusão

Os tokens apanhados são imprimidos para o `stdout`.