grafo = {"voce": ["claire","bob","alice"]}
from collections import deque

#def comecaComP é apenas um exemplo do que é possível buscar
def comecaComP(nome):
    if nome[0] == "P" or nome[0] == "p":
        return True
    else:
        return False


def pesquisa(nome):
    filaDePesquisa = deque()
    filaDePesquisa += grafo[nome]
    pessoasPesquisadas = []
    while filaDePesquisa:
        pessoa = filaDePesquisa.popleft()
        if pessoa not in pessoasPesquisadas:
            if comecaComP(pessoa):
                print(f"{pessoa} começa com p")
                return True
            else:
                filaDePesquisa += grafo[pessoa]
                pessoasPesquisadas.append[pessoa]
    return False
    
#1 - Verifico se tem algo na fila - linha 14
#2 - Atribuo a primeira pessoa da fila à uma variável - linha 15
#3 - Verifico se a pessoa já foi validada - linha 16
#4 - Verifico se é a pessoa que estou buscando - linha 17
#5 - Se for quem eu busco, retorna True - linha 19
#6 - Adiciono dicionário de pessoas de quem eu acabei de validar - linha 21
#7 - Se não for quem eu busco, adiciono na lista de pessoas validadas - linha 22
#8 - Retorna False caso não encontre o que eu busco em ninguém da lista - linha 23 