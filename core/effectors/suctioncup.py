from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.dobot import Dobot


class SuctionCup:
    def __init__(self, bot: Dobot):
        self.bot = bot

    def suck(self):
        "Starts sucking air"

        self.bot._suck(True)
        self.bot.delay()

    def blow(self):
        "Starts blowing air"

        self.bot._grip(False)
        self.bot.delay()

    def idle(self):
        "Disables effector"

        self.bot._suck(False)
        self.bot.delay()
