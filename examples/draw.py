import logging

from dobotapi.dobot import Dobot
from dobotapi.drawing.svg_handler import Handler as SVGHandler

logging.basicConfig(level=logging.DEBUG)

bot = Dobot(execution_delay=0.15)
bot.connect()
bot.speed(25, 25)
svg = SVGHandler(3)


def main():
    # TODO: Move to the first position on x,y, then move down and start drawing

    paths = svg.get_paths()
    print(paths)
    z = -47
    for path in paths:
        for point in path.points:
            print(point)
            bot.move_to(point.x + 100, point.y, z)


try:
    main()
except KeyboardInterrupt:
    bot.close()
