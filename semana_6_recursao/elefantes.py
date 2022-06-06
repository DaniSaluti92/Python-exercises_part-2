def incomodam(n):

    if not n>0:
        return ""
    elif n==1:
        return "incomodam "
    else:
        return incomodam(1)*n


def elefantes(n):
    
    if not n>0:
        return incomodam(n)
    elif n==1:
        return "Um elefante incomoda muita gente" + "\n" + "2 elefantes" + " " +  incomodam(n+1) + "muito mais" + "\n"

    return elefantes(n-1) + (str(n-1) + " " + "elefantes incomodam muita gente" + "\n" + str(n) + " " + "elefantes" + " " + incomodam(n) + "muito mais" + "\n" if n>2 else "")
