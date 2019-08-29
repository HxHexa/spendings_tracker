#!/usr/bin/python3

import pickle
import io
import argparse

from spendEntryClass import spendEntry
from sourceClass import source
from categoryClass import category

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

#newcate <name>
#newsrc <name> <amount>
#addentry <name> <amount>
#listsrc
#listcate
#viewsrc <name>
#viewcate <name>
#TBD: delsrc delcate delentry --version

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
##src1.display()
##src2.display()
##cat1.display()
##cat2.display()
#
#with open('src2.pickle', 'wb') as file:
#    pickle.dump(src2, file)
#
#with open('src2.pickle', 'rb') as file:
#    srcPickle = pickle.load(file)
#
#srcPickle.display()
