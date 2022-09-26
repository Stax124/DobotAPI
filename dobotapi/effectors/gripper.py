from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ..dobot import Dobot

from time import sleep


class Gripper:
    def __init__(self, bot: "Dobot") -> None:
        self.bot = bot

    def _grip(self, enable: bool, delay_overwrite: Optional[float] = None) -> Any:
        "Toggle state of gripping arm"

        if not delay_overwrite:
            delay_overwrite = self.bot.sleep_delay

        response = self.bot._set_end_effector_gripper(enable)

        sleep(delay_overwrite)
        return self.bot._extract_cmd_index(response)

    def open(self) -> None:
        "Opens gripper"

        self._grip(False)

    def close(self) -> None:
        "Closes gripper"

        self._grip(False)
