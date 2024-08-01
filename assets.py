from pyray import init_window
from pyray import load_texture
from pyray import load_font
from pyray import get_fps

screen_width = 768
screen_height = 448
init_window(screen_width, screen_height, f"JOGO DA FORCA - UPE - BETA 1.0.0 - Gambiarra aos montes! - [{get_fps()} FPS]")

textures = {
  "background": [
    load_texture("assets/background/Blue.png"),
    load_texture("assets/background/Green.png"),
    load_texture("assets/background/Purple.png"),
    load_texture("assets/background/Yellow.png"),
    load_texture("assets/background/Pink.png"),
    load_texture("assets/background/Gray.png"),
    load_texture("assets/background/Brown.png")
  ],
  "gui": [
    load_texture("assets/buttons/button.png"),
    load_texture("assets/buttons/button_pressed.png"),
    load_texture("assets/gui/blue_frame.png"),
    load_texture("assets/gui/text_box.png")
  ]
}

fonts = {
  "title": load_font("assets/fonts/Kaph-Regular.ttf"),
  "default": load_font("assets/fonts/m6x11.ttf"),
  "secondary": load_font("assets/fonts/m6x11plus.ttf")
}