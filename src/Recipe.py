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
    nonexistent = False
    indent = 4
    ascii = False

    def __init__(self, loadfromfile=False, identifier="", searchbydate=False):
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
            if searchbydate is False:
                CookbookHandler.loadfromcookbook(self, recipename=identifier, date="")
            elif searchbydate is True:
                CookbookHandler.loadfromcookbook(self, recipename="", date=identifier)

    def cooktodict(self):
        """Generate datadict"""
        self.datadict["1-Title"] = self.rawdata[0]
        self.datadict["2-Date"] = self.rawdata[1]
        self.datadict["3-Total (g)"] = self.rawdata[2]
        self.datadict["4-Ratio"] = [self.rawdata[3][0], self.rawdata[3][1]]
        self.datadict["5-K-N-O3 (g)"] = self.rawdata[2] * (self.rawdata[3][0] / 100)
        self.datadict["6-Sugar (g)"] = self.rawdata[2] * (self.rawdata[3][1] / 100)
        self.datadict["7-Sulfide (g)"] = (self.rawdata[2] // 10) * self.rawdata[4]
        self.datadict["8-Fe2-O3 (g)"] = (self.rawdata[2] // 10) * self.rawdata[5]

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

    def writetofile(self):
        """Saves the recipe to Cookbook.db"""
        CookbookHandler.savetocookbook(self)
