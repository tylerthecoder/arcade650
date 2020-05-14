from sprites import Sprite, Rect, Player
from controllers.controller import Controller
from controllers.keyboard import KeyboardController
from controllers.ai import AiController
from typing import List
import json

class World():
  sprites = []
  controllers: List[Controller] = []
  mainSprite = None
  player = None

  sw = 0
  sh = 0

  def loadFromFile(self):
    f = open('./data/world.json')
    data = json.load(f)
    for sprite in data['sprites']:
      if sprite["type"] == "rect":
        self.addSprite(Rect(
          sprite["x"],
          sprite["y"],
          sprite["w"],
          sprite["h"],
          sprite["imgPath"]
        ))

  def __init__(self, sw: int, sh: int):
    self.player = Player(
      sw / 2,
      sh / 2,
      "./images/person1.png",
      "./images/person2.png"
    )
    self.setMainSprite(self.player)

    self.addController(KeyboardController(self.player))

    self.loadFromFile()

    danny = Player(
      sw /2,
      sh /2,
      "./images/danny.png",
      "./images/danny.png"
    )
    self.addSprite(danny)
    self.addController(AiController(danny))

    will = Player(
      sw /2,
      sh /2,
      "./images/will.png",
      "./images/will.png"
    )
    self.addSprite(will)
    self.addController(AiController(will))

    self.addSprite(self.player)
    self.sw = sw
    self.sh = sh

  def addSprite(self, sprite):
    self.sprites.append(sprite)

  def addController(self, controller):
    self.controllers.append(controller)

  def setMainSprite(self, sprite):
    self.mainSprite = sprite

  def update(self, delta_time: int):
    for sprite in self.sprites:
      sprite.update(delta_time)
    for controller in self.controllers:
      controller.update()

  def draw(self, arcade):
    for sprite in self.sprites:
      dx = self.sw/2 - self.mainSprite.x
      dy = self.sh/2 - self.mainSprite.y
      sprite.draw(arcade, dx, dy)

