from Domain.Librarie import toString
from Logic.CRUD import adaugaLibrarie, getById, stergeLibrarie


def print_help():
    print("Comenzi disponibile: ")
    print("Ajutor: ")
    print("Adauga vanzare: adauga, id, titlu, gen, pret, reducere ")
    print("Sterge vanzare: sterge, id ")
    print("Afisare: showall ")
    print("Stop ")
    print("Parametrii trebuie separati prin virgula. ")
    print("Comenzile trebuie separate prin ; ")

def adauga(lista, parametrii):
    try:
        if len(parametrii) < 6:
            print("Parametrii insuficienti")
            return lista
        if len(parametrii) > 6:
            print("Prea multi parametrii")
            return lista
        id = str(parametrii[1])
        titlu = str(parametrii[2])
        gen = str(parametrii[3])
        pret = float(parametrii[4])
        reducere = str(parametrii[5])
        lista = adaugaLibrarie(id, titlu, gen, pret, reducere, lista)
        print("Adaugare efectuata")
        return lista
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def sterge(lista, parametrii):
    try:
        if len(parametrii) < 2:
            print("Parametrii insuficienti")
            return lista
        if len(parametrii) > 2:
            print("Prea multi parametrii")
            return lista
        id = parametrii[1]
        if getById(id, lista) is None:
            raise ValueError("Nu exista vanzare cu Id-ul dat")
        print("Stergere efectuata")
        return stergeLibrarie(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showall(lista, parametrii):
    if len(parametrii)>1:
        print("Comanda Afisare nu contine alti parametrii")
    else:
        for librarie in lista:
            print(toString(librarie))

def run_console(lista):
    print("Comenzi disponibile: ")
    print("Ajutor: ")
    print("Adauga vanzare: adauga, id, titlu, gen, pret, reducere ")
    print("Sterge vanzare: sterge, id ")
    print("Afisare: showall ")
    print("Stop ")
    print("Parametrii trebuie separati prin virgula. ")
    print("Comenzile trebuie separate prin ; ")
    contor = True
    while contor:
        comenzi = input("Introduceti comenzile (Ajutor, Adauga, Sterge, Afisare, Stop): ")
        functii = comenzi.split(";")
        for functie in functii:
            parametrii = functie.split(",")
            if(parametrii[0] == "Ajutor"):
                print_help()
            elif parametrii[0] == "Adauga":
                lista = adauga(lista, parametrii)
            elif parametrii[0] == "Sterge":
                lista = sterge(lista, parametrii)
            elif parametrii[0] == "Afisare":
                print("Lista de vanzari este: ")
                showall(lista, parametrii)
            elif parametrii[0] == "Stop":
                contor = False
            else:
                print("Comanda incorecta! Reincercati")