def menor_nome(nomes):
    a=0
    b=0
    menor="abcdefghijklmnopqrstuvxz"
    compr_lista=len(nomes)

    while(a<compr_lista):
        nome=nomes[a]
        nome_limpo=nome.strip()
        nome_maiusc=nome_limpo.capitalize()
        tamanho=(len(nome_maiusc))
        if tamanho < len(menor):
            menor=nome_maiusc
        a+=1

    return menor
