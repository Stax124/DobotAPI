from asyncio.windows_events import NULL
import python3_midi as md
import numpy as np
import time as t
from rich.pretty import pprint
from core.dobot import Dobot
from core.utils import get_coms_port
from core.dobot_interfaces import Position
port = get_coms_port()
pprint(port)

bot = Dobot(port, execution_delay=0.4)
bot.connect()
bot.speed(velocity=300, acceleration=300)
pattern = md.read_midifile(
    "C:\\Users\\Admin\\Documents\\midi_dobot\\midi_dobot.mid")[1]

x: list[md.NoteOnEvent] = [
    i for i in pattern if type(i) == md.events.NoteOnEvent]
notes: list[int] = [i.data[0] for i in x]

pprint(notes)

pprint(bot.get_pose().position)
input("C1. Press Enter to continue...")
c3 = bot.get_pose().position
pprint(c3)
input("C2. Press Enter to continue...")
c4 = bot.get_pose().position
pprint(c4)
input("Move UP!!! Press Enter to continue...")

xoff = (c3.x - c4.x) / 7
yoff = (c3.y - c4.y) / 7
zoff = (c3.z - c4.z) / 7

pprint(f"{xoff}, {yoff}, {zoff}")
sharp = {0: 0,
         1: None,
         2: 1,
         3: None,
         4: 2,
         5: 3,
         6: None,
         7: 4,
         8: None,
         9: 5,
         10: None,
         11: 6}

for i in notes:
    # if i%12 == 1 or i%12 == 3 or i%12 == 6 or i%12 == 8 or i%12 == 10:
    #     print("skipnuto")
    #     continue
    b = sharp[i % 12]
    if b == None:
        continue
    crnot = Position(c3.x - b*xoff, c3.y - b*yoff, c3.z -  # type: ignore
                     b*zoff, c3.rotation)  # type: ignore
    crnotup = Position(crnot[0], crnot[1], crnot[2] + 11, c3.rotation)
    pprint(b)
    pprint(crnot)
    pprint(crnotup)
    bot.move_to(*crnotup)
    bot.move_to(*crnot)
    bot.move_to(*crnotup)
