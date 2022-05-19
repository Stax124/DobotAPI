from core.dobot import Position, Dobot
from core.utils import get_coms_port
import time

port = get_coms_port()
bot = Dobot(port, False)
bot.connect()


def main():
    print("Dobot connected")
    bot.ir_toggle(True)

    while True:
        if(not bot.get_ir()):
            bot.conveyor_belt(0.25, 1)
        else:
            bot.conveyor_belt(0, 1)
        time.sleep(0.1)


try:
    main()
except KeyboardInterrupt:
    bot.close()
    print("Dobot disconnected")
