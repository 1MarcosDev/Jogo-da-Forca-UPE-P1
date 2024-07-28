from instrucoes import instrucoesforca
import time
from jogarforca import JogarForca
from records import mostrarRecords

# TODO: Implementar funções

def jogar():
    pass

def instrucoes():
    instrucoesforca()

def rank():
    mostrarRecords()

def autores():
    print("""Autores:
    nick do glauco - Glauco ...
    1MarcosDev - Marcos Antônio
    MarcusV4 - Macus ...
    PedroViniciusMD - Pedro Delgado
    """)

def sair():
    pass

opcoes = [
    jogar,
    instrucoes,
    rank,
    autores,
    sair
]

def menu ():
    print("")
    print("-----------------MENU--------------------")
    time.sleep(0.2)
    print("BEM VINDO AO JOGO DA FORCA !!")
    print("")
    time.sleep(0.2)
    print("Escolha uma opção abaixo:")
    time.sleep(0.2)
    print("1 - Jogar")
    time.sleep(0.2)
    print("2 - Instruções")
    time.sleep(0.2)
    print("3 - Ver rank do jogo")
    time.sleep(0.2)
    print("4 - Autores")
    time.sleep(0.2)
    print("5 - Sair")
    print("-----------------------------------------")

    opcoes[int(input()) - 1]()

# OBS --- CHAMAR O MENU PRIMEIRO DO QUE CHAMAR A VARIAVEL OPCAO
