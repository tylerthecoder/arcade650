import arcade
from helpers import Direction
from typing import Set

class Sprite():
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y
    self.lastX = x;
    self.lastY = y;
    # for calculating animations
    self.distTraveled = 0
    # for collision detection
    self.isTouching: Set[Direction] = set();

    self.tangible = True

  def draw(self, arcade: arcade):
    pass

  # returns a degrees
  def getFacingDirection(self):
    if self.lastX > self.x:
      return Direction.LEFT
    if self.lastX < self.x:
      return Direction.RIGHT
    if self.lastY > self.y:
      return Direction.UP
    if self.lastY < self.y:
      return Direction.DOWN


  # TODO: enforce that you can only move one direction at a time
  def move(self, dx: int, dy: int):
    self.distTraveled += (dx + dy)
    self.lastX, self.lastY = self.x, self.y
    self.x += dx
    self.y += dy
    pass


  def update(self, delta_time):
    pass



