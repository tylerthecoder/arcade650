from sprites import Sprite

class Controller():
  def __init__(self, sprite: Sprite):
    super().__init__()
    self.sprite = sprite

  def update(self):
    pass