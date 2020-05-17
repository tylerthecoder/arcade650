from sprites import Sprite
import arcade
from typing import Set

class Door(Sprite):
  sprites: Set[Sprite]
  rooms: Set[str]

  def __init__(self, x, y, w, h, imgPath, connectionRoom):
    super().__init__(x, y)
    self.w = w
    self.h = h
    self.texture = arcade.load_texture(imgPath)
    self.rooms = set(connectionRoom)
    self.sprites = set()


  def draw(self, dx: int, dy: int):
    arcade.draw_texture_rectangle(
      (self.x + dx) , # + self.w/2,
      (self.y + dy), # + self.h/2,
      self.w,
      self.h,
      self.texture
    )