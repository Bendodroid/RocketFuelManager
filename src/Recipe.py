# Recipe-Class


class Recipe:
    rawdata = ["", 0.0, [0.0, 0.0], 0.0, 0.0]
    datadict = {"1:Title": "",
                "2:Total": 0.0,
                "3:Ratio": [0.0, 0.0],
                "4:K-N-O3 (g)": 0.0,
                "5:Sugar (g)": 0.0,
                "6:Sulfide (g)": 0.0,
                "7:Fe2-O3 (g)": 0.0
                }
    datadictkeylist = []
    printlist = []
    savedict = {}
    longestdatadictkey = 0
    
    def __init__(self):
        """Read User Input"""
        self.rawdata[0] = input("           Input a title for the new recipe: ")
        self.rawdata[1] = float(input("                          Total Amount (g)?: "))
        self.rawdata[2][0] = float(input("    How much % K-N-O3 in the basic Mixture?: "))
        self.rawdata[2][1] = 100 - self.rawdata[2][0]
        self.rawdata[3] = float(input("           (Additive) How much Sulfide (g)?: "))
        self.rawdata[4] = float(input("            (Additive) How much Fe2-O3 (g)?: "))

    def cooktodict(self):
        """Creates complete datadict"""
        self.datadict["1:Title"] = self.rawdata[0]
        self.datadict["2:Total (g)"] = self.rawdata[1]
        self.datadict["3:Ratio"] = [self.rawdata[2][0], self.rawdata[2][1]]
        self.datadict["4:K-N-O3 (g)"] = self.rawdata[1] * (self.rawdata[2][0] / 100)
        self.datadict["5:Sugar (g)"] = self.rawdata[1] * (self.rawdata[2][1] / 100)
        self.datadict["6:Sulfide (g)"] = (self.rawdata[1] // 10) * self.rawdata[3]
        self.datadict["7:Fe2-O3 (g)"] = (self.rawdata[1] // 10) * self.rawdata[4]
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
