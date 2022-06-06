def imprime_matriz(matriz):

    n_linhas=len(matriz)
    linha=matriz[0]
    n_colunas=len(linha)
    a=0

    while(a<n_linhas):
        b=0
        while (b<n_colunas):
            if b==((n_colunas)-1):
                print(matriz[a][b],end="")
            else:
                print(matriz[a][b],end=" ")
            b=b+1
        a=a+1
        print()
