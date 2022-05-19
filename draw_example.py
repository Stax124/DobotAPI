from os import pathsep
from time import sleep
from core.drawing import svg_handler
from core.dobot import Position, Dobot
from core.utils import get_coms_port
import logging

logging.basicConfig(level=logging.DEBUG)

port = get_coms_port()
bot = Dobot(port, execution_delay=0.15)
bot.connect()
bot.speed(25, 25)
svg = svg_handler.Handler(3)


def main():
    # TODO: Move to the first position on x,y, then move down and start drawing

    print("Dobot connected")
    paths = svg.get_paths()
    print(paths)
    z = -47
    for path in paths:
        # print(len(path.points))
        for point in path.points:
            print(point)
            bot.move_to(point.x+100, point.y, z)


try:
    main()
except KeyboardInterrupt:
    bot.close()
    print("Dobot disconnected")
