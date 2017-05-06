#!/usr/bin/python3

from Screen import *
from Recipe import *
import json


def main():
    Screen.createheader("RocketFuelManager ver 1.0", True)
    calcorread = input("   Was möchten sie tun? [R]echnen oder [L]aden: ")
    if calcorread[0].capitalize() == "R":
        newrecipe = Recipe()
        print(newrecipe.printlist)
        newrecipe.cooktodict()
        print()
        print(newrecipe.datadict)
        print()
        print(newrecipe.datadictkeylist)
        print()
        newrecipe.createprettyprint()
        print(newrecipe.printlist)
        # newrecipe.prettyprintrecipe(3)
        saveornot = input("   Wollen sie speichern? [J]a oder [N]ein: ")
        if saveornot[0].capitalize() == "J":
            # newrecipe.createsavedata()
            with open("Cookbook.json", "w") as file:
                file.write(json.dumps(newrecipe.datadict, indent=4, ensure_ascii=False))
    elif calcorread[0].capitalize() == "L":
        pass

while True:
    main()
