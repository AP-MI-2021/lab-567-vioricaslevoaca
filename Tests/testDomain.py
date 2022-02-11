from Domain.Librarie import creeazaLibrarie, getId, getTitlu, getGen, getPret, getReducere


def testLibrarie():
    librarie = creeazaLibrarie("1", "Baltagul", "Traditionalism", 15, "none")

    assert getId(librarie) == "1"
    assert getTitlu(librarie) == "Baltagul"
    assert getGen(librarie) == "Traditionalism"
    assert getPret(librarie) == 15
    assert getReducere(librarie) == "none"


    librarie2 = creeazaLibrarie("2", "Ion", "Realism", 20, "silver")

    assert getId(librarie2) == "2"
    assert getTitlu(librarie2) == "Ion"
    assert getGen(librarie2) == "Realism"
    assert getPret(librarie2) == 20
    assert getReducere(librarie2) == "silver"


    librarie3 = creeazaLibrarie("3", "Enigma Otiliei", "Realism", 25, "gold")

    assert getId(librarie3) == "3"
    assert getTitlu(librarie3) == "Enigma Otiliei"
    assert getGen(librarie3) == "Realism"
    assert getPret(librarie3) == 25
    assert getReducere(librarie3) == "gold"
