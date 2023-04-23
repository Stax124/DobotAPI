# Effectors

Some of the most notable ones are: <span style="font-weight: 600; color: orange">Suction cup</span> and <span style="font-weight: 600; color: orange">Gripper</span>

Both of these are controlled exaclty the same way. Let's see how to use them.

## Suction cup

::: info
Please check with manual that you have plugged the effector into the correct port.
:::

Suction cup is a simple effector that can be used to pick up small objects by creating a vacuum.

```python{6,10}
import os
from dobotapi import Dobot

bot = Dobot()
bot.connect()

bot.suction_cup.suck() # Enable the suction cup

os.system("pause") # Wait for the user to press any key

bot.suction_cup.idle() # Disable the suction cup

bot.close() # Properly close the connection
```

## Gripper

::: info
Please check with manual that you have plugged the effector into the correct port.
:::

Gripper is a simple effector that grabs items by squeezing them.

```python{6,10}
import os
from dobotapi import Dobot

bot = Dobot()
bot.connect()

bot.gripper.open() # Open the gripper

os.system("pause") # Wait for the user to press any key

bot.gripper.close() # Close the gripper

os.system("pause") # Wait for the user to press any key

bot.gripper.idle() # Return gripper to idle

bot.close() # Properly close the connection
```
