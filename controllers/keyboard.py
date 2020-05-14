import arcade.key as keys
from controllers.controller import Controller

class KeyboardController(Controller):
  keys = set()
  lastKey = ""

  def update(self):
    if keys.W in self.keys:
      self.sprite.move(0, 10)
    elif keys.S in self.keys:
      self.sprite.move(0, -10)
    elif keys.A in self.keys:
      self.sprite.move(-10, 0)
    elif keys.D in self.keys:
      self.sprite.move(10, 0)


