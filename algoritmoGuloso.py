estadosAbranger = set(["rs","sc","pr","rj","mt","mg","sp","es"])
estacoes = {
    "kum" : set(["rs","mg","sc"]),
    "kdois" : set(["rj","rs","mt"]),
    "ktres" : set(["es","mg","pr"]),
    "kquatro" : set(["mg","sc"]),
    "kcinco" : set(["pr","sp"])
}

estacoesFinal = set()


while estadosAbranger:
    melhorEstacao = None
    estadosCobertos = set()
    for estacao, estados in estacoes.items():
        cobertos = estadosAbranger & estados #intersecção de estados que tenho que abranger e dos estados da estacao selecionada no for
        if len(cobertos) > len(estadosCobertos):
            melhorEstacao = estacao
            estadosCobertos = cobertos

    estadosAbranger -= estadosCobertos
    estacoesFinal.add(melhorEstacao)


print(estacoesFinal)

