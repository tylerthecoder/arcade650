from sprites.face import FaceSprite
import arcade.key as keys


class KeyboardController():
  keys = set()
  lastKey = ""

  def __init__(self, sprite: FaceSprite):
    self.sprite = sprite

  def update(self):
    if keys.W in self.keys:
      self.sprite.y += 10
    if keys.S in self.keys:
      self.sprite.y -= 10
    if keys.A in self.keys:
      self.sprite.x -= 10
    if keys.D in self.keys:
      self.sprite.x += 10


