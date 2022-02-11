from Domain.Librarie import getId, getTitlu, getGen, getReducere, getPret
from Logic.CRUD import adaugaLibrarie, getById, stergeLibrarie, modificaLibrarie

def testGetById():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is None
    assert getById("4", lista) is None

    lista2 = []
    lista2 = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista2)
    lista2 = adaugaLibrarie("3", "Ion", "Realism", 20, "silver", lista2)
    assert getById("1", lista2) is not None
    assert getById("2", lista2) is None
    assert getById("3", lista2) is not None

def testAdaugaLibrarie():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getTitlu(getById("1", lista)) == "Baltagul"
    assert getGen(getById("1", lista)) == "Traditionalism"
    assert getPret(getById("1", lista)) == 15
    assert getReducere(getById("1", lista)) == "none"


    lista = []
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)

    assert len(lista) == 1
    assert getId(getById("2", lista)) == "2"
    assert getTitlu(getById("2", lista)) == "Ion"
    assert getGen(getById("2", lista)) == "Realism"
    assert getPret(getById("2", lista)) == 20
    assert getReducere(getById("2", lista)) == "silver"

def testStergeLibrarie():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)

    lista = stergeLibrarie("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    try:
        lista = stergeLibrarie("3", lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert getById("2", lista) is not None
    except Exception:
        assert False


    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)
    lista = adaugaLibrarie("3", "Enigma Otiliei", "Realism", 25, "gold", lista)

    lista = stergeLibrarie("2", lista)

    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is not None

def testModificaLibrarie():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)

    lista = modificaLibrarie("1", "Enigma Otiliei", "Realism", 5, "gold", lista)

    librariaUpdatata = getById("1", lista)
    assert getId(librariaUpdatata) == "1"
    assert getTitlu(librariaUpdatata) == "Enigma Otiliei"
    assert getGen(librariaUpdatata) == "Realism"
    assert getPret(librariaUpdatata) == 5
    assert getReducere(librariaUpdatata) == "gold"

    librariaNeupdatata = getById("2", lista)
    assert getId(librariaNeupdatata) == "2"
    assert getTitlu(librariaNeupdatata) == "Ion"
    assert getGen(librariaNeupdatata) == "Realism"
    assert getPret(librariaNeupdatata) == 20
    assert getReducere(librariaNeupdatata) == "silver"


    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    try:
        lista = modificaLibrarie("3", "Enigma Otiliei", "Realism", 5, "gold", lista)
    except ValueError:
        librariaNeupdatata = getById("1", lista)
        assert getId(librariaNeupdatata) == "1"
        assert getTitlu(librariaNeupdatata) == "Baltagul"
        assert getGen(librariaNeupdatata) == "Traditionalism"
        assert getPret(librariaNeupdatata) == 15
        assert getReducere(librariaNeupdatata) == "none"
    except Exception:
        assert False

    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)

    lista = modificaLibrarie("2", "Enigma Otiliei", "Realism", 5, "gold", lista)

    librariaNeupdatata = getById("1", lista)
    assert getId(librariaNeupdatata) == "1"
    assert getTitlu(librariaNeupdatata) == "Baltagul"
    assert getGen(librariaNeupdatata) == "Traditionalism"
    assert getPret(librariaNeupdatata) == 15
    assert getReducere(librariaNeupdatata) == "none"

    librariaUpdatata = getById("2", lista)
    assert getId(librariaUpdatata) == "2"
    assert getTitlu(librariaUpdatata) == "Enigma Otiliei"
    assert getGen(librariaUpdatata) == "Realism"
    assert getPret(librariaUpdatata) == 5
    assert getReducere(librariaUpdatata) == "gold"
