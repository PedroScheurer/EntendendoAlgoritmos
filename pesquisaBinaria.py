def pesquisaBinaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None
minha_lista = [1,2,3,4,5,6,7,8,9,10]

print(pesquisaBinaria(minha_lista, 10))

def pesquisaLinear(lista, item):
    for i in lista:
        if i == item:
            return lista.index(i)


print(pesquisaLinear(minha_lista, 10))