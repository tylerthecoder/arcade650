import arcade


class FaceSprite():
  x = 300
  y = 300
  vx = 0
  vy = 0
  radius = 200

  def draw(self, arcade):
    # Draw the face
    arcade.draw_circle_filled(
      self.x,
      self.y,
      self.radius,
      arcade.color.YELLOW
    )

  def update(self, delta_time):
    self.x += self.vx * delta_time
    self.y += self.vy * delta_time



