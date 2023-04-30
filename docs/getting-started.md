# Getting Started

## Checking if everything is working

::: tip
"dobotapi.shell" is a simple CLI tool that allows you to control the robot from the terminal
:::

```bash
python3 -m dobotapi.shell
```

You should be presented with simple menu. If you see it, you are ready to go!

::: details No COM ports found
Please verify that your drivers are installed correctly or try to reboot the computer.
:::

::: details No port found
Dobot is probably not connected. Check your connection and try again.
:::

## Intro

::: warning
Python 3.9 or higher is required
:::

This tutorial will teach you how to connect and control the robot <span style="color: #2cb392">step by step</span>.

### Step 1: Initialize the robot

```python
from dobotapi import Dobot

bot = Dobot()
bot.connect()
bot.close()
```

::: info
`bot.close()` returns the gripper addon and the suction cup to idle, and stops the conveyor belt.
:::

Try running it, if you see no errors, you are ready to go to the next step.

::: details Specifying the port manually
DobotAPI will try to find the robot automatically. If you have multiple robots connected, you can specify the port manually.

```python
bot = Dobot(port=get_com_ports()[0])
```

Replace `0` with the index of the port you want to use.
You can inspec the list by printing the output of `get_com_ports()` function.

```python
from dobotapi import get_com_ports

print(get_com_ports())
```

:::

::: tip
If you want to see what is happening under the hood, you can import `logging` (or `coloredlogs`) module and set the log level to `DEBUG`.

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

:::

Well done, we have successfully connected to the robot! But now what ? Effectors! Let's move on to the next step.
