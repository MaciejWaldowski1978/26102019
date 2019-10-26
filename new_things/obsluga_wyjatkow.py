# # progrma odporny na bledy try: i except to jest jedyny sposob
#
# zmienna = input("Podaj liczbe:: ")
#
# try:                                    # tutaj zaczynamy sprawdzanie
#
#     zmienna_integer = int(zmienna)
#     print(f"To jest liczba {zmienna_integer}")
#
# except Exception:                       # tutaj sie konczy sprawdzanie czyli except Exception
#     print("Nie bylem wstanie zrzutowac na inta !!")



zmienna_1 = input("Podaj liczbe:: ")
zmienna_2 = input("Podaj liczbe:: ")

try:                                    # tutaj zaczynamy sprawdzanie

    zmienna_1 = int(zmienna_1)
    zmienna_2 = int(zmienna_2)

    print(f"Suma liczb {zmienna_1 + zmienna_2 }")

except Exception:                       # tutaj sie konczy sprawdzanie czyli except Exception
    print("Nie bylem wstanie zrzutowac na inta !!")

print("Koniec")