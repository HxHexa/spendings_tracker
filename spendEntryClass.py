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

    def setName(self, newname):
        self.name = newname

    def setAmount(self, newamount):
        self.amount = newamount

    def setNote(self, note):
        self.note = note
