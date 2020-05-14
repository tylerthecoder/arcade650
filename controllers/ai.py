from random import randint, uniform
from controllers.controller import Controller

class AiController(Controller):
  dir = 0
  chanceToChangeDir = .01

  def update(self):

    if self.chanceToChangeDir > uniform(0, 1):
      self.dir = randint(0,4)

    if self.dir == 1:
      self.sprite.move(10, 0)
    elif self.dir == 2:
      self.sprite.move(-10, 0)
    elif self.dir == 3:
      self.sprite.move(0, 10)
    elif self.dir == 4:
      self.sprite.move(0, -10)



