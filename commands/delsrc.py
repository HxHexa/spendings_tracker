#delsrc
#args: name
#deletes a source

from . import globalvar
import sys

def delsrc(args):
    #source can only be deleted if empty
    if len(globalvar.masterSource[args.name].spendEntryList) != 0:
        print('Source not empty.')
    else:
        #update master source dictionary
        try:
            del globalvar.masterSource[args.name]
        except KeyError:
            print('Source not found.')
            sys.exit(1)

        #update source string
        newstr = globalvar.listStrSource.split(' ')
        newstr.remove("'{0}'".format(args.name))
        globalvar.listStrSource = ' '.join(newstr)
        print('Source {0} deleted.'.format(args.name))
