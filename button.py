from assets import textures
from pyray import draw_texture_ex

from assets import fonts

from pyray import draw_text_ex
from pyray import measure_text_ex

from pyray import Vector2

from pyray import is_mouse_button_up
from pyray import is_mouse_button_pressed
from pyray import get_mouse_x
from pyray import get_mouse_y

from pyray import BLACK
from pyray import WHITE

import time

def hover(x, y, w, h):
  mx = get_mouse_x()
  my = get_mouse_y()

  return mx >= x and mx <= x + w and my >= y and my <= y + h

def button(text, x, y):
  width = textures["gui"][0].width*1.8
  height = textures["gui"][0].height*1.8
  size = measure_text_ex(fonts["default"], text, 20, 0)
  i = 0

  if hover(x, y, width, height) and is_mouse_button_pressed(0):
      i = 1

  draw_texture_ex(textures["gui"][i], Vector2(x, y), 0, 1.8, WHITE)
  draw_text_ex(fonts["default"], text, Vector2((x+width/2)-size.x/2, (y+height/2)-(size.y/2)-4), 20, 0, BLACK)

  return bool(i)