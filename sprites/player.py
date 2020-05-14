from sprites.sprite import Sprite, Direction
import arcade
from helpers import directionToAngle

class Player(Sprite):
  radius = 300
  vx = 0
  vy = 0
  w = 100
  h = 300
  scale = .2
  noLeft = False
  noRight = False
  noUp = False
  noDown = False

  def __init__(self, x, y, imgPath1, imgPath2):
    super().__init__(x, y)
    self.texture1 = arcade.load_texture(imgPath1)
    self.texture2 = arcade.load_texture(imgPath2)

  def draw(self, arcade: arcade, dx: int, dy: int):
    # Draw the face

    texture = self.texture1 if int(self.distTraveled / 500) % 2 == 0 else self.texture2

    direction = self.getFacingDirection()

    angle = directionToAngle(direction)

    arcade.draw_texture_rectangle(
      (self.x + dx),
      (self.y + dy),
      self.w,
      self.h,
      texture,
      angle
    )

    if (self.x + self.w / 2 >= 2500):
      self.noRight = True
    else:
      self.noRight = False

    if (self.x - self.w / 2 <= 2500):
      self.noLeft = True
    else:
      self.noLeft = False

    if (self.y + self.h / 2 >= 2500):
      self.noUp = True
    else:
      self.noUp = False

    if (self.y - self.h / 2 <= 2500):
      self.noDown = True
    else:
      self.noDown = False

  def update(self, delta_time):
    if (self.x < 2500 and self.x > -2500):
      self.x += self.vx * delta_time
    if (self.y < 2500 and self.y > -2500):
      self.y += self.vy * delta_time