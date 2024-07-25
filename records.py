import random
import os

from utils import *

def records():
    arquivo = open("records.txt", "r")
    linhas = arquivo.read().splitlines()
    arquivo.close()
    return linhas

def pegarPontos():
    recordes = records()
    pontos = []
    for recorde in recordes:
        indice = recorde.find('-')
        pontuacao = recorde[indice+1::1]
        pontos.append(int(pontuacao))
    return pontos

def pegarNomes():
    recordes = records()
    nicks = []
    for recorde in recordes:
        indice = recorde.find('-')
        nickname = recorde[slice(0, indice-1)]
        nicks.append(nickname)
    return nicks

def gerarDicionario():
    dicionario = {}
    listaNomes = pegarNomes()
    listaPontos = pegarPontos()
    for i in range(0, len(listaNomes)):
        dicionario[listaNomes[i]] = listaPontos[i]

    return dicionario

def dicionarioSorteado():
    return sortDicionario(gerarDicionario())

def salvarRecords(nick, pontuacao):
    file = open("records.txt", "a")
    file.write(f"\n{nick} - {pontuacao}")
    file.close()

def mostrarRecords():
    recodes = dicionarioSorteado()
    print('Records:')
    i = 1
    for item in recodes.items():
        print(f"{i}. {item[0]} - {item[1]}")
        i += 1

#print(dicionarioSorteado())
#mostrarRecords()
#salvarRecords("Pedro", 800)