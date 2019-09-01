#addentry
#args: name amount
#add a new entry to a source and some categories with name name and amount amount

from . import classes
from . import globalvar
import sys

def newentry(args):
    #while loop to get input for source
    print('Sources: {0}'.format(globalvar.listStrSource))
    while True:
        source = input('Enter a source, or type \'q\' to quit: ')
        if source == 'q':
            print('Cancelling operation...')
            sys.exit(1)
        try:
            globalvar.masterSource[source]
            break
        except KeyError:
            print('Source not found. Please try again.')

    #while loop to get input for category
    print('Categories: {0}'.format(globalvar.listStrCate))
    received = False
    while received != True:
        cate = input('Enter categories to add this entry to seperated by a comma, or type \'q\' to quit: ')
        if cate == 'q':
            print('Cancelling operation...')
            sys.exit(1)
        cateList = cate.split(',')
        for i in cateList:
            try:
                globalvar.masterCate[i]
                received = True
            except KeyError:
                print('Category \'{}\' not found. Please try again.'.format(i))
                received = False
                break

    #adding notes
    note = 'None'
    while True:
        decision = input('Do you want to add a note to this entry? (y/n) ')
        if decision == 'n':
            break
        elif decision == 'y':
            note = input('Enter your note: ')
            break
        else:
            print('Invalid input.')

    #adding the new entry
    newentry = classes.spendEntry(args.name, args.amount, note)
    globalvar.masterSource[source].addEntry(newentry) #adding to source
    for i in cateList:
        globalvar.masterCate[i].addEntry(newentry) #adding to categories
    #setting variables for tracking in entry
    newentry.source = source
    newentry.category = cateList

    #ending
    print('Entry \'{0}\' with amount {1} successfully added to source \'{2}\' and categories: {3}'.format(args.name, args.amount, source, cateList))
