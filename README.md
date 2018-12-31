# Lotto-nagroda

Główny plik programu to "Duży Lotek - Program Główny" importuje on z pliku moduł "Duży_Lotek_Moduł" następujące funkcje:

def ustawienia():
def czytaj_ust(nazwapliku):
def zapisz_ust(nazwapliku, gracz):
    # Funkcja pobiera nick użytkownika, ilość losowanych liczb, maksymalną losowaną wartość oraz ilość typowań. Ustawienia zapisuje.
    
def wylosowane(ile, maks):
    # Funkcja losuje ile unikalnych liczb całkowitych od 1 do maks
    
def pobierztypy(ile, maks):    
    # Funkcja pobiera od użytkownika jego typy wylosowanych liczb
    
def wyniki(wylosowane, typy, ile):
    # Funkcja porównuje wylosowane i wytypowane liczby, zwraca ilość trafień
    
def czytaj_json(nazwapliku):
    # Funkcja odczytuje dane w formacje json z pliku
    
def zapisz_json(nazwapliku, dane):
    # Funkcja zapisuje dane w formacje json do pliku
    
W pliku moduł "choinka_Modul" możemy znaleźć funkcję "def choinka(poziom):", która zostaje uruchomiona po wytypowaniu wszystkich prawidłowych liczb.
