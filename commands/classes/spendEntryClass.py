#!/usr/bin/python3

"""
spendEntry
The main building block. Basically an entry for individual spendings.
name: name of spendings
amount: amount spent
"""

class spendEntry:
    def __init__(self, name, amount, note='None'):
        self.name = name
        self.amount = amount
        self.note = note
        self.category = []
        self.source = ''

    #overloading eq for remove commands
    def __eq__(self, other):
        eqCheck = [self.name == other.name,
                   self.amount == other.amount,
                   self.note == other.note,
                   self.category == other.category,
                   self.source == other.source]
        return all(eqCheck)

    def setName(self, newname):
        self.name = newname

    def setAmount(self, newamount):
        self.amount = newamount

    def setNote(self, note):
        self.note = note

    def display(self):
        print()
        print('Entry Name: \'{0}\' Amount: {1}'.format(self.name, self.amount))
        if self.note != 'None':
            print('Note: {0}'.format(self.note))
        print('Spent from (Source): {0}'.format(self.source))
        print('Categorized under: {0}'.format(' '.join(self.category)))
