import os 

def LimparTela():
    os.system("cls")

def historico(desafiante, competidor, palavraChave, vencedor):
    arquivo = open("historico.txt", "a")
    if vencedor == competidor:
        arquivo.write(f"vencedor: {competidor}, perdedor: {desafiante}, palavra chave: {palavraChave}")
        arquivo.write("\n")
    else:
        arquivo.write(f"vencedor: {desafiante}, perdedor: {competidor}, palavra chave: {palavraChave}")
        arquivo.write("\n")
    arquivo.close

def exibir_forca(chance, palavraChave,letrasCertas):
    forca = ["   _______",
             "  |/      |",
             "  |      " + (" O" if chance < 5 else ""),
             "  |      " + ("/" if chance < 4 else "")+("|\\" if chance < 3 else ""),
             "  |      " + ("/ " if chance < 2 else "")+("\\" if chance < 1 else ""),
             "  |",
             "__|__"]
    for i in forca:
        print(i)
    for letra in palavraChave:
        if letra in letrasCertas:
                print(letra, end=' ')
        else:
            print("_", end=" ")
print()