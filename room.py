from sprites import Sprite, Door, Player, Rect
from typing import List, Tuple
from controllers.controller import Controller
from controllers.ai import AiController
from sprites.utils import detectCollision, spriteDist
import arcade

class Room():
  doors: List[Door]
  sprites: List[Sprite]
  controllers: List[Controller]

  def __init__(self, name: str, floor: Sprite):
    self.name = name
    self.sprites = []
    self.controllers = []
    self.doors = []
    self.floor = floor
    danny = Player(
      floor.x + 300,
      floor.y + 300,
      "./images/danny.png",
      "./images/danny.png"
    )
    self.addSprite(danny)
    self.addController(AiController(danny))

    will = Player(
      floor.x + 300,
      floor.y + 300,
      "./images/will.png",
      "./images/will.png"
    )
    self.addSprite(will)
    self.addController(AiController(will))

  def addSprite(self, sprite: Sprite):
    self.sprites.append(sprite)

  def removeSprite(self, sprite: Sprite):
    self.sprites.remove(sprite)

  def addDoor(self, door: Door):
    self.doors.append(door)

  def addController(self, controller: Controller):
    self.controllers.append(controller)

  # returns an array of tuples. (sprite, name of room to move too)
  def update(self) -> List[Tuple[Sprite, str]]:

    for controller in self.controllers:
      controller.update()

    spritesToBeMoved = []
    isColliding = False

    # clear all the sprites touching set
    for sprite in self.sprites:
      sprite.isTouching.clear()

   # collision logic
    for outerSprite in self.sprites:
      # check if this any other is touching any sprite
      # use isColliding to keep track
      isColliding = False

      # first check to see if it is touching any doors
      for door in self.doors:
        if detectCollision(outerSprite, door, False):
          isColliding = True

      # then check to see if it is colliding with anything in the room
      for innerSprite in self.sprites:
        if outerSprite != innerSprite and detectCollision(outerSprite, innerSprite, True):
          isColliding = True

      # now check to see if it is colliding with the floor
      if detectCollision(self.floor, outerSprite, False):
        isColliding = True

      # this mean the sprite wasn't anywhere in the room, thus it must be outside of the room
      # now we are checking which door the sprite is closest to, and moving them to the other room
      if not isColliding:
        # find the closest door, that is the one they went through
        closestDoor = sorted(self.doors, key=lambda door: spriteDist(door, outerSprite))[0]
        roomsList = list(closestDoor.rooms)
        # find the other roomname
        roomToMoveTo = roomsList[1] if roomsList[0] == self.name else roomsList[0]
        spritesToBeMoved.append((outerSprite, roomToMoveTo))
        self.removeSprite(outerSprite)

    return spritesToBeMoved


  def draw(self, offsetX: int, offsetY: int):
    self.floor.draw(arcade, offsetX, offsetY)
    for sprite in self.sprites:
      sprite.draw(arcade, offsetX, offsetY)

