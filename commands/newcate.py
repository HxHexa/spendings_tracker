#newcate
#args: name
#create a new category with name name

from . import classes
from . import globalvar

def newcate(args):
    newCate = classes.category(args.name)
    globalvar.masterCate[args.name] = newCate
    globalvar.listStrCate += '{0} '.format(args.name)
    print('New category {0} created.'.format(args.name))
