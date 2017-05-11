# CookbookHandler class

import json


class CookbookHandler:
    """Handles the Cookbook.db"""
    indent = 3
    ascii = False
    sortkeys = True

    @staticmethod
    def savetocookbook(obj):
        """Saves the new Recipe to the Cookbook"""
        try:
            # Tries to load JSON object from file
            with open("Cookbook.db", "r") as file:
                alreadysavedobj = json.loads(file.read())
        except FileNotFoundError:
            # If no Database exists, a new one is created
            alreadysavedobj = {}
        name = obj.savedata["rawdata"][0]
        alreadysavedobj[name] = obj.savedata
        with open("Cookbook.db", "w") as file:
            file.write(json.dumps(alreadysavedobj,
                                  indent=CookbookHandler.indent,
                                  ensure_ascii=CookbookHandler.ascii,
                                  sort_keys=CookbookHandler.sortkeys))

    @staticmethod
    def loadfromcookbook(obj, recipename="", date=""):
        """Loads from the Cookbook"""
        if recipename != "" and date == "":
            # Triggered to load by name
            try:
                with open("Cookbook.db", "r") as file:
                    cookbook = json.loads(file.read())
                loadobj = cookbook[recipename]
                obj.rawdata = loadobj["rawdata"]
                obj.datadict = loadobj["datadict"]
                obj.datadictkeylist = loadobj["datadictkeylist"]
                obj.longestdatadictkey = loadobj["longestdatadictkey"]
                obj.printlist = loadobj["printlist"]
            except KeyError:
                print("\n                 >>> There's no such recipe! Try again!")
                obj.nonexistent = True
        elif recipename == "" and date != "":
            # Triggered to load by date
            try:
                with open("Cookbook.db", "r") as file:
                    cookbook = json.loads(file.read())
                # Check if multiple recipies have the same date
                recipessamedate = []
                for key, value in cookbook.items():
                    if cookbook[key]["rawdata"][1] == date:
                        recipessamedate.append(key)
                if len(recipessamedate) == 1:
                    # Triggered when only one recipe has the specific date
                    for key, value in cookbook.items():
                        if cookbook[key]["rawdata"][1] == date:
                            CookbookHandler.loadfromcookbook(obj=obj, recipename=key, date="")
                elif len(recipessamedate) > 1:
                    # Triggered when more have it
                    print("\n   Multiple recipes are dated to " + date + ". Which do you want to load?\n")
                    for i in range(len(recipessamedate)):
                        print("                                         " + str(i + 1) + " : " + recipessamedate[i])
                    choice = input("\n                            Choose a recipe: ")
                    # Use number or title
                    try:
                        if int(choice):
                            choice = recipessamedate[int(choice) - 1]
                    except ValueError:
                        pass
                    CookbookHandler.loadfromcookbook(obj=obj, recipename=choice, date="")
            except KeyError:
                print("\n                 >>> There's no such recipe! Try again!")
                obj.nonexistent = True
