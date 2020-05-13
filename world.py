from sprites import Sprite, Rect, Player

class World():
  sprites = []
  mainSprite = None
  player = None

  sw = 0
  sh = 0

  def __init__(self, sw: int, sh: int):
    self.player = Player(sw / 2, sh / 2)
    self.addSprite(self.player)
    self.setMainSprite(self.player)
    self.addSprite(Rect(300, 300, 100, 100))
    self.sw = sw
    self.sh = sh

  def addSprite(self, sprite):
    self.sprites.append(sprite)

  def setMainSprite(self, sprite):
    self.mainSprite = sprite

  def update(self, delta_time: int):
    for sprite in self.sprites:
      sprite.update(delta_time);

  def draw(self, arcade):
    for sprite in self.sprites:
      dx = self.sw/2 - self.mainSprite.x
      dy = self.sh/2 - self.mainSprite.y
      sprite.draw(arcade, dx, dy)

