# Screen-Class

import os


class Screen:
    @staticmethod
    def clearscreen():
        """Clears the terminal"""
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")

    @staticmethod
    def createheader(text, clear=True):
        """Creates a header"""
        if clear is True:
            Screen.clearscreen()
        try:
            width = os.get_terminal_size()[0]
        except AttributeError:
            width = 120
        borders = ""
        borders += width * "~"
        width -= len(text)
        spaces = width // 2
        space = ""
        space += spaces * " "
        print(borders)
        print("\n" + space + text)
        print("\n" + borders)
        print("\n\n")
