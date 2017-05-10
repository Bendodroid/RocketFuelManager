### RocketFuelManager

A tool to calculate, save and edit fuel-mixtures for sugar-rockets
based on Potassium-Nitrate and Sugar.

### Features

Working:

- Calculation of fuel ingredients (K-N-O3, Sugar, Sulfide, Fe2-O3)
- Export to JSON
- Importing and printing of saved recipes
    - Now including Notes

Not Working:

- Editing of recipes in JSON files (under construction)
- User-specified ingredients (in preparation)

### How to use?

For the full program, only the 3 .py files in /src are necessary,
run it with:

    ~$ python3 Main.py

Saved recipes are named <your title>.recipe in the Program source directory. 
When trying to load from a file, you're asked to enter the name of the recipe 
you specified when calculating.

### Planned changes

- User can add or remove ingredients
    - Rework input procedure
- Load/Save improvements
    - Single database and not a file for every recipe
- Different folder for recipes
