from prompt_toolkit.shortcuts import (yes_no_dialog, input_dialog,
                                      message_dialog, radiolist_dialog, button_dialog)
from prompt_toolkit.styles import Style
from core.dobot_interfaces import Position
from dobot import Dobot
from core.utils import get_coms_port

style_dict = {
    "dialog": "bg:#88ff88",
    "dialog frame-label": "bg:#ffffff #000000",
    "dialog.body": "bg:#000000 #00ff00",
    "dialog shadow": "bg:#00aa00",
}

style = Style.from_dict(style_dict)


def main():
    try:
        port = get_coms_port()

        bot = Dobot(port, False)
        bot.connect()

        while True:
            mode = radiolist_dialog(
                title="Dobot shell",
                text="Select mode",
                values=[("get_position", "Get position"),
                        ("set_position", "Set position"),
                        ("gripper", "Gripper"),
                        ("suction_cup", "Suction cup"),
                        ("conveyor_belt", "Conveyor belt"),
                        ("exit", "Exit")
                        ],
                style=style
            ).run()

            if mode == "get_position":
                while True:
                    if yes_no_dialog(
                        title="Continue ?",
                        text=str(bot.get_pose().position),
                        style=style
                    ).run() == False:
                        break

            elif mode == "set_position":
                pos = input_dialog(
                    title="Dobot shell",
                    text="Enter position [x,y,z,r]",
                    style=style
                ).run()

                position = Position(*map(float, pos.split(",")))

                bot.move_to_position(position)

            elif mode == "gripper":
                action = radiolist_dialog(
                    title="Dobot shell",
                    text="Select action",
                    values=[("open", "Open"),
                            ("close", "Close"),
                            ("idle", "Idle"),
                            ],
                    style=style
                ).run()

                if action == "open":
                    bot.gripper.open()
                elif action == "close":
                    bot.gripper.close()
                elif action == "idle":
                    bot.suction_cup.idle()

            elif mode == "suction_cup":
                action = radiolist_dialog(
                    title="Dobot shell",
                    text="Select action",
                    values=[("suck", "Suck"),
                            ("blow", "Blow"),
                            ("idle", "Idle"),
                            ],
                    style=style
                ).run()

                if action == "suck":
                    bot.suction_cup.suck()
                elif action == "blow":
                    bot.suction_cup.blow()
                elif action == "idle":
                    bot.suction_cup.idle()

            elif mode == "conveyor_belt":
                speed = input_dialog(
                    title="Dobot shell",
                    text="Enter speed",
                    style=style
                ).run()
                bot.conveyor_belt(float(speed))

            elif mode == "exit":
                bot.close()
                return

    except Exception as e:
        message_dialog(
            title="Dobot shell",
            text=str(e),
            style=style
        ).run()


main()
