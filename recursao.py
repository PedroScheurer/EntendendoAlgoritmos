def regressiva(a,b):
    '''
    Função recursiva, em que ela mesma se chama.
    Print o valor a até o valor b.
    Valor a tem que ser maior que o b
    param a: primeiro valor
    param b: segundo valor
    return: contagem do primeir valor até o segundo valor
    '''
    print(a)
    if a <= b:
        return
    else:
        regressiva(a - 1,b)


regressiva(10,1)