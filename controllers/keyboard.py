from sprites import Sprite
from sprites import Player
import arcade.key as keys
from controllers.controller import Controller
from helpers import Direction

class KeyboardController(Controller):
  keys = set()
  lastKey = ""


  def __init__(self, sprite: Sprite):
    self.sprite = sprite

  def update(self):
    if keys.W in self.keys and not Direction.UP in self.sprite.isTouching:
      self.sprite.move(0, 10)
    elif keys.S in self.keys and not Direction.DOWN in self.sprite.isTouching:
      self.sprite.move(0, -10)
    elif keys.A in self.keys and not Direction.LEFT in self.sprite.isTouching:
      self.sprite.move(-10, 0)
    elif keys.D in self.keys and not Direction.RIGHT in self.sprite.isTouching:
      self.sprite.move(10, 0)
