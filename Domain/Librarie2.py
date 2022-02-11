def creeazaLibrarie(id, titlu, gen, pret, reducere):
    return {
        "id": id,
        "titlu": titlu,
        "gen": gen,
        "pret": pret,
        "reducere": reducere,
    }



def getId(librarie):
    return librarie["id"]

def getTitlu(librarie):
    return librarie["titlu"]

def getGen(librarie):
    return librarie["gen"]

def getPret(librarie):
    return librarie["pret"]

def getReducere(librarie):
    return librarie["reducere"]

def toString(librarie):
    return "Id: {}, Titlu: {}, Gen: {}, Pret: {}, Reducere: {}".format(
        getId(librarie),
        getTitlu(librarie),
        getGen(librarie),
        getPret(librarie),
        getReducere(librarie),
    )