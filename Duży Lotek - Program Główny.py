
from Duży_Lotek_Moduł import ustawienia, wylosowane, pobierztypy, wyniki
from Duży_Lotek_Moduł import czytaj_json, zapisz_json
# from Duży_Lotek_Moduł import czytaj_str, zapisz_str
import time

def main(args):
    # ustawienia gry
    nick, ileliczb, maksliczba, ilerazy = ustawienia()

    # losujemy liczby
    liczby_wylosowane = wylosowane(ileliczb, maksliczba)

    # pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
    for i in range(ilerazy):
        typy = pobierztypy(ileliczb, maksliczba)
        iletraf = wyniki(liczby_wylosowane, typy, ileliczb)

    nazwapliku = nick + ".json" # nazwa pliku z historią losowań
    losowania = czytaj_json(nazwapliku)

    losowania.append({
        "czas": time.time(),
        "dane": (ileliczb,maksliczba),
        "wylosowane": liczby_wylosowane,
        "ile": iletraf
        })

    zapisz_json(nazwapliku, losowania)

    print("\nLosowania: ",liczby_wylosowane)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
