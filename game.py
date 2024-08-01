from assets import textures
from assets import fonts

from pyray import draw_texture
from pyray import draw_texture_ex

from pyray import draw_text_pro
from pyray import draw_text_ex
from pyray import measure_text_ex

from pyray import close_window
from pyray import get_time
from pyray import get_char_pressed

from pyray import Vector2
from pyray import BLACK
from pyray import WHITE

from utils import text_out

from api.temas import *

class Game:
  def __init__(self, difficulty):
    self.tema = pegarTema(difficulty)
    self.palavra = pegaPalavraComTema(difficulty, self.tema).lower()
    print(self.palavra)
    self.adivinhar = []
    
    for c in self.palavra:
      self.adivinhar.append("_")

    self.lista_char = ""
    self.char = ""
    self.last_char = ""

    self.pontos = 0
    if difficulty == "easy.txt":
      self.acumulador = 10
    elif difficulty == "medium.txt":
      self.acumulador = 25
    elif difficulty == "hard.txt":
      self.acumulador = 50

    self.nickname = "|"

    self.tentativas = 7

  def play(self, menu):
    #print(menu.state)
    self.char = get_char_pressed()
    if self.char != 0:
      #print(chr(self.char))
      self.last_char = chr(self.char)
      if not chr(self.char) in self.lista_char:
        self.lista_char += (chr(self.char))

        for i in range(len(self.palavra)):
          #print(self.palavra[i])
          if self.palavra[i] == chr(self.char):
            self.adivinhar[i] = chr(self.char)

        if chr(self.char) not in self.palavra:
          self.tentativas -= 1
        else:
          self.pontos += self.acumulador

    palavra = ''.join(map(str, self.adivinhar))
    size = measure_text_ex(fonts["default"], palavra, 40, 20)
    point_size = measure_text_ex(fonts["title"], f"Pontos: {self.pontos}", 40, 0)

    if palavra == self.palavra:
      #print("ganhou")
      menu.state = 6
    elif self.tentativas == 0:
      #print("perdeu")
      menu.gameover = True
      menu.state = 6

    text_out(fonts["title"], f"Tema: {self.tema}", 20, 20, 40, 0, WHITE, BLACK)
    text_out(fonts["title"], f"Tentativas: {self.tentativas}", 20, 70, 40, 0, WHITE, BLACK)
    text_out(fonts["title"], f"Letras usadas:\n\n\n{self.lista_char}", 20, 70+50, 40, 0, WHITE, BLACK)
    #text_out(fonts["title"], f"Ultima letra: {self.last_char}", 20, 70+50, 40, 0, WHITE, BLACK)
    text_out(fonts["title"], f"Pontos: {self.pontos}", (768-point_size.x)-20, 20, 40, 0, WHITE, BLACK)
    text_out(fonts["title"], palavra, ((768/2)-(size.x/2)) - 10, 270, 40, 20, WHITE, BLACK)