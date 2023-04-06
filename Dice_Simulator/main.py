from click import secho, echo
from random import choice
from constants import dice_Data, dice_simulation

secho("Welcome to The Dice Simulator", fg="yellow", bold=True, italic=True, blink=True)

while 1:
    secho("Roll the Dice:- Y/N", fg="red", bold=True, blink=True)
    play = input("")

    if play.lower() == "y":
        secho("\nDice face is :-", fg="red", bold=True, blink=True)
        face = choice(dice_Data)
        secho(face,fg="yellow", bold=True)
        for i in dice_simulation[face]: secho(i,fg="green", bold=True)
    if play.lower() == "n":
        secho("\nDice Simulation in ended", fg="red", bold=True, blink=True)
        break

