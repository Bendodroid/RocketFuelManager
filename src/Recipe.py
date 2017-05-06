# Recipe-Class


class Recipe:
    data = [0.0, [0.0, 0.0], 0.0, 0.0]
    datadict = {"1-Menge": 0.0,
                "2-Verhältnis": [0, 0],
                "3-Gramm KNO3": 0.0,
                "4-Gramm Saccharose": 0.0,
                "5-Spatelspitzen S/10g": 0.0,
                "6-Spatelspitzen Fe2O3/10g": 0.0,
                }
    datadictkeylist = []
    printlist = []
    savedict = {}
    longestdatadictkey = 0
    
    def __init__(self):
        """Read User Input"""
        self.data[0] = float(input("\n\n                   Wieviel Gramm insgesamt?: "))
        self.data[1][0] = float(input("\n                      Wieviel Prozent KNO3?: "))
        self.data[1][1] = 100 - self.data[1][0]
        self.data[2] = float(input("   Wieviele Spatelspitzen Schwefel pro 10g?: "))
        self.data[3] = float(input("      Wieviele Spatelspitzen Fe2O3 pro 10g?: "))

    def cooktodict(self):
        """Creates complete datadict"""
        self.datadict["1-Menge"] = self.data[0]
        self.datadict["2-Verhältnis"] = [self.data[1][0], self.data[1][1]]
        self.datadict["3-Gramm KNO3"] = self.data[0] * (self.data[1][0] / 100)
        self.datadict["4-Gramm Saccharose"] = self.data[0] * (self.data[1][1] / 100)
        self.datadict["5-Spatelspitzen S/10g"] = (self.data[0] // 10) * self.data[2]
        self.datadict["6-Spatelspitzen Fe2O3/10g"] = (self.data[0] // 10) * self.data[3]
        # Create sorted datadictkeylist
        for key, value in self.datadict.items():
            self.datadictkeylist.append(key)
        self.datadictkeylist.sort()

    def createprettyprint(self):
        """Creates a pretty-printable list"""
        # Determine longest key
        for key, value in self.datadict.items():
            if len(key) > self.longestdatadictkey:
                self.longestdatadictkey = len(key) + 1
        # Create printlist
        for i in range(len(self.datadictkeylist)):
            self.printlist.append(["", ""])
        # Assign Values from datadict
        for i in range(len(self.datadictkeylist)):
            print(i)
            spacestoinsert = (self.longestdatadictkey - len(self.datadictkeylist[i])) * " "
            self.printlist[i][0] = self.datadictkeylist[i] + spacestoinsert
            self.printlist[i][1] = self.datadict[self.datadictkeylist[i]]
