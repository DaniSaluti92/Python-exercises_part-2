def primeiro_lex(lista):
    a=0
    compr=len(lista)
    c="~"

    while(a<compr):
        if (lista[a])<c:
            c=lista[a]
        a+=1

    return c
