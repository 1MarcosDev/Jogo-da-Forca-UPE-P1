from assets import textures
from assets import fonts

from pyray import draw_texture
from pyray import draw_texture_ex

from pyray import draw_text_pro
from pyray import measure_text_ex

from pyray import is_key_pressed
from pyray import get_char_pressed
from pyray import close_window
from pyray import get_time

from pyray import Vector2
from pyray import BLACK
from pyray import WHITE
from pyray import KEY_BACKSPACE

from math import cos

from utils import text_out

from button import button

from api.records import dicionarioSorteado
from api.records import salvarRecords

from game import Game

class Menu:
  def __init__(self):
    self.state = 0
    #self.game = Game("easy.txt")
    self.gameover = False

  def buttons(self):
    if button("Jogar", (768//2)-90, 150):
      self.state = 4
    
    if button("Ranking", (768//2)-90, 150+70):
      self.state = 3
    
    if button("Como jogar", (768//2)-90, 150+70*2):
      self.state = 2
    
    if button("Sair", (768//2)-90, 150+70*3):
      close_window()
    
    if button("Autores", 668-90, 150+70*3):
      self.state = 1

  def title(self):
    title = "JOGO DA FORCA"
    vertion = "Beta 1.0.0"
    size = measure_text_ex(fonts["title"], title, 60, 0)
    vertion_size = measure_text_ex(fonts["secondary"], vertion, 20, 0)
    subsize = measure_text_ex(fonts["title"], title, 60, 0)
    
    draw_text_pro(fonts["title"], title, Vector2((768/2), 80-8), Vector2(size.x // 2, 30), cos(get_time())*4, 60, 0, BLACK)

    draw_text_pro(fonts["title"], title, Vector2((768/2)-8, 80-8), Vector2(size.x // 2, 30), cos(get_time())*4, 60, 0, BLACK)
    draw_text_pro(fonts["title"], title, Vector2((768/2)-8, 80+8), Vector2(size.x // 2, 30), cos(get_time())*4, 60, 0, BLACK)

    draw_text_pro(fonts["title"], title, Vector2((768/2)+8, 80-8), Vector2(size.x // 2, 30), cos(get_time())*4, 60, 0, BLACK)
    draw_text_pro(fonts["title"], title, Vector2((768/2)+8, 80+8), Vector2(size.x // 2, 30), cos(get_time())*4, 60, 0, BLACK)

    draw_text_pro(fonts["title"], title, Vector2((768/2), 80+8), Vector2(size.x // 2, 30), cos(get_time())*4, 60, 0, BLACK)

    draw_text_pro(fonts["title"], title, Vector2(768/2, 80), Vector2(size.x // 2, 30), cos(get_time())*4, 60, 0, WHITE)

    self.buttons()

    text_out(fonts["secondary"], vertion, 768-vertion_size.x-10, 10, 20, 0, WHITE, BLACK)

  def authors(self):
    text = """
    Glauco Siqueira
    Marcos Antonio
    Marcus Vinicius
    Pedro Delgado
    """
    width = textures["gui"][2].width*4
    draw_texture_ex(textures["gui"][2], Vector2((768/2)-width/2, 20), 0, 4, WHITE)

    for line in text.splitlines():
      text_out(fonts["secondary"], line, (768/2)-132, 50+(text.splitlines().index(line)*40), 40, 0, WHITE, BLACK)

    if button("Voltar", (768//2)-90, 330):
      self.state = 0

  def tutorial(self):
    text = """
    1. Uma palavra aleatoria sera escolhida
    2. Tente adivinhar uma letra da palavra
    3. Se voce acertar, ela ira aparecer na palavra
    4. Se voce errar, voce perde uma vida
    5. Voce tem um numero limitado de vidas
    6. As vidas sao definidas pela dificuldade
    7. O jogo termina quando voce adivinhar a palavra
    8. Se voce perder todas as vidas, você perde


                Boa sorte e divirta-se jogando!
    """
    width = textures["gui"][2].width*4
    draw_texture_ex(textures["gui"][2], Vector2((768/2)-width/2, 20), 0, 4, WHITE)

    for line in text.splitlines():
      text_out(fonts["secondary"], line, (768/2)-200, 50+(text.splitlines().index(line)*20), 22, 0, WHITE, BLACK)

    if button("Voltar", (768//2)-90, 330):
      self.state = 0

  def ranking(self):
    recodes = dicionarioSorteado()
    width = textures["gui"][2].width*4
    draw_texture_ex(textures["gui"][2], Vector2((768/2)-width/2, 20), 0, 4, WHITE)

    i = 1
    for item in recodes.items():
      text_out(fonts["secondary"], f"{i}. {item[0]} - {item[1]}", (768/2)-90, 50+(i*28), 32, 0, WHITE, BLACK)
      i += 1

    if button("Voltar", (768//2)-90, 330):
      self.state = 0

  def difficulty(self):
    text_out(fonts["title"], "Dificuldade:", (768//2)-280, 80, 75, 0, WHITE, BLACK)

    if button("Facil", (768//2)-90-180, 150+70):
      self.game = Game("easy.txt")
      self.state = 5

    if button("Medio", (768//2)-90, 150+70):
      self.game = Game("medium.txt")
      self.state = 5

    if button("Dificil", (768//2)-90+180, 150+70):
      self.game = Game("hard.txt")
      self.state = 5

    if button("Voltar", (768//2)-90, 150+70*3):
      self.state = 0
  
  def scores(self):
    if self.gameover:
      final_message = "Voce perdeu..."
      final_size = measure_text_ex(fonts["title"], final_message, 40, 0)
    else:
      final_message = "Voce ganhou!"
      final_size = measure_text_ex(fonts["title"], final_message, 40, 0)
    
    width = textures["gui"][2].width*4

    self.char = get_char_pressed()
    if self.char != 0 and len(self.game.nickname) < 13:
      self.game.nickname = self.game.nickname[:-1]
      self.game.nickname += chr(self.char)
      self.game.nickname += "|"

    if is_key_pressed(KEY_BACKSPACE):
      self.game.nickname = self.game.nickname[:-2]
      self.game.nickname += "|"

    draw_texture_ex(textures["gui"][2], Vector2((768/2)-width/2, 20), 0, 4, WHITE)
    draw_texture_ex(textures["gui"][3], Vector2(50+(768/2)-width/2, 220), 0, 3, WHITE)

    text_out(fonts["title"], final_message, (768/2)-final_size.x/2, 35, 40, 0, WHITE, BLACK)
    text_out(fonts["secondary"], f"Pontos: {self.game.pontos}", (768/2)-150, 80, 60, 0, WHITE, BLACK)
    text_out(fonts["secondary"], f"Digite seu nome:", (768/2)-150, 140, 60, 0, WHITE, BLACK)
    text_out(fonts["secondary"], self.game.nickname, (768/2)-120, 235, 60, 0, WHITE, BLACK)

    if button("Salvar e voltar", (768//2)-90, 330):
      self.game.nickname = self.game.nickname[:-1]
      salvarRecords(self.game.nickname, self.game.pontos)
      self.state = 0

  def draw(self):
    if self.state == 0:
      self.title()
    elif self.state == 1:
      self.authors()
    elif self.state == 2:
      self.tutorial()
    elif self.state == 3:
      self.ranking()
    elif self.state == 4:
      self.difficulty()
    elif self.state == 5:
      self.game.play(self)
    elif self.state == 6:
      self.scores()
