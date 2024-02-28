# TPC3

**Título** Somador On/Off \
**Autor** Luís de Sá Ribeiro, A100608

## Objetivos

Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;

1. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
2. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
3. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

## Resolução

Como em **TPCs** anteriores, lemos o input pelo `stdin`. O estado On/Off é inicializado a **On** portanto qualquer número que apareça antes do primeiro **Off** é adicionado ao contador.

Definimos as expressões regulares para os 4 casos: inteiro, on, off, =. Aqui estão respetivamente:

1. (?P\<integer>[+-]?\d+)
2. (?P\<on_state>on)
3. (?P\<off_state>off)
3. (?P\<sum>=)

De seguida combinamos todas estas expressões numa só, separadas pelo operador de **OU** lógico `|` para podermos usar a função `finditer` do módulo **re** que nos devolve um iterador produzindo objetos `Match` sobre todas as correspondências não sobrepostas para o padrão mencionado anteriormente.

Em cada iteração verifica-se a qual grupo pertence o que foi capturado, e faz-se o que cada grupo especifica nos **Objetivos**

## Conclusão

Cada sinal de igual irá passar para o `stdout` o resultado da soma no momento, podendo ser também redirecionado para um ficheiro.