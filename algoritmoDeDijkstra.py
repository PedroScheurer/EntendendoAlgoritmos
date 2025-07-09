grafo = {
    "inicio": {"a": 6, "b": 2},
    "a": {"fim": 1},
    "b": {"a": 3, "fim": 5},
    "fim": {}
}

infinito = float("inf")

custos = {
    "a": 6,
    "b": 2,
    "fim": infinito
}


pais = {
    "a":"inicio",
    "b":"inicio",
    "fim": None
}

def acheNoCustoMaisBaixo(custos):
    custoMaisBaixo = float("inf")
    nodoCustoMaisBaixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custoMaisBaixo and nodo not in processados:
            custoMaisBaixo = custo
            nodoCustoMaisBaixo = nodo
    return nodoCustoMaisBaixo



processados = []
nodo = acheNoCustoMaisBaixo(custos)

while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novoCusto = custo + vizinhos[n]
        if custos[n] > novoCusto:
            custos[n] = novoCusto
            pais[n] = nodo
    processados.append(nodo)
    nodo = acheNoCustoMaisBaixo(custos)
    print(nodo)
