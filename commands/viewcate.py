#viewcate
#args: name
#view the details of category with name name

from . import globalvar
from . import classes

def viewcate(args):
    try:
        globalvar.masterCate[args.name].display()
    except KeyError:
        print('Category not found.')
