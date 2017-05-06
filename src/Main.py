#!/usr/bin/python3

from Screen import *
from Recipe import *
import json


def main():
    Screen.createheader("RocketFuelManager ver 1.0", True)
    calcorread = input("   What can I help you with? [C]alculate a new recipe? [L]oad an old one?: ")
    if calcorread[0].capitalize() == "C":
        newrecipe = Recipe()
        newrecipe.cooktodict()
        newrecipe.createprettyprint()
        saveornot = input("   Want to save? [Y]es or [N]o?: ")
        if saveornot[0].capitalize() == "Y":
            # newrecipe.createsavedata()
            with open(newrecipe.rawdata[0] + ".json", "w") as file:
                file.write(json.dumps(newrecipe.datadict, indent=4, ensure_ascii=False))
    elif calcorread[0].capitalize() == "L":
        pass

while True:
    main()
