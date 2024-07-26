import random

## Dificuldade = 1 (fácil)
## Dificuldade = 2 (médio)
## Dificuldade = 3 (díficil)
## Dificuldade de acordo com o tamanho da palavra e com a frequência em que a palavra é usada 
## O jogo tem 8 temas (Animais, Frutas, Objetos, Cores, Partes do Corpo, Profissões, Comidas, Países)



## Função para setar a dificuldade do jogo
def setDificuldade():
    global dificuldade
    dificuldade = int(input("Escolha a dificuldade do jogo, (1 - fácil, 2 - médio, 3 - díficil): "))
    #return dificuldade

## Função para abrir o jogo de acordo com a dificuldade 
def abrirArquivo(dificuldade): 
    global arquivo
    if dificuldade == 1:
        arquivo = "easy.txt"
    if dificuldade == 2:
        arquivo = "medium.txt"
    if dificuldade == 3:
        arquivo = "hard.txt"
    #return arquivo    
       
## Bloco para a manipulação da escolha do tema e da escolha da palavra
def separaLinhas(arquivo):
    arquivo = open(arquivo, "r", encoding="utf-8")
    linhas = arquivo.readlines() ## Trasnforma todas as linhas do arquivo em lista 
    linhas = [linha.strip('\n') for linha in linhas] ## Tira os caracteres de quebra de linhas 
    arquivo.close()
    return linhas

## Bloco para definir o tema
def organizarTemas(): 
    linhas_do_arquivo = separaLinhas(arquivo) 
    #print(linhas)
    lista_temas = []
    for i in range(0,92+1, 13): ## Range para coletar os temas seguindo o modelo do arquivo
        lista_temas.append(linhas_do_arquivo[i]) ## Separa todos os temas da lista  
    return lista_temas

## Bloco para capturar o tema
def pegarTema():
    lista_temas = organizarTemas()
    global tematica ## Colocando a variavel tematica no escopo global
    tematica = random.choice(lista_temas) ## Usando a biblioteca random para escolher o tema de forma aleatoria
    return tematica

## Bloco para pegar a palavra de acordo com o tema    
def pegaPalavraComTema (tematica): 
    
    linhas = separaLinhas(arquivo)
    
    if tematica == 'Animais':
        palavras_por_tema = linhas[2:12] ## Slice para o tema Animais 
        palavra = random.choice(palavras_por_tema) 
    if tematica == 'Frutas': 
        palavras_por_tema = linhas[15:25] ## Slice para o tema Frutas 
        palavra = random.choice(palavras_por_tema)
    if tematica == 'Objetos': 
        palavras_por_tema = linhas[28:38] ## Slice para o tema Objetos 
        palavra = random.choice(palavras_por_tema)
    if tematica == 'Cores': 
        palavras_por_tema = linhas[41:51] ## Slice para o tema Cores 
        palavra = random.choice(palavras_por_tema)
    if tematica == 'Partes do Corpo': 
        palavras_por_tema = linhas[54:64] ## Slice para o tema Partes do corpo 
        palavra = random.choice(palavras_por_tema)
    if tematica == 'Profissões': 
        palavras_por_tema = linhas[67:77] ## Slice para o tema Profissões 
        palavra = random.choice(palavras_por_tema)
    if tematica == 'Comidas': 
        palavras_por_tema = linhas[80:90] ## Slice para o tema Comidas 
        palavra = random.choice(palavras_por_tema) 
    if tematica == 'Países': 
        palavras_por_tema = linhas[93:103] ## Slice para o tema países 
        palavra = random.choice(palavras_por_tema) 
    return palavra    
                      
        
 
        
#(setDificuldade()) ## Linha para escolher a dificuldade 
#(abrirArquivo(dificuldade)) ## Linha para abrir o txt seguindo a dificuldade 
#print(separaLinhas(arquivo))
#print(organizarTemas())
#print(pegarTema()) ## Linha para pegar o tema 
#print(pegaPalavraComTema(tematica)) ## Linha para pegar a palavra de acordo com o tema 


