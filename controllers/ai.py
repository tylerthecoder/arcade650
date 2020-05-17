from random import randint, uniform
from controllers.controller import Controller
from helpers import Direction

class AiController(Controller):
  dir = 0
  chanceToChangeDir = .01

  def update(self):

    if self.chanceToChangeDir > uniform(0, 1):
      self.dir = randint(0,4)

    if self.dir == 1 and not Direction.RIGHT in self.sprite.isTouching:
      self.sprite.move(10, 0)
    elif self.dir == 2 and not Direction.LEFT in self.sprite.isTouching:
      self.sprite.move(-10, 0)
    elif self.dir == 3 and not Direction.UP in self.sprite.isTouching:
      self.sprite.move(0, 10)
    elif self.dir == 4 and not Direction.DOWN in self.sprite.isTouching:
      self.sprite.move(0, -10)



