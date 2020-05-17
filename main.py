import arcade
import os
from world import World
from controllers.keyboard import KeyboardController

SPRITE_SCALING = 0.5
SCREEN_TITLE = "Full Screen Example"
# How many pixels to keep as a minimum margin between the charactetr
# and the edge of the screen.
VIEWPORT_MARGIN = 40
MOVEMENT_SPEED = 5
FULLSCREEN = True

class MyGame(arcade.Window):
    """ Main application class. """
    width = 0
    height = 0


    def __init__(self):
        super().__init__(600, 600, SCREEN_TITLE, fullscreen=FULLSCREEN)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.width, self.height = self.get_size()
        self.set_viewport(0, self.width, 0, self.height)
        arcade.set_background_color(arcade.color.AMAZON)
        self.world = World(self.width, self.height)

    def update(self, delta_time):
        self.world.update(delta_time)

    def on_draw(self):
        arcade.start_render()

        left, screen_width, bottom, screen_height = self.get_viewport()

        self.world.draw(arcade)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        KeyboardController.lastKey = key;
        KeyboardController.keys.add(key);
        if key == arcade.key.ESCAPE:
            # User hits f. Flip between full and not full screen.
            self.set_fullscreen(not self.fullscreen)

            # Get the window coordinates. Match viewport to window coordinates
            # so there is a one-to-one mapping.
            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)

    def on_key_release(self, key, modifiers):
        KeyboardController.keys.remove(key)

def main():
    """ Main method """
    MyGame()
    arcade.run()

if __name__ == "__main__":
    main()