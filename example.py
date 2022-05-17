from core.effectors.gripper import Gripper
from core.effectors.suctioncup import SuctionCup
from dobot import Position, Dobot
from core.utils import get_coms_port
import time

port = get_coms_port()
bot = Dobot(port, False)
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
    lastGrab = time.time()
    max_delay = 20

    while time.time()-lastGrab < max_delay:
        if(not bot.get_ir()):
            # print(time.time()-lastGrab)
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
            lastGrab = time.time()

        time.sleep(0.1)

    else:
        print("Ur Mom Gay LOL")
        bot.MoveToPosition(posMiddle)
        bot.Close()
        print("Dobot disconnected")


try:
    main()
except KeyboardInterrupt:
    bot.MoveToPosition(posMiddle)
    bot.Close()
    print("Dobot disconnected")
