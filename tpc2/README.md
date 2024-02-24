# TPC2

**Título** Conversor básico de Markdown para html
**Autor** Luís de Sá Ribeiro, A100608

## Objetivos

Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

- Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"

In: # Exemplo
Out: \<h1>Exemplo\</h1>

- Bold: pedaços de texto entre "**":

In: Este é um \*\*exemplo\*\* ...
Out: Este é um \<b>exemplo\</b> ...

- Itálico: pedaços de texto entre "*":

In: Este é um \*exemplo\* ...
Out: Este é um \<i>exemplo\</i> ...

- Lista numerada:

In:
1. Primeiro item
2. Segundo item
3. Terceiro item
Out:
\<ol>
\<li>Primeiro item\</li>
\<li>Segundo item\</li>
\<li>Terceiro item\</li>
\</ol>

- Link: [texto](endereço URL)

In: Como pode ser consultado em \[página da UC](http://www.uc.pt)
Out: Como pode ser consultado em \<a href="http://www.uc.pt">página da UC\</a>

- Imagem: ![texto alternativo](path para a imagem)

In: Como se vê na imagem seguinte: \!\[imagem dum coelho](http://www.coellho.com) ...
Out: Como se vê na imagem seguinte: \<img src="http://www.coellho.com" alt="imagem dum coelho"/> ...

## Resolução:

O ficheiro é lido através do `stdin`, ou seja, é esperado que o *standard input* esteja redirecionado para o ficheiro, usando por exemplo o comando: `python3 md_to_html.py teste.html < teste.md` ou `cat teste.md | python3 md_to_html.py teste.html`. Se não for atríbuido nenhum argumento ao programa (e.g: `python3 md_to_html.py` apenas) o resultado será guardado com o nome `result.html`. Cada linha é interpretada e convertida de acordo. A ordem com que se chama as funções de conversão é importante para o correto funcionamento do conversor.

#### Por objetivo:

* Cabeçalhos
> Com a expressão regular `"^ {0,3}(#+) "` é possível verificar se se trata de uma linha de cabeçalho, e contando quantos `#` estão no grupo de captura, conseguimos definir o nível do cabeçalho (No ínicio considera-se que se houver até 3 espaços antes do operador de cabeçalho ainda é convertido pois é o que acontece em Markdown também).

* Bold e itálico
> São ambos semelhantes tanto na resolução como na expressão regular, `"\*\*(.+?)\*\*"` e `"\*(.+?)\*"` respetivamente. É importante aqui que **bold** seja verificado primeiro, pois caso contrário, se houvesse algo que era suposto ser bold, `**exemplo**`, a expressão para *itálico* reconheceria, ficaria `<i>*exemplo*</i>`.

* Lista numerada
> Com a expressão `"^ {0,3}\d+\. (?P<content>.*)$"` percebemos se se trata de uma lista numerada, enquanto se captura o conteúdo. Tendo a lista de linhas html que se vai convertendo, podemos ver se a anterior à que se está a analisar era já uma entrada da lista (`<li> in html[-1]`). Isto é útil para se saber se a tag de lista ordenada `<ol>` é preciso ser usada. Também serve para, no caso de não haver *match* da expressão regular, se fechar a tag com `</ol>`, pois se a linha anterior era uma entrada da lista e a atual já não é, tem que se fechar a *ordered list*. No fim do programa verifica-se se é preciso fechar mais uma vez para no caso particular de a última linha do ficheiro Markdown ser um elemento de uma lista, pois não há mais nenhuma linha seguinte para se fazer o processo explicado anteriormente.

* Links e imagens
> Tal como **bold** e *itálico* a resolução e as expressões regulares são semelhantes: `"\[(?P<texto>[^\]]*)\]\((?P<url>[^\)]*)\)"` e `"\!\[(?P<alt>[^\]]*)\]\((?P<path>[^\)]*)\)"` respetivamente. E aqui mais uma vez também é importante que os links venham primeiro, pelos mesmos motivos de **bold** e *itálico*.

#### Conclusão

Após a análise, utiliza-se uma função genérica que aceita o nome e o conteúdo e cria um ficheiro html
 