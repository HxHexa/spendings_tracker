'''
calcint.py <source> - calculates amount in source based on interest
synonym: calculateinterest, calcinterest, calculateint
'''

from . import classes
from . import globalvar

def calcint(args):
    try:
        globalvar.masterSource[args.source].calcInterest()
        print("New amount in source {0} is {1:.2f}.".format(args.source, globalvar.masterSource[args.source].amount))
    except KeyError:
        print("Source {0} not found.".format(args.source))
