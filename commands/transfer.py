'''
transfer.py - transfers from source1 to source2 an amounnt
could be used to set up a debt account, then transfer money into that
'''

from . import classes
from . import globalvar
from .listsrc import listsrc

import sys

def transfer(args):
    #lists out all source
    listsrc(args)

    #prompts for accounts to transfer
    while True:
        id1 = input("Enter name of source to transfer FROM, or type \'q\' to quit: ")
        if id1 == 'q':
            print("Cancelling operation...")
            sys.exit(1)
        try:
            globalvar.masterSource[id1]
            break
        except KeyError:
            print("Source not found. Please try again.")

    #prompts for accounts to transfer to
    while True:
        id2 = input("Enter name of source to transfer TO, or type \'q\' to quit: ")
        if id2 == 'q':
            print("Cancelling operation...")
            sys.exit(1)
        try:
            globalvar.masterSource[id2]
            break
        except KeyError:
            print("Source not found. Please try again.")

    #prompts for transfer amount
    while True:
        amount = input("Enter amount of money to transfer, or type \'q\' to quit: ")
        if amount == 'q':
            print("Cancelling operation...")
            sys.exit(1)
        try:
            float(amount)
            break
        except ValueError:
            print("Invalid input format. Please try again.")

    #transfer
    globalvar.masterSource[id1].transfer(globalvar.masterSource[id2], float(amount))
    print("Amount of {0} transfered from source {1} to source {2}.".format(amount, globalvar.masterSource[id1].name, globalvar.masterSource[id2].name))
