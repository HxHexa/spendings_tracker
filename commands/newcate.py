#newcate
#args: name
#create a new category with name name

from . import classes
from . import globalvar
import sys

def newcate(args):
    if len(args.name) < 2:
        print('All names must be at least 2 characters long.')
        sys.exit(1)
    try:
        globalvar.masterCate[args.name]
        print('Category with duplicate name already exists.')
    except KeyError:
        newCate = classes.category(args.name)
        globalvar.masterCate[args.name] = newCate
        globalvar.listStrCate += '\'{0}\' '.format(args.name)
        print('New category {0} created.'.format(args.name))
