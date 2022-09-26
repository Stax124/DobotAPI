from serial.tools import list_ports

from .exceptions import NoComportsAvaliable


def get_coms_port() -> list[str]:
    comports = list_ports.comports()

    if comports:
        devices = [comport.device for comport in comports]

        return devices
    else:
        raise NoComportsAvaliable
