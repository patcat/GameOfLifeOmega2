from time import sleep
from os import system
from worldtext import *

class Play:

    World_Width = 20
    World_Height = 8

    @classmethod
    def run(cls):
        world = World(
          Play.World_Width,
          Play.World_Height
        )

        print(world.render())

        while True:
            world._tick()
            rendered = world.render()
            system('clear')
            sleep(1)

    @classmethod
    def _f(cls, value):
        return "%.3f" % value

Play.run()