# Conveyor Belt

## Introduction

The conveyor belt is a device that is used to move objects from one place to another. It is a very common device in factories and warehouses. It is also used in many other places, such as airports, post offices, etc.
This is miniature version of said thing, but it is still as useful as the real thing.

## Addons

You should get the following addons:

- IR sensor
- Color sensor (Basicly useless)

## Usage

```py{7,11}
from time import sleep
from dobotapi import Dobot

bot = Dobot()

# Speed can range from -1.0 to 1.0 (negative values move the belt in the opposite direction)
bot.conveyor_belt.move(speed=1.0)

sleep(5) # Wait for 5 seconds

bot.conveyor_belt.idle() # Stop the conveyor belt
```
