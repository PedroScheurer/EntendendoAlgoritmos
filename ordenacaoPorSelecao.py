from random import randint

def buscaMenor(arr):
    menor = arr[0]
    menorIndice = 0
    
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menorIndice = i
        
    return menorIndice

def ordenacaoPorSelecao(arr):
    novaArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novaArr.append(arr.pop(menor))
    return novaArr


minha_lista = [randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)]
print(ordenacaoPorSelecao(minha_lista))