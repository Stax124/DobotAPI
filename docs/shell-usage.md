# Shell Usage

## Invoking the Shell

::: info
This guide is assuming that you already have dobotapi package installed. If not, please refer to [Installation](/installation) guide.
:::

You can open the TUI with this command:

```bash
python -m dobotapi.shell
```

::: warning
If some error occurs, please refer to [Troubleshooting](/troubleshooting) guide.
:::

At this point, you should see a menu with a few options. Navigate through the menu with the <span style="color: gold">arrow keys</span> and press `Enter` or `Space` to select an option.

To continue, you need to press `Tab` to focus the other elements of the menu. Then, you can press `Enter` or `Space` to select an option.

At this point, a few options are available:

- `Get position`
- `Move`
- `Gripper`
- `Suction cup`
- `Conveyor Belt`
- `Exit`

We will now go through each of them (except `Exit` which is self-explanatory).

## Get Position

First of all, you will be asked if you want to log the positions to a file. If you want to log the positions, select `Yes` and press `Enter`. If you don't want to log the positions, select `No` and press `Enter`.

Once that is done, shell should start displaying the position of the robot. Once you are done, select `No` and press `Enter`.

::: tip
If you selected `Yes` when asked if you wanted to log the positions, you should be able to find a file called `coords.txt` with all the positions logged and ready to be further processed.
:::

## Move

This option allows you to move the robot to a specific position. You will be asked to enter the coordinates of the position you want to move to. You can enter the coordinates in the following format:

`x, y, z, r`

where `x`, `y`, `z` are the coordinates of the position you want to move to and `r` is the rotation of the robot.

## Gripper

::: warning
You need to have a gripper attached to the robot and the correct port for this option to work. See [Ports](/ports) for more information.
:::

This option allows you to control the gripper of the robot. You can select one of the following options:

- `Open`
- `Close`

Operation should be instant.

## Suction Cup

::: warning
You need to have a suction cup attached to the robot and the correct port for this option to work. See [Ports](/ports) for more information.
:::

This option allows you to control the suction cup of the robot. You can select one of the following options:

- `Suck`
- `Idle`

Operation should be instant.

## Conveyor Belt

::: warning
You need to have a conveyor belt attached to the robot and the correct port for this option to work. See [Ports](/ports) for more information.
:::

This option allows you to control the conveyor belt of the robot. You will be asked a few questions:

- `Speed`: You can enter a number between 0 and 1. This number represents the speed of the conveyor belt.
- `Forward`: You can select `Yes` or `No`. If you select `Yes`, the conveyor belt will move forward. If you select `No`, the conveyor belt will move backward.
