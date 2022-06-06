def sao_multiplicaveis(m1,m2):
    n_linhas_m1=len(m1)
    linha_m1=m1[0]
    n_colunas_m1=len(linha_m1)

    n_linhas_m2=len(m2)
    linha_m2=m2[0]
    n_colunas_m2=len(linha_m2)

    if (n_colunas_m1)==(n_linhas_m2):
        return True
    else:
        return False
