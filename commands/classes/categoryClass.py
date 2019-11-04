from .spendEntryClass import spendEntry
import math

"""
category
Used for keeping track of how much money is going into which category
The main difference between this and source is that an amount is not neccesary
upon initialization. In addition, adding an entry to a category will increment
its amount instead of the reverse with a source.
name: name of category
amount: amount of money on category
spendEntryList: list of spendEntry(ies) that falls under the category
"""

class category():
    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount
        self.spendEntryList = []

    def display(self):
        print('Category Name:{0} Amount:{1} Entries:'.format(self.name, self.amount))
        print('ID. Name - Amount')
        counter = 1
        for i in self.spendEntryList:
            print('{0}. {1} - {2}'.format(counter, i.name, i.amount))
            counter += 1

    def setName(self, name):
        self.name = name

    def setAmount(self, amount):
        self.amount = amount

    def addEntry(self, spendEntry):
        self.spendEntryList.append(spendEntry)
        self.amount += spendEntry.amount
        self.amount = round(self.amount, 2)

    def removeEntry(self, spendEntry):
        self.spendEntryList.remove(spendEntry)
        self.amount -= spendEntry.amount
        self.amount = round(self.amount, 2)
