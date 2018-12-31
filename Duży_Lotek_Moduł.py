# duży lotek + nagroda

import random
import os
import json 

def ustawienia():
    # Funkcja pobiera nick użytkownika, ilość losowanych liczb, maksymalną losowaną wartość
    # oraz ilość typowań. Ustawienia zapisuje.

    nick = input("Podaj nick: ")
    nazwapliku = nick + ".ini"
    gracz = czytaj_ust(nazwapliku)
    odp = None
    if gracz:
        print("Twoje ustawienia:\nLiczb: %s\nZ Maks: %s\nLosowań: %s" %(gracz[1], gracz[2], gracz[3]))
        odp = input("Zmieniasz (t/n)? ")

    if not gracz or odp.lower() == "t":      
        while True:
            try:
                ile = int(input("Podaj ilość typowanych liczb: "))
                maks = int(input("Podaj maksymalną losową liczbę: "))
                if ile > maks:
                    print("Błędne dane!")
                    continue
                ilelos = int(input("Ile losowań: "))
                break
            except ValueError:
                print("Błędne dane!")
                continue
        gracz = [nick, str(ile), str(maks), str(ilelos)]
        zapisz_ust(nazwapliku, gracz)

    return gracz[0:1] + [int(x) for x in gracz[1:4]]

def czytaj_ust(nazwapliku):
    if os.path.isfile(nazwapliku):
        plik = open(nazwapliku, "r")
        linia = plik.readline()
        plik.close()
        if linia:
            return linia.split(";")
    return False

def zapisz_ust(nazwapliku, gracz):
    plik = open(nazwapliku, "w")
    plik.write(";".join(gracz))
    plik.close()

def wylosowane(ile, maks):
    # Funkcja losuje ile unikalnych liczb całkowitych od 1 do maks
    wylosowane = []
    i=0
    while i < ile:
        liczba = random.randint(1,maks)
        if wylosowane.count(liczba) == 0:
            wylosowane.append(liczba)
            i = i+1
    return wylosowane
        


def pobierztypy(ile, maks):    
    # Funkcja pobiera od użytkownika jego typy wylosowanych liczb
    print("Wytypuj %s z %s liczb: " %(ile, maks))
    typy = []
    i=0
    while i < ile:
        try:
            typ = int(input("Podaj liczbę %s: " %(i+1)))
        except ValueError:
            print("Błędne dane!")
            continue
        
        if typy.count(typ) == 0 and maks >= typ > 0:
            typy.append(typ)
            i = i+1
    return typy
    
   
from choinka_Modul import choinka

def wyniki(wylosowane, typy, ile):
    # Funkcja porównuje wylosowane i wytypowane liczby, zwraca ilość trafień
    trafione = set(wylosowane) & set(typy)
    if len(trafione) == ile:
        print("GRATULACJE !!!")
        choinka(13)

    elif trafione:
        print("Ilość trafień: %s" % len(trafione))
        trafione = ", ".join(map(str,trafione))
        print("Trafione liczby: ", trafione)
            
    else:
        print("Brak trafień. Spróbuj jeszcze raz!") 
    print("X"*40)
    return len(trafione)


def czytaj_json(nazwapliku):
    # Funkcja odczytuje dane w formacje json z pliku
    dane = []
    if os.path.isfile(nazwapliku):
        with open(nazwapliku, "r") as plik:
            dane = json.load(plik)
    return dane

def zapisz_json(nazwapliku, dane):
    # Funkcja zapisuje dane w formacje json do pliku
    with open(nazwapliku, "w") as plik:
        json.dump(dane, plik)


       
'''
def zapisz_str(nazwapliku, dane):
    # Funkcja zapisuje dane w formacje txt do pliku
    with open(nazwapliku, "w") as plik:
        for slownik in dane:
            linia = [k + ":" + str(w) for k, w in slownik.iteritems()]
            linia = ";".join(linia)
            # plik.write(linia+"\n") - zamiast tak, można:
            print >>plik, linia
'''
