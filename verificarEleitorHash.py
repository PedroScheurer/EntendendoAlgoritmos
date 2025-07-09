votaram = {}

def verificaEleitor(nome):
    if votaram.get(nome):
        print(f"{nome} já votou!")
    else:
        votaram[nome] = True
        print(f"Deixe {nome} votar!")

verificaEleitor("Pedro")
verificaEleitor("Pedro")