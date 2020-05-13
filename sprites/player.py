from sprites.sprite import Sprite
import arcade

class Player(Sprite):
  radius = 300
  vx = 0
  vy = 0
  w = 200
  h = 600
  scale = .2

  def __init__(self, x, y):
    super().__init__(x, y)

  def draw(self, arcade: arcade, dx: int, dy: int):
    # Draw the face
    texture = arcade.load_texture("./images/test.bmp")
    arcade.draw_texture_rectangle(
      (self.x + dx) , # + self.w/2,
      (self.y + dy), # + self.h/2,
      self.w,
      self.h,
      texture
    )

  def update(self, delta_time):
    self.x += self.vx * delta_time
    self.y += self.vy * delta_time