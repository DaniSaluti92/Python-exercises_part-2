def soma_lista(lista):
    soma=0
    
    if len(lista)<=2:
        for i in lista:
            soma=soma+i
    else:
        meio = len(lista)//2
        lista1 = lista[:meio]
        lista2 = lista[meio:]
        soma = soma_lista(lista1)+soma_lista(lista2)

    return soma
