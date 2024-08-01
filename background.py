from pyray import draw_texture
from pyray import WHITE
from assets import textures

class Background:
  def __init__(self, texture = 0):
    self.texture = texture
    self.pos_x = 0

  def draw(self):
    self.pos_x += 1
    
    if self.pos_x > 12*64:
      self.pos_x = 0

    for y in range(7):
      for x in range(24):
        draw_texture(textures["background"][self.texture], (x*64)-self.pos_x, y*64, WHITE)