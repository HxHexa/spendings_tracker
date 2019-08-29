#listsrc
#list all existing sources

from . import classes
from . import globalvar

def listsrc(args):
    print('All existing sources:')
    print(globalvar.listStrSource)
