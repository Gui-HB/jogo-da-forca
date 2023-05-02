import os
import time

def limparTela():
    os.system("cls")

def color():
    os.system("color 5")

def criar_base_dados():
    try:
        arquivo = open("lista_de_participantes.txt","r")
        arquivo.close()
    except:
        arquivo = open("lista_de_participantes.txt","w")
        print("Histórico de partidas criado com sucesso!")
        input("Pressione ENTER para continuar!")
        arquivo.close()

def gravar_nomes():
        print("-=-=- A partida está prestes a começar -=-=-")
        desafiante = input("Por gentileza, digite o nome do Desafiante: ")
        competidor = input("E agora, digite o nome do Competidor: ")

        try:
            arquivo_nick = open("lista_de_participantes.txt", "a")
            arquivo_nick.write("\n" "Desafiante: " +desafiante)
            arquivo_nick.write("  " "Competidor: "+competidor)
            arquivo_nick.close()
        except:
            print("ERRO!")
        input("-=-=- Pressione a tecla Enter -=-=-")

def desafiante_vencedor():
        try:
            vencedor = open("lista_de_participantes.txt", "a")
            vencedor.write("\n" +"Desafiante venceu!" "\n")
            vencedor.close()
        except:
            print("ERRO!")
        input("-=-=- Pressione a tecla Enter -=-=-")

def competidor_vencedor():
        try:
            vencedor = open("lista_de_participantes.txt", "a")
            vencedor.write("\n" +"Competidor venceu!" "\n")
            vencedor.close()
        except:
            print("ERRO!")
        input("-=-=- Pressione a tecla Enter -=-=-")


def piscapisca():
     while True:
        cor = 0
        print("### Seja Bem-Vindo ao jogo da forca dos gurizes ###")
        print("### Escolha uma opção meu chapa ###")
        time.sleep(0.001)
        os.system("color "+str(cor))
        cor = cor + 1
        if cor == 10:
            cor = 0
        break
            