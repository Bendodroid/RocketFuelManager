# Recipe-Class

from CookbookHandler import *


class Recipe:
    rawdata = ["", "", 0.0, [0.0, 0.0], 0.0, 0.0, ""]
    datadict = {"1-Title": "",
                "2-Date": "",
                "3-Total (g)": 0.0,
                "4-Ratio": [0.0, 0.0],
                "5-K-N-O3 (g)": 0.0,
                "6-Sugar (g)": 0.0,
                "7-Sulfide (g)": 0.0,
                "8-Fe2-O3 (g)": 0.0,
                "9-Notes": "",
                }
    datadictkeylist = []
    longestdatadictkey = 0
    printlist = []
    savedata = {}
    loadedfromjson = False
    imported = False
    nonexistent = False
    indent = 4
    ascii = False

    def __init__(self, loadfromfile=False, singlefile=False, identifier="", searchbydate=False):
        """Read User Input or load from file"""
        if loadfromfile is False:
            self.rawdata[0] = input("\n           Input a title for the new recipe: ")
            self.rawdata[1] = input("                               Input a date: ")
            self.rawdata[2] = float(input("                          Total Amount (g)?: "))
            self.rawdata[3][0] = float(input("      %age of K-N-O3 for the basic Mixture?: "))
            self.rawdata[3][1] = 100 - self.rawdata[3][0]
            self.rawdata[4] = float(input("       (Additive) How much Sulfide/10g (g)?: "))
            self.rawdata[5] = float(input("        (Additive) How much Fe2-O3/10g (g)?: "))
        elif loadfromfile is True:
            self.loadedfromjson = True
            if singlefile is True:
                CookbookHandler.loadfromcookbook(self, jsonkey=identifier, singlefile=True, bydate=False)
                self.imported = True
            else:
                CookbookHandler.loadfromcookbook(self, jsonkey=identifier, singlefile=False, bydate=searchbydate)

    def cooktodict(self):
        """Generate datadict"""
        self.datadict["1-Title"] = self.rawdata[0]
        self.datadict["2-Date"] = self.rawdata[1]
        self.datadict["3-Total (g)"] = self.rawdata[2]
        self.datadict["4-Ratio"] = [self.rawdata[3][0], self.rawdata[3][1]]
        self.datadict["5-K-N-O3 (g)"] = self.rawdata[2] * (self.rawdata[3][0] / 100)
        self.datadict["6-Sugar (g)"] = self.rawdata[2] * (self.rawdata[3][1] / 100)
        self.datadict["7-Sulfide (g)"] = (self.rawdata[2] / 10) * self.rawdata[4]
        self.datadict["8-Fe2-O3 (g)"] = (self.rawdata[2] / 10) * self.rawdata[5]
        if self.rawdata[6] is not "":
            self.datadict["9-Notes"] = self.rawdata[6]

    def generatekeylist(self, reset=True):
        """Generate keylist"""
        if reset is True:
            self.datadictkeylist = []
        for key, value in self.datadict.items():
            self.datadictkeylist.append(key)
        self.datadictkeylist.sort()

    def createprettyprint(self, excludenotes=False):
        """Creates a pretty-printable list"""
        self.generatekeylist(reset=True)
        # Determine longest key
        self.longestdatadictkey = 0
        for key in self.datadictkeylist:
            if len(key) > self.longestdatadictkey:
                self.longestdatadictkey = len(key) + 1
        # Create printlist
        self.printlist = []
        for i in range(len(self.datadictkeylist) - int(excludenotes)):
            self.printlist.append(["", ""])
        # Remove numbers in front of keys in self.datadictkeylist
        for key in self.datadictkeylist:
            newkey = ""
            for i in range(2, len(key)):
                newkey += key[i]
            self.datadictkeylist[self.datadictkeylist.index(key)] = newkey
        # Assign Values from self.datadict
        for i in range(len(self.datadictkeylist) - int(excludenotes)):
            spacestoinsert = (self.longestdatadictkey - len(self.datadictkeylist[i])) * " "
            self.printlist[i][0] = self.datadictkeylist[i] + spacestoinsert
            if type(self.datadict[str(i + 1) + "-" + self.datadictkeylist[i]]) is float:
                self.printlist[i][1] = str(round(self.datadict[str(i + 1) + "-" + self.datadictkeylist[i]], 2))
            elif type(self.datadict[str(i + 1) + "-" + self.datadictkeylist[i]]) is list:
                a = str(round(self.datadict[str(i + 1) + "-" + self.datadictkeylist[i]][0], 2))
                b = str(round(self.datadict[str(i + 1) + "-" + self.datadictkeylist[i]][1], 2))
                self.printlist[i][1] = "[" + a + ", "
                self.printlist[i][1] += b + "]"
            else:
                self.printlist[i][1] = str(self.datadict[str(i + 1) + "-" + self.datadictkeylist[i]])

    def prettyprintrecipe(self, regenerate=False, indent=24, newlines=2):
        """Print the recipe aligned to ':' """
        if regenerate is True:
            self.createprettyprint(excludenotes=False)
        for i in range(newlines):
            print()
        spaces = indent * " "
        for item in self.printlist:
            print(spaces + item[0] + " : " + str(item[1]))
        if self.loadedfromjson is not True:
            self.datadict["9-Notes"] = input("\n\n                      Add notes if you want: ")
            self.rawdata[6] = self.datadict["9-Notes"]

    def createsavedata(self):
        """Creates JSON-compatible object to save all data"""
        self.savedata["rawdata"] = self.rawdata
        self.savedata["datadict"] = self.datadict
        self.savedata["datadictkeylist"] = self.datadictkeylist
        self.savedata["longestdatadictkey"] = self.longestdatadictkey
        self.savedata["printlist"] = self.printlist

    def writetofile(self, singlefile=False):
        """Saves the recipe to Cookbook.db or single file"""
        CookbookHandler.savetocookbook(self, singlefile=singlefile)

    def modifynoteprocedure(self, save=True):
        """Method to modify the notes"""
        modnotes = input("\n                        [M]odify the notes?: ")
        if modnotes.capitalize() == "M":
            self.rawdata[6] = input("                      Put in your new Notes: ")
            self.cooktodict()
            self.createprettyprint()
            self.createsavedata()
            if save is True:
                self.writetofile(singlefile=False)
            try:
                with open(self.rawdata[0] + ".recipe", "r") as file:
                    file.read()
                modornot = input("\n                  [M]odify the single file?: ")
                if modornot.capitalize() == "M":
                    self.writetofile(singlefile=True)
            except FileNotFoundError:
                pass
