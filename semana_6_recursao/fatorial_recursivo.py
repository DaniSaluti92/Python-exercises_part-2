def fatorial(x):
    if x<0:
        return False
    elif x>=0 and x<=1:
        return 1
    else:
        return x*fatorial(x-1)