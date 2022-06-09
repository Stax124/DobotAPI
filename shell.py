"Shell for quick testing of the Dobot"

import os
from prompt_toolkit.shortcuts import (yes_no_dialog, input_dialog,
                                      message_dialog, radiolist_dialog)
from prompt_toolkit.styles import Style
from core.dobot_interfaces import Position
from core.dobot import Dobot
from core.utils import get_coms_port
import json

style_dict = {
    "dialog": "bg:#88ff88",
    "dialog frame-label": "bg:#ffffff #000000",
    "dialog.body": "bg:#000000 #00ff00",
    "dialog shadow": "bg:#00aa00",
}

style = Style.from_dict(style_dict)

config = json.load(open("config.json")) if os.path.exists("config.json") else {
    "midi": []
}


def save():
    "Save config"

    json.dump(config, open("config.json", "w", encoding="utf-8"),
              indent=4, ensure_ascii=False)


def main():
    "Default main function"

    try:
        port = get_coms_port()

        bot = Dobot(port, True)
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
                        ("midi", "MIDI"),
                        ("exit", "Exit")
                        ],
                style=style
            ).run()

            if mode == "get_position":
                file = None

                if yes_no_dialog(
                    title="Get Position",
                    text="Log coords into coords.txt ?",
                    style=style
                ).run():
                    file = open("coords.txt", "a", encoding="utf-8")
                    file.write("-" * 20 + "\n")

                while True:
                    position = str(bot.get_pose().position)

                    if file:
                        file.write(position + "\n")

                    if yes_no_dialog(
                        title="Continue ?",
                        text=position,
                        style=style
                    ).run() is False:
                        if file:
                            file.close()

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

                forward = yes_no_dialog(
                    title="Dobot shell",
                    text="Forward ?",
                    style=style
                ).run()

                interface = input_dialog(
                    title="Dobot shell",
                    text="Enter interface [0 (default), 1]",
                    style=style
                ).run()

                forward = 1 if forward else -1
                interface = int(interface) if interface else 0

                bot.conveyor_belt(
                    float(speed), direction=forward, interface=interface)

            elif mode == "midi":
                # Three options: Add song, remove song, play song
                action = radiolist_dialog(
                    title="Dobot shell",
                    text="Select action",
                    values=[("add_song", "Add song"),
                            ("remove_song", "Remove song"),
                            ("play_song", "Play song"),
                            ],
                    style=style
                ).run()

                if action == "add_song":

                    while True:
                        song = input_dialog(
                            title="Dobot shell",
                            text="Enter song file location",
                            style=style
                        ).run()

                        if os.path.exists(song):
                            config["midi"].append(song)
                            save()
                            break
                        else:
                            x = yes_no_dialog(
                                title="Dobot shell",
                                text="Song file not found. Continue ?",
                                style=style
                            ).run()

                            if x is False:
                                break

                elif action == "remove_song":
                    songs = config["midi"]

                    if not songs:
                        message_dialog(
                            title="Dobot shell",
                            text="No songs to remove",
                            style=style
                        ).run()
                        continue

                    else:
                        song = radiolist_dialog(
                            title="Dobot shell",
                            text="Select song",
                            values=[(i, os.path.basename(i)) for i in songs],
                            style=style
                        ).run()

                        config["midi"].remove(song)
                        save()

            else:
                bot.close()
                return

    except Exception as exception:
        message_dialog(
            title="Dobot shell",
            text=str(exception),
            style=style
        ).run()


main()
