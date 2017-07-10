#!/usr/bin/env python3


import tc

from Recipe import Recipe


while True:
    tc.create_header("RocketFuelManager ver 1.0", clearterm=True)
    calcorread = input(" What can I help you with? [C]alculate a new recipe or [L]oad an old one?: ")
    if calcorread.capitalize() == "C":
        # Calculate a new recipe
        newrecipe = Recipe()
        newrecipe.cooktodict()
        newrecipe.createprettyprint(excludenotes=True)
        newrecipe.prettyprintrecipe(indent=28, newlines=2)
        saveornot = input("\n\n               Want to save? [Y]es or [N]o?: ")
        if saveornot[0].capitalize() == "Y":
            # Save data
            newrecipe.createsavedata()
            cookbookorsingle = input("\n     [A]dd to Cookbook, [e]xport or [b]oth?: ")
            if cookbookorsingle.capitalize() == "A":
                newrecipe.writetofile(singlefile=False)
            elif cookbookorsingle.capitalize() == "E":
                newrecipe.writetofile(singlefile=True)
            elif cookbookorsingle.capitalize() == "B":
                newrecipe.writetofile(singlefile=False)
                newrecipe.writetofile(singlefile=True)

    elif calcorread.capitalize() == "L":
        singleorcookbook = input("\n   Load a [s]ingle file or from [C]ookbook?: ")
        if singleorcookbook.capitalize() == "S":
            # Load from single file
            name = input("\n        Enter the name of your .recipe file: ")
            loadrecipe = Recipe(loadfromfile=True, singlefile=True, identifier=name, searchbydate=False)
            if loadrecipe.nonexistent is not True:
                loadrecipe.prettyprintrecipe(regenerate=True, indent=28, newlines=2)
                importornot = input("\n        Do you want to [i]mport the recipe?: ")
                if importornot.capitalize() == "I":
                    loadrecipe.modifynoteprocedure(save=True)
        elif singleorcookbook.capitalize() == "C":
            # Load a saved recipe
            dateorname = input("\n             Search by [d]ate or by [n]ame?: ")
            if dateorname.capitalize() == "N":
                # Load by name
                recipename = input("\n              Enter the name of your recipe: ")
                loadrecipe = Recipe(loadfromfile=True, identifier=recipename, searchbydate=False)
                if loadrecipe.nonexistent is not True:
                    loadrecipe.prettyprintrecipe(regenerate=True, indent=28, newlines=2)
                    loadrecipe.modifynoteprocedure(save=True)
            elif dateorname.capitalize() == "D":
                # Load by date
                recipedate = input("\n              Enter the date of your recipe: ")
                loadrecipe = Recipe(loadfromfile=True, identifier=recipedate, searchbydate=True)
                if loadrecipe.nonexistent is not True:
                    loadrecipe.prettyprintrecipe(regenerate=True, indent=28, newlines=2)
                    loadrecipe.modifynoteprocedure(save=True)
    repeatorexit = input("\n\n        Do you want to exit? [Y]es or [N]o?: ")
    if repeatorexit.capitalize() == "Y":
        tc.clear_term()
        break
