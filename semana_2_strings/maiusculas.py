def maiusculas(frase):

    a=0
    compr=len(frase)
    b=""
    while(a<compr):
        if (ord(frase[a])>63) and (ord(frase[a])<96):
            b=b+(frase[a])
        a+=1

    return b
