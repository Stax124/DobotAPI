from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.dobot import Dobot


class Gripper:
    def __init__(self, bot: Dobot):
        self.bot = bot

    def open(self):
        "Opens gripper"

        self.bot._grip(False)
        self.bot.delay()

    def close(self):
        "Closes gripper"

        self.bot._suck(True)
        self.bot.delay()

    def idle(self):
        "Closes Gripper and sets pneu to idle state"

        self.bot._grip(True)
        self.bot._suck(False)
        self.bot.delay()
