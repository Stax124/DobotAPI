"""
DobotAPI
========

Python API for controlling Dobot Magician and it's addons
"""

from .dobot import Dobot
from .shell import main as run_shell

__all__ = [
    "Dobot",
    "run_shell",
]
