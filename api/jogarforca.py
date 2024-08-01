from temas import pegarTema
from temas import pegaPalavraComTema
from temas import setDificuldade
from temas import abrirArquivo
from records import records
from records import salvarRecords
from records import pegarPontos
import random
import os


def JogarForca():
    print('Bem-vindo ao jogo da forca')
    (abrirArquivo(setDificuldade()))
    nick = input('Digite o seu nick: ')
    tema = pegarTema()
    palavras = pegaPalavraComTema(tema)
    #records = Records('records.txt')

    #dificuldade = input('Escolha a dificuldade (Fácil = 1, Médio = 2, Difícil = 3): ').strip()
    #TentativasMax = {'1':10, '2':8, '3':5}.get(dificuldade, 8)
    TentativasMax = 7
    PalavraSecreta = palavras.lower()
    LetrasCertas = set(PalavraSecreta)
    LetrasUsadas = set()
    Tentativas = 0
    Dicas = 0
    pontuacao = 0

    while Tentativas < TentativasMax and LetrasCertas:
        #DesenhoForca(Tentativas)
        print(f"\nPalavra: {' '.join([letra if letra in LetrasUsadas else '_' for letra in PalavraSecreta])}")
        print(f"O tema é: {tema}")
        print(f"Tentativas restantes: {TentativasMax - Tentativas}")
        print(f"Dicas usadas: {Dicas}")
        jogada = input("Escolha uma letra ou '?' para uma dica: ").strip().lower()

        if jogada == '?':
            if Dicas < 3:
                dica = random.choice(list(LetrasCertas))
                LetrasUsadas.add(dica)
                LetrasCertas.remove(dica)
                Dicas += 1
                Tentativas += 1
                print(f'Dica: a letra {dica} foi revelada.')
            else:
                print('Você já usou todas as suas dicas!')
            continue

        if len(jogada) != 1 or not jogada.isalpha():
            print('Caractere inválido! Digite apenas uma letra.')
            continue

        if jogada in LetrasUsadas:
            print('Você já tentou esta letra!')
            continue
        LetrasUsadas.add(jogada)
        if jogada in LetrasCertas:
            pontuacao += 250
            LetrasCertas.remove(jogada)
            print('Você acertou uma letra!')
        else:
            pontuacao += 0
            Tentativas += 1
            print('Letra errada.')

    if not LetrasCertas:
        pontuacao += 500
        print(f"Parabéns, {nick}! Você adivinhou a palavra '{PalavraSecreta}'.")
        salvarRecords(nick, pontuacao)
    else:
        #DesenhoForca(Tentativas)
        print(f"Você perdeu! A palavra era '{PalavraSecreta}'.")
        salvarRecords(nick, pontuacao)
