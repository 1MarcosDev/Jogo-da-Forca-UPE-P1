from pyray import *
from assets import textures
from background import Background
from button import button
from menu import Menu

import random

#background = Background(random.randint(0, 6))
background = Background(1)
menu = Menu()

set_target_fps(60)

while not window_should_close():
  set_window_title(f"JOGO DA FORCA - UPE - BETA 1.0.0 - Gambiarra aos montes! - [{get_fps()} FPS]")
  begin_drawing()

  clear_background(RAYWHITE)
  draw_text("Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY)

  background.draw()
  menu.draw()

  #draw_fps(10, 10)
  end_drawing()

close_window()
