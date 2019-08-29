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

#TBDone: delsrc delcate delentry --version
#newcate <name>
newcate = subparser.add_parser('newcate', help='create a new spendings category')
newcate.add_argument('name', help='name of new category')
newcate.set_defaults(func=commands.newcate)

#listcate
listcate = subparser.add_parser('listcate', help='list all categories')
listcate.set_defaults(func=commands.listcate)

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
