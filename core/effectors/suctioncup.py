from __future__ import annotations
from sympy import im
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dobot import Dobot


class SuctionCup:
    def __init__(self, bot: Dobot):
        "Constructor of gripper"

        self.bot = bot

    def Suck(self):
        "Starts sucking Air"

        self.bot._suck(True)
        self.bot.Delay()

    def Blow(self):
        "Starts blowing Air"

        self.bot._grip(False)
        self.bot.Delay()

    def Idle(self):
        "Disable pneu"

        self.bot._suck(False)
        self.bot.Delay()
