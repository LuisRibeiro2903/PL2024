# TPC1

**Título** Análise de dados em csv
**Autor** Luís de Sá Ribeiro, A100608

## Objetivos

* Lista ordenada alfabeticamente das modalidades desportivas;
* Percentagens de atletas aptos e inaptos para a prática desportiva;
* Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...

## Resolução:

Para satisfazer todos os objetivos impostos, foi criada uma classe `EMD_DTO`. Esta classe contém atributos respetivos às colunas do ficheiro csv mas não todas, apenas aquelas necessárias à resolução destes objetivos.

De seguida, lê-se o ficheiro através do `stdin`, ou seja, é esperado que o *standard input* esteja redirecionado para o ficheiro, usando por exemplo o comando: `python3 tpc1.py < emd.csv`. Criando e populando uma lista de `EMD_DTO` está-se pronto para resolver os 3 pontos.

#### Por objetivo:

* Lista ordenada alfabeticamente
> Apenas se extrai as categorias de cada objeto para uma lista por compreensão e se ordena.

* Percentagens de atletas aptos e inaptos
> Cria-se uma lista por compreensão com apenas os elementos aptos
  O tamanho desta lista a dividir pelo tamanho da inicial será a percentagem de atletas aptos
  1 (ou 100, pois no meu caso apresento o valor em percentagem) menos este valor, dará o valor de inaptos

* Distribuição por escalão etário
> Ordena-se a lista pela idade, por uma questão de legibilidade
  Para cada elemento, calcula-se a que intervalo pertence

#### Conclusão

Após a análise, utiliza-se uma função genérica que aceita o nome e o conteúdo e cria um ficheiro csv
 