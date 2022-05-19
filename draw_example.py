from os import pathsep
from time import sleep
from core.drawing import svg_handler
from core.effectors.gripper import Gripper
from core.effectors.suctioncup import SuctionCup
from core.dobot import Position, Dobot
from core.utils import get_coms_port
import logging

logging.basicConfig(level=logging.DEBUG)

port = get_coms_port()
bot = Dobot(port, execution_delay=0.25)
bot.connect()
svg = svg_handler.Handler(1)


def main():
    print("Dobot connected")
    paths = svg.get_paths()
    print(paths)
    z = bot.get_pose().position.z
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
