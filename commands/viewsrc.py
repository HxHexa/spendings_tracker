#viewsrc
#args: name
#view the details of source with name name

from . import globalvar
from . import classes

def viewsrc(args):
    try:
        globalvar.masterSource[args.name].display()
    except KeyError:
        print('Source not found.')
