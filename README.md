### RocketFuelManager

A tool to calculate, save and edit fuel-mixtures for sugar-rockets
based on Potassium-Nitrate and Sugar.

### Features

Working:

- Calculation of fuel ingredients (K-N-O3, Sugar, Sulfide, Fe2-O3)
- Saving and Importing of recipes from a JSON file
- Importing and printing of saved recipes (Now including notes)

### How to use?

For the full program, only the .py files in /src are necessary,
run it with:

    ~$ python3 Main.py

Saved recipes are named <your title>.recipe in the Program source directory.
When trying to load from the Cookbook, you're asked to enter the name of the recipe you specified when calculating.

### Planned changes

- User-specified ingredients (in preparation)
    - Rework input procedure
- Load/Save improvements
    - Editing or Removing of recipes in JSON files (under construction)
        - Currently you have to delete saved recipes manually or 
          overwrite them
