from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ..dobot import Dobot

from time import sleep

from ..dobot_message import Message


class Gripper:
    def __init__(self, bot: "Dobot") -> None:
        self.bot = bot

    def _set_end_effector_gripper(
            self, enable: bool = False, disable: Optional[bool] = False
        ) -> Message:
        msg = Message()
        msg.id = 63
        msg.ctrl = 0x03
        msg.params = bytearray([])

        if disable is False:
            msg.params.extend(bytearray([0x01]))
        else:
            msg.params.extend(bytearray([0x00]))
        
        if enable is True:
            msg.params.extend(bytearray([0x01]))
        else:
            msg.params.extend(bytearray([0x00]))
        return self.bot._send_command(msg)

    def _grip(
            self, enable: bool, disable: Optional[bool] = False, delay_overwrite: Optional[float] = None
        ) -> Any:
        "Toggle state of gripping arm"

        if not delay_overwrite:
            delay_overwrite = self.bot.sleep_delay

        response = self._set_end_effector_gripper(enable, disable)

        sleep(delay_overwrite)
        return self.bot._extract_cmd_index(response)

    def open(self) -> None:
        "Opens gripper"

        self._grip(False)

    def close(self) -> None:
        "Closes gripper"

        self._grip(True)

    def idle(self) -> None:
        "Sets gripper to idle state"

        self._grip(True, True) # First argument doesn't matter
