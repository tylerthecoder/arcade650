from sprites.sprite import Sprite
import arcade

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

  def __init__(self, x, y):
    super().__init__(x, y)

  def draw(self, arcade: arcade, dx: int, dy: int):
    # Draw the face
    texture = arcade.load_texture("./images/test.bmp")
    if (self.x + self.w / 2 < 2500 and self.x - self.w / 2 > -2500 and self.y - self.h / 2 > -2500 and self.y + self.h / 2 < 2500):
      arcade.draw_texture_rectangle(
        (self.x + dx) , # + self.w/2,
        (self.y + dy), # + self.h/2,
        self.w,
        self.h,
        texture
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