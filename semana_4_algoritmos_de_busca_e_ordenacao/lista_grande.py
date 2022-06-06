import random

def lista_grande(n):
    lista=[]
    while(len(lista)<n):
        x=random.randint(0,100)
        lista.append(x)

    return lista 
