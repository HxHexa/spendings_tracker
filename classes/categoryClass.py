from .spendEntryClass import spendEntry

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
        for i in self.spendEntryList:
            print('{0} - {1}'.format(i.name, i.amount))

    def setName(self, name):
        self.name = name

    def setAmount(self, amount):
        self.amount = amount

    def addEntry(self, spendEntry):
        self.spendEntryList.append(spendEntry)
        self.amount += spendEntry.amount

    def removeEntry(self, spendEntry):
        self.spendEntryList.append(spendEntry)
        self.amount -= spendEntry.amount
