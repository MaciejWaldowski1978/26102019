x = 5
krotka = ("element", "drugi_element")

ciag_znakow = "Nasza liczba to:, {} blablba {}"

print("Nasza liczba to:", x, sep = "     ") # formatowanie strungow f
print(f"Nasza liczba to:, {x} blablba {krotka}") # formatowanie strungow f i nawisy wansate
print(f"Nasza liczba to:, {x + 10} blablba {krotka}") # formatowanie strungow f i nawisy wansate

print("Nasza liczba to:, {} blablba {}", (x+15, krotka)) # formatowanie strungow f i nawisy wansate
print(ciag_znakow.format, (x+15, krotka)) # formatowanie strungow f i nawisy wansate


print("Nasza liczba to:, {} blablba {}".format(x+15, krotka, {2: "slownik"})) # formatowanie strungow f i nawisy wansate



imie = input("Podaj imie :")

nazwisko = input("Podaj nazwisko :")


odpowiedz = (f"Twoje imie to {imie}, a nazwisko to {nazwisko.upper()}")
odpowiedz2 = ("Twoje imie to {}, a nazwisko to {}".format(imie.capitalize(), nazwisko.capitalize()))

print(odpowiedz)
print(odpowiedz2)

#print("cos" % (infor)) # nie dziala a bylo pokazana na udemy
