from sprites import Sprite
import arcade

class Rect(Sprite):
  def __init__(self, x, y, w, h):
    super().__init__(x, y)
    self.w = w
    self.h = h

  def draw(self, arcade: arcade, dx: int, dy: int):
    arcade.draw_rectangle_filled(
      self.x + dx,
      self.y + dy,
      self.w,
      self.h,
      arcade.color.RED
    )
