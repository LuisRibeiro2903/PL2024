# TPC5

**Título** Gramática Independente de Contexto (GIC) \
**Autor** Luís de Sá Ribeiro, A100608

## Objetivos

Construir uma gramática para uma linguagem simples.

Exemplo:

    ?a 
    b=a*2/(27-3)
    !a+b
    c=a*b/(a/b)

## Resolução

    T = {'?', var, '=', '*', num, '/', '(', ')', '-', '!'}

    N = {S, Expr, Op, Expr2, Op2, Expr3}

    S = S

    P = {

        S -> '?' var              LA = {'?'}
           | '!' Expr             LA = {'!'}
           | var '=' Expr         LA = {var}
    
        Expr -> Expr2 Op

        Op -> &                   LA = Follow(Op) = Follow(Expr) = {')'}
            | '+' Expr            LA = {'+'}
            | '-' Expr            LA = {'-'}
        
        Expr2 -> Expr3 Op2

        Op2 -> &                  LA = Follow(Op2) = Follow(Expr2) = {')','+','-'}
             | '*' Expr           LA = {'*'}
             | '/' Expr           LA = {'/'}
        
        Expr3 -> '(' Expr ')'     LA = {'('}
               | var              LA = {var}
               | num              LA = {num}
    }