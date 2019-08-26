#!/usr/bin/python3

from spendEntryClass import spendEntry

"""
source
Used for keeping track of how much money was spent on which source
name: name of source
amount: amount of money in source
spendEntryList: list of spendEntry(ies) that was spent on the source
"""

class source():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.spendEntryList = []

    def display(self):
        print('Source Name:{0} Amount:{1} Entries:'.format(self.name, self.amount))
        for i in self.spendEntryList:
            print('{0} - {1}'.format(i.name, i.amount))

    def setName(self, newname):
        self.name = newname

    def setAmount(self, newamount):
        self.amount = newamount

    def addEntry(self, spendEntry):
        self.spendEntryList.append(spendEntry)
        self.amount -= spendEntry.amount

    def removeEntry(self, spendEntry):
        self.spendEntryList.remove(spendEntry)
        self.amount += spendEntry.amount
