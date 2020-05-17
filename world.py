from sprites import Sprite, Rect, Player, Floor, Door
from controllers.controller import Controller
from controllers.keyboard import KeyboardController
from controllers.ai import AiController
from typing import Mapping, Set, List
from room import Room
import json

class World():
  rooms: Mapping[str, Room] = {}
  doors: Set[Door] = set()
  mainSprite = None
  player = None

  sw = 0
  sh = 0

  def loadFromFile(self):
    f = open('./data/world.json')
    data = json.load(f)


    for room in data['rooms']:
      roomName = room["id"]
      floor = room["floor"]
      self.addRoom(
        Room(
          roomName,
          Floor(
            floor["x"],
            floor["y"],
            floor["w"],
            floor["h"],
            floor["imgPath"]
          )
        )
      )

      for sprite in room['sprites']:
        if sprite["type"] == "rect":
          sprite = Rect(
            sprite["x"],
            sprite["y"],
            sprite["w"],
            sprite["h"],
            sprite["imgPath"]
          )
          self.rooms[roomName].addSprite(sprite)

    doors = data["doors"]
    for door in doors:
      doorEnt = Door(
          door["x"],
          door["y"],
          door["w"],
          door["h"],
          door["imgPath"],
          door["rooms"]
        )

      self.addDoor(doorEnt)
      for roomName in doorEnt.rooms:
        self.rooms[roomName].addDoor(doorEnt)


  def __init__(self, sw: int, sh: int):
    self.player = Player(
      0,
      0,
      "./images/person1.png",
      "./images/person2.png"
    )
    self.setMainSprite(self.player)

    self.loadFromFile()

    self.rooms["loft"].addSprite(self.mainSprite)
    self.rooms["loft"].addController(KeyboardController(self.player))

    self.sw = sw
    self.sh = sh

  def addRoom(self, room: Room):
    self.rooms[room.name] = room

  def addDoor(self, door: Door):
    self.doors.add(door)

  def setMainSprite(self, sprite):
    self.mainSprite = sprite

  def update(self, delta_time: int):
    # reset the players in the doors
    for door in self.doors:
      door.sprites.clear()

    for room in self.rooms.values():
      spritesToMove = room.update()
      for sprite, roomName in spritesToMove:
        print("Moving", roomName)
        self.rooms[roomName].addSprite(sprite)

  def draw(self, arcade):
    offsetX = self.sw / 2 - self.mainSprite.x
    offsetY = self.sh / 2 - self.mainSprite.y
    for room in self.rooms.values():
      room.draw(offsetX, offsetY)

    for door in self.doors:
      door.draw(offsetX, offsetY)


