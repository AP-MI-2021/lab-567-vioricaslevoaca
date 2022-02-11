from Domain.Librarie import toString
from Logic.CRUD import adaugaLibrarie, stergeLibrarie, modificaLibrarie
from Logic.functionalitate import discount, modificareGen, pretMinim, ordonareDupaPret, nrTitluriPeGen


def printMenu():
    print("1. Adaugare carte")
    print("2. Stergere carte")
    print("3. Modificare carte")
    print("4. Reduceri silver si gold")
    print("5. Inlocuire gen")
    print("6. Cel mai mic pret pentru fiecare gen")
    print("7. Ordonarea vanzarilor crescator dupa pret")
    print("8. Numarul de titluri pentru fiecare gen")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare carti")
    print("x. Iesire")


def uiAdaugaLibrarie(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul: ")
        titlu = input("Dati titlul: ")
        gen = input("Dati genul: ")
        pret = float(input('Dati pretul: '))
        reducere = input("Dati tipul de reducere: ")
        rezultat = adaugaLibrarie(id, titlu, gen, pret, reducere, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeLibrarie(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul cartii de sters: ")
        rezultat = stergeLibrarie(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaLibrarie(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul cartii de modificat: ")
        titlu = input("Dati noul titlu: ")
        gen = input("Dati noul gen: ")
        pret = float(input('Dati noul pret: '))
        reducere =input("Dati noul tip de reducere: ")
        rezultat = modificaLibrarie(id, titlu, gen, pret, reducere, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiDiscount(lista, undo_list, redo_list):
    rezultat = discount(lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat

def uiModificareGen(lista, undo_list, redo_list):
    numeOriginal=input("Dati titlul operei al carei gen se va modifica: ")
    numeSchimbat=input("Dati genul cu care se va inlocui: ")
    rezultat = modificareGen(numeOriginal, numeSchimbat, lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat

def uiPretMinim(lista):
    rezultat = pretMinim(lista)
    for gen in rezultat:
        print("Genul {} are cel mai mic pret {}".format(gen, rezultat[gen]))

def uiOrdonareDupaPret(lista, undo_list, redo_list):
    rezultat = ordonareDupaPret(lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat

def uiNrTitluriPeGen(lista):
    rezultat = nrTitluriPeGen(lista)
    for gen in rezultat:
        print("Genul {} are {} titluri".format(gen, rezultat[gen]))

def showAll(lista):
    for librarie in lista:
        print(toString(librarie))


def runMenu(lista):
    undo_list = []
    redo_list = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaLibrarie(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = uiStergeLibrarie(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = uiModificaLibrarie(lista, undo_list, redo_list)
        elif optiune == "4":
            lista = uiDiscount(lista, undo_list, redo_list)
        elif optiune == "5":
            lista = uiModificareGen(lista, undo_list, redo_list)
        elif optiune == "6":
            uiPretMinim(lista)
        elif optiune == "7":
            lista = uiOrdonareDupaPret(lista, undo_list, redo_list)
        elif optiune == "8":
            uiNrTitluriPeGen(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")