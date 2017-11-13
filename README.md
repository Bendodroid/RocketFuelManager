# RocketFuelManager

A tool to calculate, save and edit fuel-mixtures for sugar-rockets
based on Potassium-Nitrate and Sugar.

## Features

Working:

- Calculation of fuel ingredients (K-N-O3, Sugar, Sulfide, Fe2-O3)
- Importing and printing of saved recipes (Now including notes)
- Specify where to store the recipe, in a single file or the Cookbook
- Editing notes in importing process

## How to use?

For the full program, only the .py files in /src are necessary,
run it in /src with:

    ~$ python3 Main.py

Saved recipes are stored in the Cookbook.db in the Program source directory.
When trying to load from the Cookbook, you're asked to enter the name or date
of the recipe you specified when calculating.
The program doesn't care how you format the date and title, it uses
your input(as a string) as an identifier to save/load it, so don't put unnecessary
whitespaces at the end of your input. To keep it easy, you
should always use the same way to input your date or title,
something like 2017-12-31.

## Planned changes

- User-specified ingredients (in preparation)
    - Rework input procedure
- Load/Save improvements
    - Editing or Removing of recipes in JSON files (under construction)
    - Currently you have to delete saved recipes manually or 
      overwrite them
