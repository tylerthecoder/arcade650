from sprites import Sprite, Rect, Player
import json

class World():
  sprites = []
  mainSprite = None
  player = None

  sw = 0
  sh = 0

  def loadFromFile(self):
    f = open('./data/world.json')
    data = json.load(f);
    for sprite in data['sprites']:
      if sprite["type"] == "rect":
        self.addSprite(Rect(
          sprite["x"],
          sprite["y"],
          sprite["w"],
          sprite["h"],
          sprite["imgPath"]
        ));

  def __init__(self, sw: int, sh: int):
    self.player = Player(sw / 2, sh / 2)
    self.setMainSprite(self.player)
    self.loadFromFile()
    self.addSprite(self.player)
    self.sw = sw
    self.sh = sh

  def addSprite(self, sprite):
    self.sprites.append(sprite)

  def setMainSprite(self, sprite):
    self.mainSprite = sprite

  def update(self, delta_time: int):
    for sprite in self.sprites:
      sprite.update(delta_time)

  def draw(self, arcade):
    for sprite in self.sprites:
      dx = self.sw - self.mainSprite.x
      dy = self.sh - self.mainSprite.y
      sprite.draw(arcade, dx, dy)

