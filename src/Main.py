#!/usr/bin/python3

from Screen import *
from Recipe import *


while True:
    Screen.createheader("RocketFuelManager ver 1.0", clear=True)
    calcorread = input("   What can I help you with? [C]alculate a new recipe? [L]oad an old one?: ")
    if calcorread[0].capitalize() == "C":
        newrecipe = Recipe()
        newrecipe.cooktodict()
        newrecipe.createprettyprint()
        newrecipe.prettyprintrecipe(indent=24, newlines=2)
        saveornot = input("\n\n               Want to save? [Y]es or [N]o?: ")
        if saveornot[0].capitalize() == "Y":
            newrecipe.createsavedata()
            newrecipe.writetofile()
    elif calcorread[0].capitalize() == "L":
        pass

    repeatorexit = input("          Do you want to exit? [Y]es or [N]: ")
    if repeatorexit.capitalize() == "Y":
        break
