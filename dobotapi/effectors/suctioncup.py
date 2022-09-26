from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ..dobot import Dobot

from time import sleep

from ..dobot_message import Message


class SuctionCup:
    def __init__(self, bot: "Dobot"):
        self.bot = bot

    def _set_end_effector_suction_cup(
        self, enable: bool = False, is_ctrl_enabled: bool = True
    ) -> Message:
        msg = Message()
        msg.id = 62
        msg.ctrl = 0x03
        msg.params = bytearray([])

        if is_ctrl_enabled:
            msg.params.extend(bytearray([0x01]))
        else:
            msg.params.extend(bytearray([0x00]))

        if enable:
            msg.params.extend(bytearray([0x01]))
        else:
            msg.params.extend(bytearray([0x00]))

        return self.bot._send_command(msg)

    def _suck_air(self, enable: bool, delay_overwrite: Optional[float] = None) -> Any:
        "Toggle state of suction cup"

        if not delay_overwrite:
            delay_overwrite = self.bot.sleep_delay

        response = self._set_end_effector_suction_cup(enable)

        sleep(delay_overwrite)
        return self.bot._extract_cmd_index(response)

    def suck(self) -> None:
        "Starts sucking air"

        self._suck_air(True)

    def idle(self) -> None:
        "Disables effector"

        self._suck_air(False)
        self.bot.delay()
