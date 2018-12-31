# duży lotek + nagroda

import random

# ustalenie przez użytkownika ile liczb jest do losowania
try:
    ileliczb = int(input("Podaj ilość typowanych liczb: "))
    maksliczba = int(input("Podaj maksymalną losową liczbę: "))
    if ileliczb > maksliczba:
        print("Błędne dane!")
        exit()
except ValueError:
    print("Błędne dane!")
    exit()

# losowanie liczb randomowych i zapisywanie ich do listy "wylosowane"
wylosowane = []
i=0
while i < ileliczb:
    liczba = random.randint(1,maksliczba)
    if wylosowane.count(liczba) == 0:
        wylosowane.append(liczba)
        i = i+1
    
# pętla, aby użytkownik mógł 3 razy typować liczby
for x in range(3):
    print("\n\t\tLOSOWANIE %s" %(x+1))
    print("Wytypuj %s z %s liczb: " %(ileliczb, maksliczba))
    
    # wybieranie liczb i zapisywanie ich do listy "typy"
    typy = []
    i=0
    while i < ileliczb:
        try:
            typ = int(input("Podaj liczbę %s: " %(i+1)))
        except ValueError:
            print("Błędne dane!")
            continue
        
        if typy.count(typ) == 0 and maksliczba >= typ > 0:
            typy.append(typ)
            i = i+1
    print("\nTwoje liczby to: ", typy)
    
    # porównianie liczb i wyświetlenie powtórzonych lub nagrodę
    print("\n"+"X"*40+"\n\t\tWYNIK %s" %(x+1))
    trafione = set(wylosowane) & set(typy)

    if len(trafione) == ileliczb:
        print("GRATULACJE !!!")
        def choinka(poziom):
            for a in range(poziom+1):
                print(" "*(poziom-a)+"*"*(2*a-1))
                print(" "*(poziom-a)+"O "*a)
            print(" "*(poziom-1)+"*")
            print(" "*(poziom-2)+"***")
        choinka(13)
        break
    
    elif trafione:
        print("Ilość trafień: %s" % len(trafione))
        print("Trafione liczby: ", trafione)
        
    else:
        print("Brak trafień. Spróbuj jeszcze raz!") 
    print("X"*40)

print("\nWylosowane liczby to: ",wylosowane)
