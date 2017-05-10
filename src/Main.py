#!/usr/bin/python3

from Screen import *
from Recipe import *


while True:
    Screen.createheader("RocketFuelManager ver 1.0", clear=True)
    calcorread = input(" What can I help you with? [C]alculate a new recipe or [L]oad an old one?: ")
    if calcorread[0].capitalize() == "C":
        newrecipe = Recipe()
        newrecipe.cooktodict()
        newrecipe.createprettyprint(excludenotes=True)
        newrecipe.prettyprintrecipe(indent=28, newlines=2)
        saveornot = input("\n\n               Want to save? [Y]es or [N]o?: ")
        if saveornot[0].capitalize() == "Y":
            newrecipe.createsavedata()
            newrecipe.writetofile()
    elif calcorread[0].capitalize() == "L":
        recipename = input("\n                 Enter the name of a recipe: ")
        loadrecipe = Recipe(loadfromfile=True, filename=recipename)
        if loadrecipe.nonexistent is not True:
            loadrecipe.prettyprintrecipe(regenerate=True, indent=28, newlines=2)
    repeatorexit = input("\n\n        Do you want to exit? [Y]es or [N]o?: ")
    if repeatorexit.capitalize() == "Y":
        Screen.clearscreen()
        break
