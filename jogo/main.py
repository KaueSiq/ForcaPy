import qrcode
from PIL import Image
from funcoes import LimparTela, historico, exibir_forca

LimparTela()
while True:
    letrasCertas=[]
    letrasErradas=[]
    vencedor=()
    print("##BEM VINDO AO JOGO DA FORCA##")
    while True:
        desafiante = input("Insira o Nome do Desafiante:")
        competidor = input("Insira o Nome do Competidor:")
        if desafiante and competidor.isalpha():
            break
        else:
            LimparTela()
            print("Entrada inválida!")
    LimparTela()
    while True:
        palavraChave = input("Insira a Palavra chave:").upper()
        if palavraChave.isalpha():
            break
        else:
            LimparTela()
            print("Entrada inválida!")
    dica1 = input("Insira a dica 1:")
    dica2 = input("Insira a dica 2:")
    dica3 = input("Insira a dica 3:")
    chance = 5
    dicas=[dica1, dica2, dica3]
    LimparTela()
    while True:
        print()
        exibir_forca(chance,palavraChave,letrasCertas)
        print()
        print("Deseja JOGAR ou pedir uma DICA?")
        opcao = input()
        if opcao == "dica":
            LimparTela()
            try:
                print("A dica é:" ,(dicas[0]),"." )
                del dicas[0]
            except:
                print("Sem mais dicas!")
            print("Você possue mais ", len(dicas), "dicas.")
        elif opcao == "jogar":
            LimparTela()
            print("Boa sorte!")
        else :
            LimparTela()
            print("Opção inválida, escolha novamente.")
        exibir_forca(chance,palavraChave,letrasCertas)
        print()
        print("A Palavra tem",len(palavraChave), "letras.")

        if len(letrasErradas) > 0:
            print("Letras erradas:", " ".join(letrasErradas)) 
        while True:
            letraTentativa = input("Digite uma letra: ").upper()
            LimparTela()
            print()
            exibir_forca(chance,palavraChave,letrasCertas)
            print()
            print("A Palavra tem",len(palavraChave), "letras.")
            if letraTentativa.isalpha():
                break
        LimparTela()
        if letraTentativa in letrasErradas or letraTentativa in letrasCertas:
            print("Você já tentou essa letra, tente outra agora.")
        elif letraTentativa in palavraChave:
            print("Boa, a letra", letraTentativa.upper(), "está na palavra.")
            letrasCertas.append(letraTentativa)
            if len(letrasCertas) == len(set(palavraChave)):
                print(palavraChave.upper())
                print("Parabéns, você ganhou!")
                print("Mas", palavraChave, "era uma palavra muito fácil.")
                vencedor = competidor
                break
            else:
                print("Agora tente outra letra.")
        else:
            print("Puxa, a letra ", letraTentativa.upper(), "não está na palavra.")
            letrasErradas.append(letraTentativa)
            chance -= 1
            if chance == 0:
                print("Você perdeu! A palavra era", palavraChave,".")
                vencedor = desafiante
                exibir_forca(chance)
                break
            else:
                print("Você só tem mais", chance, "chances.")
    historico(desafiante,competidor,palavraChave,vencedor)
    print("Salvamos seu histórico com sucesso.")
    input("Pressione enter para continuar...")
    LimparTela()
    while True:
        print("Escolha com sabedoria.")
        loop=input("'JOGAR' Para recomeçar o jogo" "\n" "'HISTORICO' Para visualizar historico de partida" "\n" "'SAIR' Para sair do jogo" "\n")
        if loop == "historico":
            try:
                LimparTela()
                arquivo = open("historico.txt", "r")
                dados = arquivo.read()
                print("Aqui vai o histórico de jogos:")
                print(dados)
                input("Pressione Enter para continuar...")
                LimparTela()
            except:
                LimparTela()
                print("Ops, o histórico está indisponivel.")
        elif loop == "jogar":
            palavraChave=()
            letrasErradas=[]
            letrasCertas=[]
            vencedor=()
            desafiante=()
            competidor=()
            LimparTela()
            break
        elif loop == "sair":
            LimparTela()
            link = "https://www.youtube.com/watch?v=eUEqE2RJqhQ"
            qr = qrcode.QRCode(version=None, box_size=10, border=4)
            qr.add_data(link)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.show()
            exit()
        else:
            print("Por favor escolha uma opção válida.")