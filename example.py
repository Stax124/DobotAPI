from dobot import Position, Dobot
from core.utils import get_coms_port

port = get_coms_port()
bot = Dobot(port, True)
bot.Connect()

pos1 = Position(188, 5.5, -23, 1.65)
pos2 = Position(186, 74.3, 77, 21.79)
pos3 = Position(137.5, 178.3, -17, 52)


def main():
    print("Dobot connected")
    while True:
        bot.MoveToPosition(pos1)
        bot.Grip(True)
        bot.MoveToPosition(pos2)
        bot.MoveToPosition(pos3)
        bot.Grip(False)
        bot.MoveToPosition(pos2)


try:
    main()
except KeyboardInterrupt:
    bot.Close()
    print("Dobot disconnected")
