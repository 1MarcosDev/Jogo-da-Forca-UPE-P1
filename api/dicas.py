import random
import jogarforca


def dicas():
    dicas = 0
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