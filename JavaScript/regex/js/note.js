\d = busca por números

\. = busca por . (o \ evita que regex considere um caractere especial)

{} = é um quantificador, defini quantas vezes o caracter apaarece em sequência
    EX: \d{3} = significa que aparecerá 3 números em seguência

\/ = busca por /

\( ou \) = busca () parênteses

. = é um meta-char que significa qualquer char (qualquer caracter)

[] = pode indica os tipo de caracter que podem aparecer no local
    EX: [-.] = . ou - podem aparecer
    OBS: Dentro dos [] não precisamos usar \ (todos os carater tem o real valor)

[]* = indica que os caracter dentro dos [] podem aparecer 1, 2 ou mais vezes

[0-9] = indica que podem aparecer algum numero entre 0 a 9

\s = indica espaços em branco (space ou TAB)

\w = significa word char e é uma atalho para [A-Za-z0-9_]


// Quantife

* = é um quantifier que significa zero ou mais vezes

? = indica que o caracter é opcional (pode ou não, aparecer) (zero ou uma vez)

[1,] ou + = uma ou mais vezes em sequência (sem o 0)
    OBS: [1,] = no minimo 1 vez

{3, 10} = no min 3 e max 10 vezes

/*--------------------------------------------------------*/

\d = Encontra correspondência com um número (Equivalente a [0-9])

^ = indica que o conteúdo está no inicio

$ = indica que o conteúdo está no final

\b = âncora que seleciona um word boundary, isso é o início ou fim da palavra

| = ou
    EX: x|y Pesquisa correspondência em 'x' ou 'y'

?: = dizemos que não queremos ver esse grupo na resposta

() = Declaramos um grupo

/*----------------- Nota sobre o uso do ? -----------------*/

Gananciosa: [a-z]{1,5}
Preguiçosa: [a-z]{1,5}?

/*---------------------------------------------------------*/

\1 = referencia ao primeiro grupo
    EX: (h1|h2)(?:.+) = o primeiro é (h1|h2)