from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dobot import Dobot


class SuctionCup:
    def __init__(self, bot: Dobot):
        self.bot = bot

    def Suck(self):
        "Starts sucking air"

        self.bot._suck(True)
        self.bot.Delay()

    def Blow(self):
        "Starts blowing air"

        self.bot._grip(False)
        self.bot.Delay()

    def Idle(self):
        "Disables effector"

        self.bot._suck(False)
        self.bot.Delay()
