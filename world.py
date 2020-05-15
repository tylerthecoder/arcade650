from sprites import Sprite, Rect, Player, Floor, Door
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
    for room in data['rooms']:
      for sprite in room['sprites']:
        if sprite["type"] == "rect":
          self.addSprite(Rect(
            sprite["x"],
            sprite["y"],
            sprite["w"],
            sprite["h"],
            sprite["imgPath"]
          ))

        if sprite["type"] == "floor":
          self.addSprite(Floor(
            sprite["x"],
            sprite["y"],
            sprite["w"],
            sprite["h"],
            sprite["imgPath"]
          ))

        if sprite["type"] == "door":
          self.addSprite(Door(
            sprite["x"],
            sprite["y"],
            sprite["w"],
            sprite["h"],
            sprite["imgPath"],
            sprite["connectionRoom"]
          ))

  def __init__(self, sw: int, sh: int):
    self.player = Player(
      0,
      0,
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
    # Initially allow players to move wherever they want when draw is called
    for player in self.sprites:
      if (isinstance(player, Player)):
        player.noDown = False
        player.noUp = False
        player.noLeft = False
        player.noRight = False

    # Determine if any player runs into a wall
    for player in self.sprites:
      if (isinstance(player, Player)):
        for sprite in self.sprites:
          if (isinstance(sprite, Rect)):
            self.detectCollision(sprite, player)
          if (isinstance(sprite, Door)):
            self.detectRoomMove(sprite, player)

    # Draw new positions of sprites
    for sprite in self.sprites:
      dx = self.sw / 2 - self.mainSprite.x
      dy = self.sh / 2 - self.mainSprite.y
      sprite.draw(arcade, dx, dy)

  # Check what directions the player can move in
  # If they would run into a wall by going in one direction, don't allow that
  def detectCollision(self, rect: Rect, player: Player):
    rectLeft = rect.x - rect.w / 2
    rectRight = rect.x + rect.w / 2
    rectTop = rect.y + rect.h / 2
    rectBottom = rect.y - rect.h / 2

    playerLeft = player.x - player.w / 2
    playerRight = player.x + player.w / 2
    playerTop = player.y + player.h / 2
    playerBottom = player.y - player.h / 2

    if (playerRight >= rectLeft and playerRight <= rect.x):
      if ( not ((playerTop <= rectBottom) or (playerBottom >= rectTop)) ):
        player.noRight = True
    if (playerLeft <= rectRight and playerLeft >= rect.x):
      if ( not ((playerTop <= rectBottom) or (playerBottom >= rectTop)) ):
        player.noLeft = True
    if (playerTop >= rectBottom and playerTop <= rect.y):
      if ( not ((playerRight <= rectLeft) or (playerLeft >= rectRight)) ):
        player.noUp = True
    if (playerBottom <= rectTop and playerBottom >= rect.y):
      if ( not ((playerRight <= rectLeft) or (playerLeft >= rectRight)) ):
        player.noDown = True

  def detectRoomMove(self, door: Door, player: Player):
    doorLeft = door.x - door.w / 2
    doorRight = door.x + door.w / 2
    doorTop = door.y + door.h / 2
    doorBottom = door.y - door.h / 2

    if (player.x >= doorLeft and player.x <= doorRight and player.y <= doorTop and player.y >= doorBottom and player == self.mainSprite):
      player.prevRoom = player.currRoom
      player.currRoom = -1
      player.enterDoorX = player.x
      player.enterDoorY = player.y
    elif (player == self.mainSprite and player.currRoom == -1):
      # Moved through the door
      if ( ((player.x - door.w / 2) > player.enterDoorX) or ((player.x + door.w / 2) < player.enterDoorX) or ((player.y - door.h / 2) > player.enterDoorY) or ((player.y + door.h / 2) < player.enterDoorY) ):
        player.enterDoorX = -1
        player.enterDoorY = -1
        player.currRoom = door.connectionRoom

      # Went back into original room (still not perfect, but I was just trying to make this work for adding new sprites and dumping old onesw)
      else:
        player.enterDoorX = -1
        player.enterDoorY = -1
        player.currRoom = player.prevRoom


