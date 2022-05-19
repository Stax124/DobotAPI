from core.dobot import Position, Dobot
from core.utils import get_coms_port
import time

port = get_coms_port()
bot = Dobot(port, False)
bot.connect()

#ReleasePosition (x=283.0964660644531, y=19.580909729003906, z=-45.90699768066406, rotation=3.9566705226898193)
#MiddleSPosition (x=97.96730041503906, y=173.89041137695312, z=124.62773895263672, rotation=60.603729248046875)
#GrabPosition (x=27.88756561279297, y=188.13694763183594, z=15.004730224609375, rotation=81.56843566894531)
posGrab = Position(x=27.88756561279297, y=188.13694763183594,
                   z=15.004730224609375, rotation=81.56843566894531)
posMiddle = Position(x=97.96730041503906, y=173.89041137695312,
                     z=124.62773895263672, rotation=60.603729248046875)
posRelease = Position(x=283.0964660644531, y=19.580909729003906,
                      z=-45.90699768066406, rotation=3.9566705226898193)


def main():
    print("Dobot connected")
    bot.ir_toggle(True)
    lastGrab = time.time()
    max_delay = 20

    while True:
        if(not bot.get_ir()):
            bot.conveyor_belt(0.25, 1)
        else:
            bot.conveyor_belt(0, 1)
            bot.move_to_position(posGrab)
            bot.suction_cup.suck()
            bot.move_to_position(posMiddle)
            bot.move_to_position(posRelease)
            bot.suction_cup.blow()
            bot.move_to_position(posMiddle)
            bot.suction_cup.idle()
        time.sleep(0.1)


try:
    main()
except KeyboardInterrupt:
    bot.move_to_position(posMiddle)
    bot.close()
    print("Dobot disconnected")
