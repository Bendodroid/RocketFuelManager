# Recipe-Class


class Recipe:
    rawdata = ["", 0.0, [0.0, 0.0], 0.0, 0.0]
    datadict = {"1:Title": "",
                "2:Total (g)": 0.0,
                "3:Ratio": [0.0, 0.0],
                "4:K-N-O3 (g)": 0.0,
                "5:Sugar (g)": 0.0,
                "6:Sulfide (g)": 0.0,
                "7:Fe2-O3 (g)": 0.0
                }
    datadictkeylist = []
    printlist = []
    savedata = []
    longestdatadictkey = 0

    def __init__(self):
        """Read User Input"""
        self.rawdata[0] = input("\n           Input a title for the new recipe: ")
        self.rawdata[1] = float(input("                          Total Amount (g)?: "))
        self.rawdata[2][0] = float(input("       %age of K-N-O3 in the basic Mixture?: "))
        self.rawdata[2][1] = 100 - self.rawdata[2][0]
        self.rawdata[3] = float(input("       (Additive) How much Sulfide/10g (g)?: "))
        self.rawdata[4] = float(input("        (Additive) How much Fe2-O3/10g (g)?: "))

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
        # Remove numbers in front of keys in self.datadictkeylist
        for key in self.datadictkeylist:
            newkey = ""
            for i in range(2, len(key)):
                newkey += key[i]
            self.datadictkeylist[self.datadictkeylist.index(key)] = newkey
        print(self.datadictkeylist)
        # Assign Values from self.datadict
        for i in range(len(self.datadictkeylist)):
            spacestoinsert = (self.longestdatadictkey - len(self.datadictkeylist[i])) * " "
            self.printlist[i][0] = self.datadictkeylist[i] + spacestoinsert
            self.printlist[i][1] = self.datadict[str(i + 1) + ":" + self.datadictkeylist[i]]

    def prettyprintrecipe(self, indent=4, newlines=2):
        for i in range(newlines):
            print()
        spaces = indent * " "
        for item in self.printlist:
            print(spaces + item[0] + " : " + str(item[1]))

    def createsavedata(self):
        self.savedata.append(self.rawdata)
        self.savedata.append(self.datadict)
        self.savedata.append(self.datadictkeylist)
        self.savedata.append(self.longestdatadictkey)
        self.savedata.append(self.printlist)
