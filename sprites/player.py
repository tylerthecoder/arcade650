from sprites.sprite import Sprite

class Player(Sprite):
  radius = 300
  vx = 0
  vy = 0

  def __init__(self, x, y):
    super().__init__(x, y)

  def draw(self, arcade, dx: int, dy: int):
    # Draw the face
    arcade.draw_circle_filled(
      self.x + dx,
      self.y + dy,
      self.radius,
      arcade.color.YELLOW
    )

  def update(self, delta_time):
    self.x += self.vx * delta_time
    self.y += self.vy * delta_time