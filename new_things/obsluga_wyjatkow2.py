# wyrzucamy blad czyli sami piszemy jakie bledy chcemy aby wyrzucil....
try:
    raise Exception("Dwoń po Policję !")
except Exception:
    print("Tutaj sie jeszcze wypierdzielilem")

raise Exception ("Inny blad")
