from pyray import draw_text_ex
from pyray import Vector2

def text_out(font, text, x, y, size, spacing, color, outcolor):
  draw_text_ex(font, text, Vector2(x-size/10, y), size, spacing, outcolor)
  draw_text_ex(font, text, Vector2(x+size/10, y), size, spacing, outcolor)

  draw_text_ex(font, text, Vector2(x, y-size/10), size, spacing, outcolor)
  draw_text_ex(font, text, Vector2(x, y+size/10), size, spacing, outcolor)

  draw_text_ex(font, text, Vector2(x, y), size, spacing, color)