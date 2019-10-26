import csv # importuje biblioteke csv


def prepare_data(wartosc): # funkcja przygotowanie danych

    wartosc = wartosc.replace("$", "") # zastapienie $ na kwocie wartosc
    wartosc = wartosc.replace(",", "")  # zastapienie $ na kwocie wartosc
    kwota = float(wartosc)

    if isinstance(kwota, float): # sprawdzenie czy jest zmienna float
        return kwota


def analisis(lista):
    srednia = sum(lista)/len(lista)
    return srednia

def wyciagnij_srednia(csv_file):
    lista = []
    for row in csv_file:
        wartosc = row["balance"] # to jest nasza jedna kolumna tam gdzie sa kwoty w dolarach...
        kwota = prepare_data(wartosc)  # wywolanie funkcji prepare data
        lista.append(kwota) # dodaje do listy

    wynik = analisis(lista) # wrzucenie do sredniej

    return round(wynik, 2) # zwrocenie wyniku zaokraglonego do 2 miejsc

def wypisz_wiersze(csv_file):
    for row in csv_file:
        print(row["balance"])

with open("../resources/data.csv") as plik:
    csv_file = csv.DictReader(plik)

    print(wyciagnij_srednia(csv_file))