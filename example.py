from core.effectors.gripper import Gripper
from core.effectors.suctioncup import SuctionCup
from dobot import Position, Dobot
from core.utils import get_coms_port
from time import sleep

port = get_coms_port()
bot = Dobot(port, True)
bot.Connect()

pos1 = Position(188, 5.5, -23, 1.65)
pos2 = Position(186, 74.3, 77, 21.79)
pos3 = Position(137.5, 178.3, -17, 52)

gripper = Gripper(bot)
sucktioncup = SuctionCup(bot)


def main():
    print("Dobot connected")
    while True:
        # gripper.Open()
        # sleep(0.5)
        # gripper.Close()
        # sleep(0.5)
        # gripper.Open()
        # sleep(0.5)
        # gripper.Idle()
        sucktioncup.Blow()
        sleep(0.5)
        sucktioncup.Suck()
        sleep(0.5)
        sucktioncup.Blow()
        sleep(0.5)
        sucktioncup.Idle()


try:
    main()
except KeyboardInterrupt:
    bot.Close()
    print("Dobot disconnected")
