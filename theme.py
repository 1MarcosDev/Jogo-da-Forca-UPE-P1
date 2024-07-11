import random

class ThemeHandler:
    ### Define dificuldade do jogo
    def setDifficult(self, difficult):
        self.__dificult = difficult

    ### Gera o tema de forma aleatoria
    def genTheme(self):
        i = random.randrange(0, 8) # Gera numero aleatorio entre 0, 8 (quantidade de temas diponiveis)
        self.__themeIndex = i*13   # Pega o tema beaseado no formato do arquivo (a cada tema existem 13 linhas entre eles)
        self.__theme = self.__lines[self.__themeIndex] # Define a variavel do tema
    
    ### Retorna o tema em formato de string
    def getTheme(self):
        return self.__theme

    ### Retorna a palavra baseado no tema
    def getWordByTheme(self):
        i = random.randrange(0,9) # Gera um número entre 0 e 9 (quantidade de palavras disponiveis)
        return self.__lines[self.__themeIndex + 2 + i] ## Retorna o tema (soma mais 2 devido aos espaços em branco entre o tema e as palavras)
    
    ### Construtor
    def __init__(self, difficult = 0):
        self.setDifficult(difficult) # Define dificuldade

        # TODO: Criar função para isso
        if difficult == 0:
            self.__file = open("easy.txt", "r")
        elif difficult == 1:
            self.__file = open("medium.txt", "r")
        elif difficult == 2:
            self.__file = open("hard.txt", "r")

        self.__lines = self.__file.readlines() # Salva todas as linhas do arquivo em uma variavel

        self.genTheme() # Gera o tema

        self.__file.close()