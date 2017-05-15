#!/usr/bin/python3

from Screen import Screen
from Recipe import Recipe


while True:
    Screen.createheader("RocketFuelManager ver 1.0", clear=True)
    calcorread = input(" What can I help you with? [C]alculate a new recipe or [L]oad an old one?: ")
    if calcorread.capitalize() == "C":
        # Calculate a new recipe
        newrecipe = Recipe()
        newrecipe.cooktodict()
        newrecipe.createprettyprint(excludenotes=True)
        newrecipe.prettyprintrecipe(indent=28, newlines=2)
        saveornot = input("\n\n               Want to save? [Y]es or [N]o?: ")
        if saveornot[0].capitalize() == "Y":
            # Save data to Cookbook.db
            newrecipe.createsavedata()
            newrecipe.writetofile()
    elif calcorread.capitalize() == "L":
        # Load a saved recipe
        dateorname = input("\n             Search by [d]ate or by [n]ame?: ")
        if dateorname.capitalize() == "N":
            # Load by name
            recipename = input("\n              Enter the name of your recipe: ")
            loadrecipe = Recipe(loadfromfile=True, identifier=recipename, searchbydate=False)
            if loadrecipe.nonexistent is not True:
                loadrecipe.prettyprintrecipe(regenerate=True, indent=28, newlines=2)
        elif dateorname.capitalize() == "D":
            # Load by date
            recipedate = input("\n              Enter the date of your recipe: ")
            loadrecipe = Recipe(loadfromfile=True, identifier=recipedate, searchbydate=True)
            if loadrecipe.nonexistent is not True:
                loadrecipe.prettyprintrecipe(regenerate=True, indent=28, newlines=2)
    repeatorexit = input("\n\n        Do you want to exit? [Y]es or [N]o?: ")
    if repeatorexit.capitalize() == "Y":
        Screen.clearscreen()
        break
