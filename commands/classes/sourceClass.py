from .spendEntryClass import spendEntry

"""
source
Used for keeping track of how much money was spent on which source
name: name of source
amount: amount of money in source
spendEntryList: list of spendEntry(ies) that was spent on the source
"""

class source():
    def __init__(self, name, amount, interest):
        self.name = name
        self.amount = amount
        self.interest = interest
        self.spendEntryList = []

    def display(self):
        print('Source Name: \'{0}\' Amount: {1} Interest: {2}% Entries:'.format(self.name, self.amount, self.interest))
        print('ID. Name - Amount - Interest')
        counter = 1
        for i in self.spendEntryList:
            print('{0}. {1} - {2}'.format(counter, i.name, i.amount))
            counter += 1

    def setName(self, newname):
        self.name = newname

    def setAmount(self, newamount):
        self.amount = newamount

    def setInterest(self, newinterest):
        self.interest = newinterest

    def addEntry(self, spendEntry):
        self.spendEntryList.append(spendEntry)
        self.amount += spendEntry.amount
        self.amount = round(self.amount, 2)

    def removeEntry(self, spendEntry):
        self.spendEntryList.remove(spendEntry)
        self.amount -= spendEntry.amount
        self.amount = round(self.amount, 2)

    def calcInterest(self):
        self.amount = self.amount / 100 * (100 + self.interest)
        self.amount = round(self.amount, 2)

    #transfer to otherSource an amount
    def transfer(self, otherSource, transferAmount):
        self.amount -= transferAmount
        otherSource.amount += transferAmount
        self.amount = round(self.amount, 2)
        otherSource.amount = round(otherSource.amount, 2)
