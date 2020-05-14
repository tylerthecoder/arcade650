from sprites import Sprite
from sprites import Player
import arcade.key as keys
from controllers.controller import Controller

class KeyboardController(Controller):
  keys = set()
  lastKey = ""


  def __init__(self, sprite: Sprite):
    self.sprite = sprite

  def update(self):
    if (isinstance(self.sprite, Player)):
      if keys.W in self.keys and not self.sprite.noUp:
        self.sprite.move(0, 10)
      if keys.S in self.keys and not self.sprite.noDown:
        self.sprite.move(0, -10)
      if keys.A in self.keys and not self.sprite.noLeft:
        self.sprite.move(-10, 0)
      if keys.D in self.keys and not self.sprite.noRight:
        self.sprite.move(10, 0)
    else:
      if keys.W in self.keys:
        self.sprite.move(0, 10)
      if keys.S in self.keys:
        self.sprite.move(0, -10)
      if keys.A in self.keys:
        self.sprite.move(-10, 0)
      if keys.D in self.keys:
        self.sprite.move(10, 0)


