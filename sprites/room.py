from sprites import Sprite
import arcade

class Room():

  def __init__(self, x, y, w, h, imgPath):
    super().__init__(x, y)
    self.w = w
    self.h = h
    self.texture = arcade.load_texture(imgPath)


  def draw(self, arcade: arcade, dx: int, dy: int):
    arcade.draw_texture_rectangle(
      (self.x + dx) , # + self.w/2,
      (self.y + dy), # + self.h/2,
      self.w,
      self.h,
      self.texture
    )