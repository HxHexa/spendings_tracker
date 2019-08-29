#!/usr/bin/python3
#main program

import pickle
import io
import argparse
import sys

from classes import source, category, spendEntry
import commands

#Used to keep track of all sources and categories through sessions
#To be pickled/depickled at start of program
masterSource = {}
masterCate = {}
#Used for commands that require listing of all the sources/cate
listStrSource = ''
listStrCate = ''

#Standard argument parser
#a lot of help from the argparse documentation
#https://docs.python.org/3/library/argparse.html
#and this write-up
#https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()

#changing the default behavior when no argument is given
#thanks to: https://stackoverflow.com/questions/4042452/display-help-message-with-python-argparse-when-script-is-called-without-any-argu
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)

#TBDone: delsrc delcate delentry --version
#newcate <name>
newcate = subparser.add_parser('newcate', help='create a new spendings category')
newcate.add_argument('name', help='name of new category')
newcate.set_defaults(func=commands.newcate)

#newsrc <name> <amount>
#newsrc = subparser.add_parser('newsrc', help='create a new source of money')
#newsrc.add_argument('name', help='name of source')
#newsrc.add_argument('amount', help='amount of money currently in source', type=int)
#newsrc.set_defaults(func=newsrc)

#calling the default functions, defined in the specific commands files
args = parser.parse_args()
args.func(args)

#src1 = source('wallet', 200)
#src2 = source('tdacc', 1000)
#cat1 = category('games')
#cat2 = category('books')
#
#x1 = spendEntry('fe3h', 50, 'GOTY no regrets')
#x2 = spendEntry('ps4', 110, 'ehhh')
#y1 = spendEntry('graphics', 27)
#y2 = spendEntry('physics', 8)
#
#src1.addEntry(x1)
#src2.addEntry(x2)
#src2.addEntry(y1)
#src2.addEntry(y2)
#cat1.addEntry(x1)
#cat1.addEntry(x2)
#cat2.addEntry(y1)
#cat2.addEntry(y2)
#
#src1.display()
#src2.display()
#cat1.display()
#cat2.display()

#with open('src2.pickle', 'wb') as file:
#    pickle.dump(src2, file)
#
#with open('src2.pickle', 'rb') as file:
#    srcPickle = pickle.load(file)
#
#srcPickle.display()
