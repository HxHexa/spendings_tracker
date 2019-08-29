#listcate
#list all existing categories

from . import classes
from . import globalvar

def listcate(args):
    print('All existing categories:')
    print(globalvar.listStrCate)
