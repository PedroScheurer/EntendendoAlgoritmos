from random import randint
def quicksort(array):
    '''
    Utiliza os fundamentos de dividir para conquistar.
    Em que o pivô do quicksort é o primeiro item da lista.
    Faz duas subarrays, uma menor dos menores que o pivo e outra dos maiores.
    param array: array que será ordenada
    return: array ordenada
    '''
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)


listaDesordenada = []
for i in range(0,10):
    listaDesordenada.append(randint(0,20))

print(f"Lista: {listaDesordenada}")
print(quicksort(listaDesordenada))