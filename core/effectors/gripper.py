from __future__ import annotations
from sympy import im
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dobot import Dobot


class Gripper:
    def __init__(self, bot: Dobot):
        "Constructor of gripper"

        self.bot = bot

    def Open(self):
        "Opens gripper"

        self.bot._grip(False)
        self.bot.Delay()

    def Close(self):
        "Closes gripper"

        self.bot._suck(True)
        self.bot.Delay()

    def Idle(self):
        "Closes Gripper and setting pneu in idle state"

        self.bot._grip(True)
        self.bot._suck(False)
        self.bot.Delay()
