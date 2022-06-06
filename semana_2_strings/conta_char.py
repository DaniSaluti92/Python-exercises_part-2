def conta_letras(frase,contar="vogais"):

    a=0
    compr=len(frase)
    vogais=0
    consoantes=0

    while(a<compr):
        b=frase[a]
        if (b=="a" or b=="e" or b=="i" or b=="o" or b=="u") or (b=="A" or b=="E" or b=="I" or b=="O" or b=="U"):
            vogais += 1
        elif (ord(b))>31 and (ord(b))<65 :
            vogais=vogais+0
        else:
            consoantes +=1
        a+=1

    if contar=="vogais":
        return vogais
    else:
        return consoantes
