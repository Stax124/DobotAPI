from dobot import Position, Dobot
from core.utils import get_coms_port
import time

port = get_coms_port()
bot = Dobot(port, False)
bot.Connect()


def main():
    print("Dobot connected")
    bot.set_ir(True)
    lastGrab = time.time()
    max_delay = 20

    while True:
        if(not bot.get_ir()):
            # print(time.time()-lastGrab)
            bot.conveyor_belt(0.25, 1)
        else:
            bot.conveyor_belt(0, 1)
        time.sleep(0.1)


try:
    main()
except KeyboardInterrupt:
    bot.Close()
    print("Dobot disconnected")
