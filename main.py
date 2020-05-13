import arcade
import os

from world import World
from controllers.keyboard import KeyboardController

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Full Screen Example"

# How many pixels to keep as a minimum margin between the charactetr
# and the edge of the screen.
VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    """ Main application class. """

    world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
    controller = KeyboardController(world.player)

    def __init__(self):
        """
        Initializer
        """
        # Open a window in full screen mode. Remove fullscreen=True if
        # you don't want to start this way.
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # This will get the size of the window, and set the viewport to match.
        # So if the window is 1000x1000, then so will our viewport. If
        # you want something different, then use those coordinates instead.
        width, height = self.get_size()
        self.set_viewport(0, width, 0, height)
        arcade.set_background_color(arcade.color.AMAZON)
        self.example_image = arcade.load_texture(":resources:images/tiles/boxCrate_double.png")

    def update(self, delta_time):
        self.world.update(delta_time)
        self.controller.update()


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