def soma_matrizes(m1,m2):
    n_linhas_m1=len(m1)
    linha_m1=m1[0]
    n_colunas_m1=len(linha_m1)

    n_linhas_m2=len(m2)
    linha_m2=m2[0]
    n_colunas_m2=len(linha_m2)

    #somas as matrizes

    a=0
    soma_matrizes=[]

    while (a<n_linhas_m1):
        linha=[]
        b=0
        while (b<n_colunas_m1):
            soma_elementos=(m1[a][b])+(m2[a][b])
            linha.append(soma_elementos)
            b=b+1
        a=a+1
        soma_matrizes.append(linha)

    if (n_linhas_m1==n_linhas_m2) and (n_colunas_m1==n_colunas_m2):
        return(soma_matrizes)
    else:
        return False
        
