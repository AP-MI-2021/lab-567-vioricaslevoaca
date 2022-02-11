from Domain.Librarie import creeazaLibrarie, getId


def adaugaLibrarie(id, titlu, gen, pret, reducere, lista):
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja")
    if int(id) < 1:
        raise ValueError("ID-ul nu poate fi nul sau negativ!")
    if len(titlu) == 0:
        raise ValueError("Introduceti titlul!")
    if len(gen) == 0:
        raise ValueError("Introduceti genul!")
    if pret < 0:
        raise ValueError("Pretul nu poate fi negativ!")
    if reducere != "gold" and reducere != "silver" and reducere != "none" and reducere != "Gold" and reducere != "Silver" and reducere != "None":
        raise ValueError("Reducere invalida! Introduceti gold, silver sau none")
    librarie = creeazaLibrarie(id, titlu, gen, pret, reducere)
    return lista + [librarie]

def getById(id, librarii):
    for librarie in librarii:
        if getId(librarie) == id:
            return librarie
    return None

def stergeLibrarie(id, lista):
    if getById(id, lista) is None:
        raise ValueError("Nu exista o librarie cu id-ul dat")
    return [librarie for librarie in lista if getId(librarie) != id]

def modificaLibrarie(id, titlu, gen, pret, reducere, lista):
    if getById(id, lista) is None:
        raise ValueError("Nu exista o librarie cu id-ul dat")
    if len(titlu) == 0:
        raise ValueError("Introduceti titlul!")
    if len(gen) == 0:
        raise ValueError("Introduceti genul!")
    if pret < 0:
        raise ValueError("Pretul nu poate fi negativ!")
    if reducere != "gold" and reducere != "silver" and reducere != "none"  and reducere != "Gold" and reducere != "Silver" and reducere != "None":
        raise ValueError("Reducere invalida! Introduceti gold, silver sau none")
    listaNoua = []
    for librarie in lista:
        if getId(librarie) == id:
            librarieNoua = creeazaLibrarie(id, titlu, gen, pret, reducere)
            listaNoua.append(librarieNoua)
        else:
            listaNoua.append(librarie)
    return listaNoua