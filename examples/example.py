import logging as console
import time

import coloredlogs
from dobotapi.dobot import Dobot, Position

coloredlogs.install(
    level=console.DEBUG, fmt="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S"
)


bot = Dobot()
bot.connect()

posGrab = Position(324.22, -31.75, 14.42, -5.59)
posRelease = Position(173.75, 268.69, 48.04, 57.11)
posMiddle = Position(239.45, 0.83, 140.17, 0.20)


def main():
    bot.ir_toggle(True)
    lastGrab = time.time()
    max_delay = 20

    while time.time() - lastGrab < max_delay:
        if not bot.get_ir():
            bot.conveyor_belt.move(0.25)
        else:
            bot.conveyor_belt.move(0)
            bot.move_to_position(posGrab)
            bot.suction_cup.suck()
            bot.move_to_position(posMiddle)
            bot.move_to_position(posRelease)
            bot.suction_cup.suck()
            bot.suction_cup.idle()
            bot.move_to_position(posMiddle)
            lastGrab = time.time()

        time.sleep(0.1)

    else:
        bot.move_to_position(posMiddle)
        bot.close()


try:
    main()
except KeyboardInterrupt:
    bot.move_to_position(posMiddle)
    bot.close()
