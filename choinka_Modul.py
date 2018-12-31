
def choinka(poziom):
    for a in range(poziom+1):
        print(" "*(poziom-a)+"*"*(2*a-1))
        print(" "*(poziom-a)+"O "*a)
    print(" "*(poziom-1)+"*")
    print(" "*(poziom-2)+"***")
    return choinka
