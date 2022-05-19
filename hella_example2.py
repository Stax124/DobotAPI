from core.effectors.gripper import Gripper
from core.effectors.suctioncup import SuctionCup
from core.dobot import Position, Dobot
from core.utils import get_coms_port
import time

port = get_coms_port()
bot = Dobot(port, False)
bot.connect()

sucktioncup = SuctionCup(bot)

#ReleasePosition1 (x=217.86207580566406, y=149.8310546875, z=16.965282440185547, rotation=34.51760482788086)
#ReleasePosition2 (x=208.19082641601562, y=104.1470947265625, z=17.151718139648438, rotation=26.57642936706543)
#MiddleSPosition (x=97.96730041503906, y=173.89041137695312, z=124.62773895263672, rotation=60.603729248046875)
#GrabPosition (x=27.88756561279297, y=188.13694763183594, z=15.004730224609375, rotation=81.56843566894531)
posGrab = Position(x=251.52867126464844, y=-4.765195846557617,
                   z=-42.128211975097656, rotation=-1.0853352546691895)
posMiddle = Position(x=201.03648376464844, y=123.8348159790039,
                     z=116.35449981689453, rotation=31.63231086730957)
posRelease1 = Position(x=209.86575317382812, y=148.5121612548828,
                       z=17.670623779296875, rotation=35.28525161743164)
posRelease2 = Position(x=202.63885498046875, y=101.3697280883789,
                       z=17.314048767089844, rotation=26.57642936706543)


def main():
    print("Dobot connected")
    bot.ir_toggle(True)
    lastGrab = time.time()
    max_delay = 20
    count = 0
    while True:
        if(not bot.get_ir()):
            # print(time.time()-lastGrab)
            bot.conveyor_belt(0, 1)
            pass
        else:
            while(bot.get_ir()):
                pass
            bot.conveyor_belt(0, 1)
            bot.move_to_position(posGrab)
            sucktioncup.suck()
            bot.move_to_position(posMiddle)
            if(count == 0):
                bot.move_to_position(posRelease1)
                count += 1
            elif(count == 1):
                bot.move_to_position(posRelease2)
                count += 1
            sucktioncup.blow()
            bot.move_to_position(posMiddle)
            sucktioncup.idle()
            if(count == 2):
                bot.conveyor_belt(0.25, -1)
                count = 0
                bot.delay()
                bot.delay()
        time.sleep(0.1)


try:
    main()
except KeyboardInterrupt:
    bot.move_to_position(posMiddle)
    bot.close()
    print("Dobot disconnected")
