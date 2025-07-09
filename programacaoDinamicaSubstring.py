palavraA = "fish"
palavraB = "hish"

lin = len(palavraA)
col = len(palavraB)
celula = [[0 for _ in range(col+1)] for _ in range(lin+1)]

maxValor = 0



for i in range(1,lin+1):
    for j in range(1,col+1):
        if palavraA[i-1] == palavraB[j-1]:
            celula[i][j] = celula[i-1][j-1] + 1
            maxValor = max(maxValor, celula[i][j])
        else:
            celula[i][j] = 0


for linha in celula:
    print(linha)


