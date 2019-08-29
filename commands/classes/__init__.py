#__init__.py
#for packing up stuffs and making the main program neater
#resolved thanks to
#https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#example-directory-structure
#and
#https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x
#I realise that an init is not needed in python3, but this makes thing neater
#only 1 import classes needed in main

from .spendEntryClass import spendEntry
from .categoryClass import category
from .sourceClass import source
