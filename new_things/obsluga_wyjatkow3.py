# def pobierz_liczbe():
#     return int(input("Pdaj liczbe "))
#
# pobierz_liczbe()

def wsadz_do_listy (element, lista):
    if element<10: # sprawdzamy
        lista.append(element) # dodajemy element patrz to co na dole ...
    else: # w momencie gdy jest wsadzana liczba 112 to 112 jest > od 10 i wchodzimy tutaj i na samym koncu lapiemy wyjatek
        raise Exception(f"Element {element} jest wiekszt niz 10 ups")

nasza_lista =[] #pusta lista
print(nasza_lista) #wypisz pusta liste

try: # zabezpieczamy sie
    wsadz_do_listy(0, nasza_lista) # metoda wsadz do listy
    print(nasza_lista) # dwa argument lelemnt i lista nasz ...

    wsadz_do_listy(1, nasza_lista)
    print(nasza_lista)

    wsadz_do_listy(2, nasza_lista)
    print(nasza_lista)

    wsadz_do_listy(3, nasza_lista)
    print(nasza_lista)

    wsadz_do_listy(4, nasza_lista)
    print(nasza_lista)

    wsadz_do_listy(112, nasza_lista) # ten wyjatek sie nie dodaje do listy i kod sie nie wywala poniewaz jeste w try except
    print(nasza_lista)

    wsadz_do_listy(9, nasza_lista)
    print(nasza_lista)

except Exception as error: # error to taka zmienna jak element w for ze :)
    print(error)
    print(nasza_lista) # tutaj wyprintuje aktualna liste mozemy z tego zrezygnwac

