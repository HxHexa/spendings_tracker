#newsrc
#args: name amount
#create a new source with name name and amount amount

from . import classes
from . import globalvar
import sys

def newsrc(args):
    if len(args.name) < 2:
        print('All names for source must be at least 2 characters long.')
        sys.exit(1)
    try:
        globalvar.masterSource[args.name]
        print('Source with duplicate name already exists.')
    except KeyError:
        newSrc = classes.source(args.name, args.amount)
        globalvar.masterSource[args.name] = newSrc
        globalvar.listStrSource += '\'{0}\' '.format(args.name)
        print('New source {0} created containing money amount of {1}.'.format(args.name, args.amount))
