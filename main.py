#!/usr/bin/python3
#main program

import pickle
import io
import argparse
import sys

import commands

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

#version number
parser.add_argument('--version', action='version', version='0.04')

#reset
reset = subparser.add_parser('reset', help='create new .pickle files and wipe previous data')
reset.set_defaults(func=commands.reset)

#newcate <name>
newcate = subparser.add_parser('newcate', help='create a new spendings category', aliases=['newcategory'])
newcate.add_argument('name', help='name of new category')
newcate.set_defaults(func=commands.newcate)

#newsrc <name> <amount>
newsrc = subparser.add_parser('newsrc', help='create a new source with designated amount', aliases=['newsource'])
newsrc.add_argument('name', help='name of new source')
newsrc.add_argument('amount', help='amount of money already in source', type=float)
newsrc.set_defaults(func=commands.newsrc)

#listsrc
listsrc = subparser.add_parser('listsrc', help='list all sources', aliases=['listsource'])
listsrc.set_defaults(func=commands.listsrc)

#listcate
listcate = subparser.add_parser('listcate', help='list all categories', aliases=['listcategory'])
listcate.set_defaults(func=commands.listcate)

#newentry
newentry = subparser.add_parser('newentry', help='add a new spending entry')
newentry.add_argument('name', help='name of new entry')
newentry.add_argument('amount', help='amount of money spent', type=float)
newentry.set_defaults(func=commands.newentry)

#viewsrc
viewsrc = subparser.add_parser('viewsrc', help='view the details of a source', aliases=['viewsource'])
viewsrc.add_argument('name', help='name of source to view')
viewsrc.set_defaults(func=commands.viewsrc)

#viewcate
viewcate = subparser.add_parser('viewcate', help='view the details of a category', aliases=['viewcategory'])
viewcate.add_argument('name', help='name of category to view')
viewcate.set_defaults(func=commands.viewcate)

#viewentry
viewentry = subparser.add_parser('viewentry', help='look up the details of an entry')
viewentry.set_defaults(func=commands.viewentry)

#calling the default functions, defined in the specific commands files
args = parser.parse_args()
args.func(args)

#pickling new data after program's completion
with open('./commands/globalpickle/masterSource.pickle', 'wb') as file:
    pickle.dump(commands.globalvar.masterSource, file)
with open('./commands/globalpickle/masterCate.pickle', 'wb') as file:
    pickle.dump(commands.globalvar.masterCate, file)
with open('./commands/globalpickle/listStrSource.pickle', 'wb') as file:
    pickle.dump(commands.globalvar.listStrSource, file)
with open('./commands/globalpickle/listStrCate.pickle', 'wb') as file:
    pickle.dump(commands.globalvar.listStrCate, file)
