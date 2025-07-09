from random import randint

def somaItens(lista):
    '''
    Utilizado conceito de dividir para conquistar e recursividade.
    Em que, é chamado a própria função dentro dela do segundo valor em diante.
    Se a lista não tiver nada, retorna 0
    param lista: lista que terá os valores somados
    return: retorna soma dos valores da lista
    '''
    if lista == []:
        return 0
    else:
        return lista[0] + somaItens(lista[1:])
    
listaDesordenada = []
for i in range(0,10):
    listaDesordenada.append(randint(0,20))
    
print(f"Lista: {listaDesordenada}")
print(somaItens(listaDesordenada))