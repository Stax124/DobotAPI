from serial.tools import list_ports

def get_coms_port() -> str:
    return list_ports.comports()[0].device