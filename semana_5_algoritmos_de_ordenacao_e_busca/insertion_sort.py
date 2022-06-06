def insertion_sort(lista):
    a=0

    while a<(len(lista)-1):
        if lista[a+1]<lista[a]:
            lista[a], lista[a+1] = lista[a+1], lista[a]
            a=0
        else:
            a+=1

    return lista
