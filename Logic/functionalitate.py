from Domain.Librarie import getId, creeazaLibrarie, getGen, getTitlu, getPret, getReducere

def discount(lista):
    listaNoua=[]
    for librarie in lista:
        if getReducere(librarie)=="silver":
            librarieNoua = creeazaLibrarie(
                getId(librarie),
                getTitlu(librarie),
                getGen(librarie),
                getPret(librarie)  - (0.05 * getPret(librarie)),
                getReducere(librarie)
            )
            listaNoua.append(librarieNoua)
        elif getReducere(librarie)=="gold":
            librarieNoua = creeazaLibrarie(
                getId(librarie),
                getTitlu(librarie),
                getGen(librarie),
                getPret(librarie) - (0.1 * getPret(librarie)),
                getReducere(librarie)
            )
            listaNoua.append(librarieNoua)
        else:
            listaNoua.append(librarie)
    return listaNoua

def modificareGen(numeOriginal, numeSchimbat, lista):
    listaNoua = []
    for librarie in lista:
        if getTitlu(librarie) == numeOriginal:
            librarieNoua = creeazaLibrarie(
                getId(librarie),
                getTitlu(librarie),
                numeSchimbat ,
                getPret(librarie),
                getReducere(librarie)
            )
            listaNoua.append(librarieNoua)
        else:
            listaNoua.append(librarie)
    return listaNoua

def pretMinim(lista):
    rezultat = {}
    for librarie in lista:
        gen = getGen(librarie)
        pret = getPret(librarie)
        if gen in rezultat:
            if pret < rezultat[gen]:
                rezultat[gen]=pret
        else:
            rezultat[gen]=pret
    return rezultat

def nrTitluriPeGen(lista):
    rezultat = {}
    aux=[]
    for librarie in lista:
        gen = getGen(librarie)
        ok=0
        titlu = getTitlu(librarie)
        for p in aux:
            if titlu == p:
                ok = 1
        aux.append(titlu)
        if gen in rezultat and ok == 0:
            rezultat[gen] = rezultat[gen] + 1
        else:
            rezultat[gen] = 1
    return rezultat

def ordonareDupaPret(lista):
    return sorted(lista, key = lambda librarie: getPret(librarie))