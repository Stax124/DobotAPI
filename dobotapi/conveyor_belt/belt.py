from __future__ import annotations

import struct
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..dobot import Dobot

from ..dobot_message import Message
from ..exceptions import DobotException

STEP_PER_CIRCLE = 360.0 / 1.8 * 10.0 * 16.0
MM_PER_CIRCLE = 3.1415926535898 * 36.0


class ConveyorBelt:
    def __init__(self, bot: Dobot):
        self.bot = bot
        self.current_speed: float = 0

    def move(self, speed: float, interface: Literal[0, 1] = 0) -> None:
        "Run conveyor belt at speed ranging from `-1.0` to `1.0`"

        direction = -1 if speed <= 1 else 1
        speed = abs(speed)

        if 0.0 <= speed <= 1.0 and (direction == 1 or direction == -1):
            motor_speed = 70 * speed * STEP_PER_CIRCLE / MM_PER_CIRCLE * direction
            self.current_speed = speed
            self._set_stepper_motor(motor_speed, interface)
        else:
            raise DobotException("Speed must be between -1.0 and 1.0")

    def idle(self):
        "Stops the conveyor belt"

        self.move(speed=0)
        self.current_speed = 0

    def _set_stepper_motor(
        self, speed: float, interface: int = 0, motor_control: bool = True
    ) -> Message:
        msg = Message()
        msg.id = 0x87
        msg.ctrl = 0x03
        msg.params = bytearray([])
        if interface == 1:
            msg.params.extend(bytearray([0x01]))
        else:
            msg.params.extend(bytearray([0x00]))
        if motor_control is True:
            msg.params.extend(bytearray([0x01]))
        else:
            msg.params.extend(bytearray([0x00]))
        msg.params.extend(bytearray(struct.pack("i", int(speed))))
        return self.bot._send_command(msg)
