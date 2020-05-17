from sprites import Sprite
from sprites.player import Player
from sprites.floor import Floor
from helpers import Direction

def detectCollision(rect1: Sprite, rect2: Sprite, update: bool):

  if not rect1.tangible and not rect2.tangible:
    return False

  rectLeft = rect1.x - rect1.w / 2
  rectRight = rect1.x + rect1.w / 2
  rectTop = rect1.y + rect1.h / 2
  rectBottom = rect1.y - rect1.h / 2

  playerLeft = rect2.x - rect2.w / 2
  playerRight = rect2.x + rect2.w / 2
  playerTop = rect2.y + rect2.h / 2
  playerBottom = rect2.y - rect2.h / 2


  if playerRight >= rectLeft and playerRight <= rectRight:
    if ( not ((playerTop <= rectBottom) or (playerBottom >= rectTop)) ):
      if (update):
        rect2.isTouching.add(Direction.RIGHT)
        rect1.isTouching.add(Direction.LEFT)
      return True
  if playerLeft <= rectRight and playerLeft >= rectLeft:
    if ( not ((playerTop <= rectBottom) or (playerBottom >= rectTop)) ):
      if (update):
        rect2.isTouching.add(Direction.LEFT)
        rect1.isTouching.add(Direction.RIGHT)
      return True
  if playerTop >= rectBottom and playerTop <= rectTop:
    if ( not ((playerRight <= rectLeft) or (playerLeft >= rectRight)) ):
      if (update):
        rect2.isTouching.add(Direction.UP)
        rect1.isTouching.add(Direction.DOWN)
      return True
  if playerBottom <= rectTop and playerBottom >= rectBottom:
    if ( not ((playerRight <= rectLeft) or (playerLeft >= rectRight)) ):
      if (update):
        rect2.isTouching.add(Direction.DOWN)
        rect1.isTouching.add(Direction.UP)
      return True

  return False


def spriteDist(sprite1: Sprite, sprite2: Sprite):
  dx = sprite1.x - sprite2.x
  dy = sprite1.y - sprite2.y
  return (dx**2+dy**2)**(0.5)
