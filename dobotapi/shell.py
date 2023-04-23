"Shell for quick testing of the Dobot"

from prompt_toolkit.shortcuts import (
    input_dialog,
    message_dialog,
    radiolist_dialog,
    yes_no_dialog,
)
from prompt_toolkit.styles import Style

from .dobot import Dobot
from .dobot_interfaces import Position
from .exceptions import NoComportsAvaliable
from .utils import get_coms_port

style_dict = {
    "dialog": "bg:#88ff88",
    "dialog frame-label": "bg:#ffffff #000000",
    "dialog.body": "bg:#000000 #00ff00",
}

style = Style.from_dict(style_dict)


def main():
    "Default main function"

    try:
        try:
            port = get_coms_port()[0]
        except NoComportsAvaliable:
            port = message_dialog(
                title="No COM ports found",
                text="Probably forgot to install the drivers?",
                style=style,
            ).run()

        if port is None:
            message_dialog(
                title="No port found",
                text="Please connect the Dobot to a USB port.",
                style=style,
            ).run()
            return

        bot = Dobot(port, True)
        bot.connect()

        while True:
            mode = radiolist_dialog(
                title="Dobot shell",
                text="Select mode",
                values=[
                    ("get_position", "Get position"),
                    ("set_position", "Move"),
                    ("gripper", "Gripper"),
                    ("suction_cup", "Suction cup"),
                    ("conveyor_belt", "Conveyor belt"),
                    ("exit", "Exit"),
                ],
                style=style,
            ).run()

            if mode == "get_position":
                file = None

                if yes_no_dialog(
                    title="Get Position",
                    text="Log coords into coords.txt ?",
                    style=style,
                ).run():
                    file = open("coords.txt", "a", encoding="utf-8")
                    file.write("-" * 20 + "\n")

                while True:
                    position = str(bot.get_pose().position)

                    if file:
                        file.write(position + "\n")

                    if (
                        yes_no_dialog(
                            title="Continue ?", text=position, style=style
                        ).run()
                        is False
                    ):
                        break

            elif mode == "set_position":
                pos = input_dialog(
                    title="Dobot shell", text="Enter position [x,y,z,r]", style=style
                ).run()

                position = Position(*map(float, pos.split(",")))

                bot.move_to_position(position)

            elif mode == "gripper":
                action = radiolist_dialog(
                    title="Dobot shell",
                    text="Select action",
                    values=[
                        ("open", "Open"),
                        ("close", "Close"),
                        ("idle", "Idle")
                    ],
                    style=style,
                ).run()

                if action == "open":
                    bot.gripper.open()
                elif action == "close":
                    bot.gripper.close()
                elif action == "idle":
                    bot.gripper.idle()

            elif mode == "suction_cup":
                action = radiolist_dialog(
                    title="Dobot shell",
                    text="Select action",
                    values=[
                        ("suck", "Suck"),
                        ("idle", "Idle"),
                    ],
                    style=style,
                ).run()

                if action == "suck":
                    bot.suction_cup.suck()
                elif action == "idle":
                    bot.suction_cup.idle()

            elif mode == "conveyor_belt":
                speed = input_dialog(
                    title="Dobot shell", text="Enter speed [0-1]", style=style
                ).run()

                forward = yes_no_dialog(
                    title="Dobot shell", text="Forward ?", style=style
                ).run()

                interface = input_dialog(
                    title="Dobot shell",
                    text="Enter interface [0 (default), 1]",
                    style=style,
                ).run()

                forward = 1 if forward else -1
                interface = 1 if interface.strip() == "1" else 0

                bot.conveyor_belt.move(float(speed * forward), interface=interface)

            elif mode == "exit":
                bot.close()
                return

    except Exception as exception:
        message_dialog(title="Dobot shell", text=str(exception), style=style).run()


if __name__ == "__main__":
    main()
