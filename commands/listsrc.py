#listsrc
#list all existing sources

from . import classes
from . import globalvar

def listsrc(args):
    print('ID. Name - Amount')
    counter = 1
    for i in globalvar.masterSource:
        print('{0}. {1} - {2}'.format(counter, globalvar.masterSource[i].name, globalvar.masterSource[i].amount))
        counter += 1

