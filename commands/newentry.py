#addentry
#args: name amount
#add a new entry to a source and some categories with name name and amount amount

from . import classes
from . import globalvar
import sys

def newentry(args):
    newentry = classes.spendEntry(args.name, args.amount)

    #while loop to get input for source
    print('Sources: {0}'.format(globalvar.listStrSource))
    received = False
    while received != True:
        source = input('Enter a source, or type \'q\' to quit: ')
        if source == 'q':
            print('Cancelling operation.')
            sys.exit(1)
        try:
            globalvar.masterSource[source]
            print('Source {} found.'.format(source))
            received = True
        except KeyError:
            print('Source not found. Please try again.')

    #while loop to get input for category
    print('Categories: {0}'.format(globalvar.listStrCate))
    print('Example input: august,groceries,food')
    received = False
    cateList = []
    while received != True:
        cate = input('Enter categories to add this entry to seperated by a comma, or type \'q\' to quit: ')
