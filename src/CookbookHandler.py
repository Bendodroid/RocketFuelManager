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
            with open("Cookbook.db", "r") as file:
                alreadysavedobj = json.loads(file.read())
        except FileNotFoundError:
            alreadysavedobj = {}
        name = obj.savedata["rawdata"][0]
        alreadysavedobj[name] = obj.savedata
        with open("Cookbook.db", "w") as file:
            file.write(json.dumps(alreadysavedobj,
                                  indent=CookbookHandler.indent,
                                  ensure_ascii=CookbookHandler.ascii,
                                  sort_keys=CookbookHandler.sortkeys))

    @staticmethod
    def loadfromcookbook(obj, recipename):
        """Loads from the Cookbook"""
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
