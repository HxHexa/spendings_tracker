#delentry
#args: none
#deletes an entry

from . import classes
import sys

def delentry(args):
    #The codes used for selecting which entry to delete
    #is taken straight out of viewentry
    src = 0
    cate = 0

    #Deciding whether the entry the user wants to look up is under a source or cate
    while True:
        inp = input('Source or category (src/cate/q) ')
        if inp == 'src':
            src = 1
            break
        elif inp == 'cate':
            cate = 1
            break
        elif inp == 'q':
            print('Cancelling operation...')
            sys.exit(1)
        else:
            print('Invalid input.')

    if src == 1:
        #Picking a source to look under
        #Is copied straight from newentry.py
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
        #Picking an entry to display
        globalvar.masterSource[source].display()
        while True:
            num = input('Enter the ID of the entry, or type \'q\' to quit: ')
            if num == 'q':
                print('Cancelling operation...')
                sys.exit(1)
            try:
                globalvar.masterSource[source].spendEntryList[int(num) - 1].display()
                break
            except IndexError:
                print('Invalid ID number. Please try again.')

    if cate == 1:
        #Picking a source to look under
        #Is copied straight from newentry.py
        print('Categories: {0}'.format(globalvar.listStrCate))
        while True:
            cate = input('Enter a category, or type \'q\' to quit: ')
            if cate == 'q':
                print('Cancelling operation...')
                sys.exit(1)
            try:
                globalvar.masterCate[cate]
                break
            except KeyError:
                print('Source not found. Please try again.')
        #Picking an entry to display
        globalvar.masterCate[cate].display()
        while True:
            num = int(input('Enter the ID of the entry, or type \'q\' to quit: '))
            if num == 'q':
                print('Cancelling operation...')
                sys.exit(1)
            try:
                globalvar.masterCate[cate].spendEntryList[num - 1].display()
                break
            except IndexError:
                print('Invalid ID number. Please try again.')
