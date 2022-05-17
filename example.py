from core.effectors.gripper import Gripper
from core.effectors.suctioncup import SuctionCup
from dobot import Position, Dobot
from core.utils import get_coms_port
from time import sleep

port = get_coms_port()
bot = Dobot(port, True)
bot.Connect()

posGrab = Position(324.22, -31.75, 14.42, -5.59)
posRelease = Position(173.75, 268.69, 48.04, 57.11)
posMiddle = Position(239.45, 0.83, 140.17, 0.20)

gripper = Gripper(bot)
sucktioncup = SuctionCup(bot)

moving = False


def main():
    print("Dobot connected")
    bot.set_ir(True)
    while True:
        # gripper.Open()
        # sleep(0.5)
        # gripper.Close()
        # sleep(0.5)
        # gripper.Open()
        # sleep(0.5)
        # gripper.Idle()
        # sucktioncup.Blow()
        # sleep(0.5)
        # sucktioncup.Suck()
        # sleep(0.5)
        # sucktioncup.Blow()
        # sleep(0.5)
        # sucktioncup.Idle()
        if(not bot.get_ir()):
            bot.conveyor_belt(0.25, 1)
        else:
            bot.conveyor_belt(0, 1)
            bot.MoveToPosition(posGrab)
            sucktioncup.Suck()
            bot.MoveToPosition(posMiddle)
            bot.MoveToPosition(posRelease)
            sucktioncup.Blow()
            sucktioncup.Idle()
            bot.MoveToPosition(posMiddle)
        sleep(0.1)


try:
    main()
except KeyboardInterrupt:
    bot.Close()
    print("Dobot disconnected")
