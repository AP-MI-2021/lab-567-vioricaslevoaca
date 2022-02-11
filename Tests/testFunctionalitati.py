from Domain.Librarie import getPret, getGen, getId
from Logic.CRUD import getById, adaugaLibrarie
from Logic.functionalitate import discount, modificareGen, pretMinim, ordonareDupaPret, nrTitluriPeGen

def testDiscount():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)
    lista = adaugaLibrarie("3", "Enigma Otiliei", "Realism", 25, "gold", lista)

    lista = discount(lista)

    assert getPret(getById("1", lista)) == 15
    assert getPret(getById("2", lista)) == 19
    assert getPret(getById("3", lista)) == 22.5

def testModificareGen():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)
    lista = adaugaLibrarie("3", "Enigma Otiliei", "Realism", 25, "gold", lista)

    lista = modificareGen("Ion", "Interbelic", lista)

    assert getGen(getById("1", lista)) == "Traditionalism"
    assert getGen(getById("2", lista)) == "Interbelic"
    assert getGen(getById("3", lista)) == "Realism"

def testPretMinim():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)
    lista = adaugaLibrarie("3", "Enigma Otiliei", "Realism", 25, "gold", lista)

    rezultat = pretMinim(lista)

    assert len(rezultat) == 2
    assert rezultat["Traditionalism"] == 15
    assert rezultat["Realism"] == 20

def testOrdonareDupaPret():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 25, "silver", lista)
    lista = adaugaLibrarie("3", "Enigma Otiliei", "Realism", 20, "gold", lista)

    rezultat = ordonareDupaPret(lista)

    assert getId(rezultat[0]) == "1"
    assert getId(rezultat[1]) == "3"
    assert getId(rezultat[2]) == "2"

def testNrTitluriPeGen():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 25, "silver", lista)
    lista = adaugaLibrarie("3", "Enigma Otiliei", "Realism", 20, "gold", lista)

    rezultat = nrTitluriPeGen(lista)

    assert len(rezultat) == 2
    assert rezultat["Traditionalism"] == 1
    assert rezultat["Realism"] == 2