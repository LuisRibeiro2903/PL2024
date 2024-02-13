# TPC1

**Título** Análise de dados em csv
**Autor** Luís de Sá Ribeiro, A100608

## Objetivos

* Lista ordenada alfabeticamente das modalidades desportivas;
* Percentagens de atletas aptos e inaptos para a prática desportiva;
* Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...

## Resolução:

Para satisfazer todos os objetivos impostos, foi criada uma classe `EMD_DTO`. Esta classe contém atributos respetivos às colunas do ficheiro csv mas não todas, apenas aquelas necessárias à resolução destes objetivos.

De seguida, lê-se o ficheiro através do `stdin`, ou seja, é esperado que o *standard input* esteja redirecionado para o ficheiro, usando por exemplo o comando: `python3 tpc1.py < emd.csv`