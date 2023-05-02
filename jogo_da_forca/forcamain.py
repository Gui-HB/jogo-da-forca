from funcoes import limparTela, color, gravar_nomes, competidor_vencedor, desafiante_vencedor


while True:

    limparTela()
    color()

    print("-=-=- Seja Bem-Vindo ao jogo da forca dos gurizes -=-=-")
    print("-=-=- Escolha uma opção meu chapa -=-=-")
    print("------------------------------")
    print("(1) Começar uma partida")
    print("(2) Ver o histórico de partidas")
    print("(0) Sair do jogo")
    print("------------------------------")
    opcao = input()
    if opcao not in ["1", "2", "0"]:
            print("Opção inválida. Tente novamente.")

    if opcao == "0":
        break

    elif opcao == "1":
        limparTela()
        gravar_nomes()
        vidas = 5
    
        limparTela()
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        palavrachave = input("Digite a palavra chave: ")
        dica1 = input("Dica 1: ")
        dica2 = input("Dica 2: ")
        dica3 = input("Dica 3: ")
        dica = 3
        try:
            arquivo_palavra = open("lista_de_participantes.txt", "a")
            arquivo_palavra.write("\n" "Palavra: " +palavrachave)
            arquivo_palavra.close()
        except:
            print("ERRO!")
        input("-=-=- Pressione a tecla Enter -=-=-")
        limparTela()

        # Cria uma lista de asteriscos com a mesma quantidade de elementos que a palavra chave
        numeroletras = ["*" for letra in palavrachave]

        while vidas > 0:
            print("-=-=-=-=-=-=-=-=-=-=-=-")
            print("Palavra chave: ", " ".join(numeroletras))
            print("Você tem mais ",vidas," vidas!")
            print("(1) Jogar!")
            print("(2) Pedir Dica!")
            print("(0) Voltar ao Início!")
            
            opcaoJogo = input("-=-=- Selecione uma opção: ")
            if opcao not in ["1", "2", "0"]:
                    print("Opção inválida. Tente novamente.")
            
            limparTela()

            if opcaoJogo == "0":
                break

            elif opcaoJogo == "1":
                dica = dica-1
                limparTela()
                letra = input("Digite uma letra: ")

                if letra in palavrachave:
                    for i in range(len(palavrachave)):
                        if palavrachave[i] == letra:
                            numeroletras[i] = letra

                    #print("Palavra chave: ", " ".join(numeroletras))

                    if "*" not in numeroletras:
                        limparTela()
                        print("Parabéns, você venceu!")
                        competidor_vencedor()
                        with open('lista_de_participantes.txt', 'r') as arquivo:
                            linhas = arquivo.readlines()[-3:]
                            for linha in linhas:
                                print(linha)
                        input("-=-=- Pressione a tecla Enter -=-=-")
                    
                        break
                else:
                    if vidas == 5:
                        print("Letra não encontrada na palavra chave." "\n" "  +----+" "\n" "  O    |")
                        print("Você errou! Agora você tem",vidas-1,"vidas restantes! ")
                        input("-=-=- Pressione a tecla Enter -=-=-")
                        vidas -= 1 #remove uma vida
                        limparTela()
                    elif vidas == 4:
                        print("Letra não encontrada na palavra chave." "\n" "  +----+" "\n" "  O    |" "\n" "  |    |")
                        print("Você errou! Agora você tem",vidas-1,"vidas restantes! ")
                        input("-=-=- Pressione a tecla Enter -=-=-")
                        vidas -= 1 #remove uma vida
                        limparTela()
                    elif vidas == 3:
                        print("Letra não encontrada na palavra chave." "\n" "  +----+" "\n" "  O    |" "\n" " /|    |")
                        print("Você errou! Agora você tem",vidas-1,"vidas restantes! ")
                        input("-=-=- Pressione a tecla Enter -=-=-")
                        vidas -= 1 #remove uma vida
                        limparTela()
                    elif vidas == 2:
                        print("Letra não encontrada na palavra chave." "\n" "  +----+" "\n" "  O    |" "\n" " /|\   |")
                        print("Você errou! Agora você tem",vidas-1,"vidas restantes! ")
                        input("-=-=- Pressione a tecla Enter -=-=-")
                        vidas -= 1 #remove uma vida
                        limparTela()
                    elif vidas == 1:
                        print("Letra não encontrada na palavra chave."  "\n" "  +----+" "\n" "  O    |" "\n" " /|\   |" "\n" "  /\  ===")
                        print("Você errou! Agora você tem",vidas-1,"vidas restantes! ")
                        input("-=-=- Pressione a tecla Enter -=-=-")
                        vidas -= 1 #remove uma vida
                        limparTela()
                    

            elif opcaoJogo == "2":
                    if dica==3:
                        print("Dica 1: ", dica1, "\n" "Você deve chutar uma letra agora!")
                        input("-=-=- Pressione a tecla Enter -=-=-")
                        limparTela()

                    elif dica==2:
                        print("Dica 1: ", dica1,"\n","Dica 2: ", dica2, "\n" "Você deve chutar uma letra agora!")
                        input("-=-=- Pressione a tecla Enter -=-=-")
                        limparTela()
                    elif dica==1:
                        print("Dica 1: ", dica1,"\n""Dica 2: ", dica2,"\n""Dica 3: ", dica3, "\n" "Você deve chutar uma letra agora!")
                        input("-=-=- Pressione a tecla Enter -=-=-")
                        limparTela()                 
                    else:
                        print("Dica 1: ",dica1,"\n""Dica 2: ",dica2,"\n""Dica 3: ",dica3,"\n""Suas dicas acabaram! :( ")
            else:
                print("Opção inválida, tente novamente.")
        else:
            limparTela()
            print("Que pena, você perdeu.""\n","A palavra chave era : ", palavrachave)
            desafiante_vencedor()
            with open('lista_de_participantes.txt', 'r') as arquivo:
                linhas = arquivo.readlines()[-3:]
                for linha in linhas:
                    print(linha)
            continuar = input("Deseja jogar denovo?""\n""(0) Não""\n""(1) Sim""\n")
            if continuar==0:
                break
            elif continuar==1:
                input("-=-=- Pressione a tecla Enter -=-=-")

    elif opcao == "2":
        limparTela()
        try:
            arquivo = open("lista_de_participantes.txt", "r")
            dados = arquivo.read()
            print(dados)
            input("-=-=- Pressione a tecla Enter para voltar -=-=-")
        except:
            print("Arquivo não Encontrado")
