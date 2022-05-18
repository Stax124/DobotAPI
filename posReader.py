from core.effectors.gripper import Gripper
from core.effectors.suctioncup import SuctionCup
from dobot import Position, Dobot
from core.utils import get_coms_port
from time import sleep

port = get_coms_port()
bot = Dobot(port, True)
bot.connect()

pos1 = Position(188, 5.5, -23, 1.65)
pos2 = Position(186, 74.3, 77, 21.79)
pos3 = Position(137.5, 178.3, -17, 52)

gripper = Gripper(bot)
sucktioncup = SuctionCup(bot)


def main():
    print("Dobot connected")
    bot.ir_toggle(True)
    while True:
        print(bot.get_pose())


try:
    main()
except KeyboardInterrupt:
    bot.close()
    print("Dobot disconnected")
