"Main library for Dobot"

from multiprocessing import RLock
import struct
from time import sleep
from typing import Any, Literal, Optional
import serial
from core.DobotMessage import Message
from core.dobot_interfaces import GPIO, MODE_PTP, Joints, Pose, Position
from core.exception_interfaces import DobotException
from core.effectors.gripper import Gripper
from core.effectors.suctioncup import SuctionCup
import logging as console


MAX_QUEUE_LEN = 32
STEP_PER_CIRCLE = 360.0 / 1.8 * 10.0 * 16.0
MM_PER_CIRCLE = 3.1415926535898 * 36.0


class Dobot():
    "Class for controlling Dobot Magician and it's accessories"

    def __init__(self, port: str, execution_delay: float = 1.5) -> None:
        self.port = port
        self.sleep_delay = execution_delay
        self.gripper = Gripper(self)
        self.suction_cup = SuctionCup(self)
        self._ser = serial.Serial()
        self._lock = RLock()

    def connect(self) -> bool:
        "Connects to dobot and returns true if successful"

        console.info("Connecting to Dobot on port: " + self.port)
        self._ser = serial.Serial(
            self.port,
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS)
        self._set_queued_cmd_start_exec()
        self._set_queued_cmd_clear()
        self._set_ptp_joint_params(200, 200, 200, 200, 200, 200, 200, 200)
        self._set_ptp_coordinate_params(velocity=200, acceleration=200)
        self._set_ptp_jump_params(10, 200)
        self._set_ptp_common_params(velocity=100, acceleration=100)
        return self._ser.isOpen()

    def disconnect(self) -> None:
        "Disconnects robot"

        console.info("Disconnecting dobot")
        if(not self._ser == None and self._ser.isOpen()):
            self._ser.close()

    def close(self) -> None:
        "Exits the dobot program properly"

        self._grip(False)
        self._suck(False)
        self.conveyor_belt(0)
        self.disconnect()

    def move_to(self, x: float, y: float, z: float, r: float = 0., mode: MODE_PTP = MODE_PTP.MOVL_XYZ, delay_overwrite: Optional[float] = None) -> Any:
        "Move robot to exact coordinates"

        if not delay_overwrite:
            delay_overwrite = self.sleep_delay

        cmd = self._set_ptp_cmd(x, y, z, r, mode)

        sleep(delay_overwrite)
        return self._extract_cmd_index(cmd)

    def move_to_position(self, position: Position, mode: MODE_PTP = MODE_PTP.MOVL_XYZ, delay_overwrite: Optional[float] = None) -> Any:
        "Move robot to position"

        if not delay_overwrite:
            delay_overwrite = self.sleep_delay

        cmd = self._set_ptp_cmd(position.x, position.y,
                                position.z, position.rotation, mode)

        sleep(delay_overwrite)
        return self._extract_cmd_index(cmd)

    def get_pose(self) -> Pose:
        "Get current position and state of joints of robot"

        msg = Message()
        msg.id = 10
        response = self._send_command(msg)

        return Pose(
            Position(
                struct.unpack_from('f', response.params, 0)[0],
                struct.unpack_from('f', response.params, 4)[0],
                struct.unpack_from('f', response.params, 8)[0],
                struct.unpack_from('f', response.params, 12)[0]
            ),
            Joints(
                struct.unpack_from('f', response.params, 16)[0],
                struct.unpack_from('f', response.params, 20)[0],
                struct.unpack_from('f', response.params, 24)[0],
                struct.unpack_from('f', response.params, 28)[0]
            )
        )

    def _suck(self, enable: bool, delay_overwrite: Optional[float] = None) -> Any:
        "Toggle state of suction cup"

        if not delay_overwrite:
            delay_overwrite = self.sleep_delay

        response = self._set_end_effector_suction_cup(enable)

        sleep(delay_overwrite)
        return self._extract_cmd_index(response)

    def _grip(self, enable: bool, delay_overwrite: Optional[float] = None) -> Any:
        "Toggle state of gripping arm"

        if not delay_overwrite:
            delay_overwrite = self.sleep_delay

        response = self._set_end_effector_gripper(enable)

        sleep(delay_overwrite)
        return self._extract_cmd_index(response)

    def ir_toggle(self, enable: bool = True, port: GPIO = GPIO.PORT_GP4) -> Any:
        "Turn the IR sensor on or off"

        msg = Message()
        msg.id = 138
        msg.ctrl = 0x03
        msg.params = bytearray([])
        msg.params.extend(bytearray([int(enable)]))
        msg.params.extend(bytearray([port]))
        msg.params.extend(bytearray([0x1]))  # Version1=0, Version2=1
        return self._extract_cmd_index(self._send_command(msg))

    def get_ir(self, port: GPIO = GPIO.PORT_GP4) -> bool:
        "Check if IR sensor is triggered"

        msg = Message()
        msg.id = 138
        msg.ctrl = 0x00
        msg.params = bytearray([])
        msg.params.extend(bytearray([port]))
        msg.params.extend(bytearray([0x01]))
        msg.params.extend(bytearray([0x1]))  # Version1=0, Version2=1
        response = self._send_command(msg)
        console.debug(str(response))
        state = struct.unpack_from('?', response.params, 0)[0]
        return state

    def get_alarms(self):
        "Get alarm state of robot"

        response = self._get_alarms()
        console.debug("Response:" + str(response))
        alarms = struct.unpack_from('I', response.params, 0)
        console.debug("Alarms:" + str(alarms))
        return alarms

    def _extract_cmd_index(self, response: Message) -> Any:
        return struct.unpack_from('I', response.params, 0)[0]

    def _set_ptp_cmd(self, x: float, y: float, z: float, r: float, mode: MODE_PTP) -> Message:
        msg = Message()
        msg.id = 84
        msg.ctrl = 0x03
        msg.params = bytearray([])
        msg.params.extend(bytearray([mode]))
        msg.params.extend(bytearray(struct.pack('f', x)))
        msg.params.extend(bytearray(struct.pack('f', y)))
        msg.params.extend(bytearray(struct.pack('f', z)))
        msg.params.extend(bytearray(struct.pack('f', r)))
        return self._send_command(msg)

    def _set_queued_cmd_start_exec(self) -> Message:
        msg = Message()
        msg.id = 240
        msg.ctrl = 0x01
        return self._send_command(msg)

    def _set_queued_cmd_clear(self) -> Message:
        msg = Message()
        msg.id = 245
        msg.ctrl = 0x01
        return self._send_command(msg)

    def _set_ptp_joint_params(self, v_x: float, v_y: float, v_z: float, v_r: float, a_x: float, a_y: float, a_z: float, a_r: float) -> Message:
        msg = Message()
        msg.id = 80
        msg.ctrl = 0x03
        msg.params = bytearray([])
        msg.params.extend(bytearray(struct.pack('f', v_x)))
        msg.params.extend(bytearray(struct.pack('f', v_y)))
        msg.params.extend(bytearray(struct.pack('f', v_z)))
        msg.params.extend(bytearray(struct.pack('f', v_r)))
        msg.params.extend(bytearray(struct.pack('f', a_x)))
        msg.params.extend(bytearray(struct.pack('f', a_y)))
        msg.params.extend(bytearray(struct.pack('f', a_z)))
        msg.params.extend(bytearray(struct.pack('f', a_r)))
        return self._send_command(msg)

    def _set_ptp_coordinate_params(self, velocity: float, acceleration: float) -> Message:
        msg = Message()
        msg.id = 81
        msg.ctrl = 0x03
        msg.params = bytearray([])
        msg.params.extend(bytearray(struct.pack('f', velocity)))
        msg.params.extend(bytearray(struct.pack('f', velocity)))
        msg.params.extend(bytearray(struct.pack('f', acceleration)))
        msg.params.extend(bytearray(struct.pack('f', acceleration)))
        return self._send_command(msg)

    def _set_ptp_jump_params(self, jump: float, limit: float) -> Message:
        msg = Message()
        msg.id = 82
        msg.ctrl = 0x03
        msg.params = bytearray([])
        msg.params.extend(bytearray(struct.pack('f', jump)))
        msg.params.extend(bytearray(struct.pack('f', limit)))
        return self._send_command(msg)

    def _get_alarms(self) -> Message:
        msg = Message()
        msg.id = 20
        return self._send_command(msg)

    def _set_ptp_common_params(self, velocity: float, acceleration: float) -> Message:
        msg = Message()
        msg.id = 83
        msg.ctrl = 0x03
        msg.params = bytearray([])
        msg.params.extend(bytearray(struct.pack('f', velocity)))
        msg.params.extend(bytearray(struct.pack('f', acceleration)))
        return self._send_command(msg)

    def _set_end_effector_suction_cup(self, enable: bool = False) -> Message:
        msg = Message()
        msg.id = 62
        msg.ctrl = 0x03
        msg.params = bytearray([])
        msg.params.extend(bytearray([0x01]))
        if enable is True:
            msg.params.extend(bytearray([0x01]))
        else:
            msg.params.extend(bytearray([0x00]))
        return self._send_command(msg)

    def _set_end_effector_gripper(self, enable: bool = False) -> Message:
        msg = Message()
        msg.id = 63
        msg.ctrl = 0x03
        msg.params = bytearray([])
        msg.params.extend(bytearray([0x01]))
        if enable is True:
            msg.params.extend(bytearray([0x01]))
        else:
            msg.params.extend(bytearray([0x00]))
        return self._send_command(msg)

    def _set_stepper_motor(self, speed: float, interface: int = 0, motor_control: bool = True) -> Message:
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
        msg.params.extend(bytearray(struct.pack('i', int(speed))))
        return self._send_command(msg)

    def conveyor_belt(self, speed: float, direction: Literal[1, -1] = 1, interface=0) -> None:
        "Configure the conveyor belt speed and direction"

        if 0.0 <= speed <= 1.0 and (direction == 1 or direction == -1):
            motor_speed = 70 * speed * STEP_PER_CIRCLE / MM_PER_CIRCLE * direction
            self._set_stepper_motor(motor_speed, interface)
        else:
            raise DobotException("Wrong Parameter")

    def speed(self, velocity: float = 100., acceleration: float = 100.) -> None:
        "Configure the speed of the robot"

        self._set_ptp_common_params(velocity, acceleration)
        self._set_ptp_coordinate_params(velocity, acceleration)

    def wait(self, ms) -> None:
        "Let robot wait for certain time"

        self._set_wait_cmd(ms)

    def _set_wait_cmd(self, ms: int) -> Message:
        msg = Message()
        msg.id = 110
        msg.ctrl = 0x03
        msg.params = bytearray(struct.pack('I', ms))
        return self._send_command(msg)

    def _send_command(self, msg: Message) -> Message:
        if(self._ser != None and self._ser.isOpen):
            with self._lock:
                self._ser.reset_input_buffer()
                self._send_message(msg)
                r_msg = self._read_message()
            if r_msg is None:
                console.debug("No response")
                return Message()
            else:
                return r_msg

        raise DobotException("Serial port is not open")

    def _send_message(self, message: Message) -> None:
        console.debug("Sending: " + str(message))
        if(self._ser != None and self._ser.isOpen()):
            with self._lock:
                self._ser.write(message.bytes())

    def _read_message(self) -> Optional[Message]:
        if(self._ser == None):
            return None
        # Search for begin
        begin_found = False
        last_byte = None
        tries = 5
        while not begin_found and tries > 0:
            current_byte = ord(self._ser.read(1))
            if current_byte == 170:
                if last_byte == 170:
                    begin_found = True
            last_byte = current_byte
            tries = tries - 1
        if begin_found:
            payload_length = ord(self._ser.read(1))
            payload_checksum = self._ser.read(payload_length + 1)
            if len(payload_checksum) == payload_length + 1:
                b = bytearray([0xAA, 0xAA])
                b.extend(bytearray([payload_length]))
                b.extend(payload_checksum)
                msg = Message(b)
                return msg
        return None

    def delay(self, delay: Optional[float] = None) -> None:
        "Wait for certain amount of time, if no delay is given, wait bots default delay"

        if delay:
            sleep(delay)
        else:
            sleep(self.sleep_delay)
