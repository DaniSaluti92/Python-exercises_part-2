lista_impares = []

def encontra_impares(lista):
    
    if len(lista) == 1:
        elemento = lista[0]
        resto = elemento%2

        if resto != 0:
            lista_impares.append(elemento)

    else:
        meio = len(lista)//2
        lista1 = lista[:meio]
        lista2 = lista[meio:]
        lista3 = encontra_impares(lista1)
        lista4 = encontra_impares(lista2)

    return lista_impares
