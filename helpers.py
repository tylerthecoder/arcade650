from enum import Enum

class Direction(Enum):
  UP = 0
  RIGHT = 1
  DOWN = 2
  LEFT = 3


def directionToAngle(direction: Direction):
  if direction == Direction.UP:
    return 0
  if direction == Direction.DOWN:
    return 180
  if direction == Direction.LEFT:
    return 270
  if direction == Direction.RIGHT:
    return 90
  return 0