#from instrucoes import instrucoesforca
import time
from jogarforca import JogarForca
from records import mostrarRecords

# TODO: Implementar funções

def jogar():
    JogarForca()

def instrucoes():
    print("""
    Bem-vindo ao Jogo da Forca!

    Instruções:
    1. O jogo escolhe uma palavra secreta que você deve adivinhar.
    2. Você verá uma linha para cada letra da palavra secreta.
    3. Em cada rodada, você pode tentar adivinhar uma letra da palavra.
    4. Se a letra estiver na palavra secreta, ela será revelada em todas as posições correspondentes.
    5. Se a letra não estiver na palavra secreta, você perde uma vida.
    6. Você tem um número limitado de vidas dependendo da dificuldade que você escolherá. Cada erro custa uma vida.
    7. O jogo continua até você adivinhar a palavra completa ou perder todas as vidas.
    8. Se você adivinhar a palavra antes de perder todas as vidas, você ganha!
    9. Se você perder todas as vidas antes de adivinhar a palavra, você perde.

    Boa sorte e divirta-se jogando!
    """)

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
