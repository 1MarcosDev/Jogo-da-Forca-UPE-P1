import random

def LerPalavras(arquivo):
    with open(arquivo, 'r') as file:
        palavras = file.read().splitlines()
    return palavras


def EscolherPalavra(palavras):
    return random.choice(palavras)