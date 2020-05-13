from sprites import Player
import arcade.key as keys


class KeyboardController():
  keys = set()
  lastKey = ""

  def __init__(self, sprite: Player):
    self.sprite = sprite

  def update(self):
    if keys.W in self.keys:
      self.sprite.move(0, 10)
    elif keys.S in self.keys:
      self.sprite.move(0, -10)
    elif keys.A in self.keys:
      self.sprite.move(-10, 0)
    elif keys.D in self.keys:
      self.sprite.move(10, 0)


