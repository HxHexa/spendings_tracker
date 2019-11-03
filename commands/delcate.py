#delcate
#args: name
#deletes a category

from . import globalvar
from . import classes

def delcate(args):
    #category can only be deleted if empty
    if len(globalvar.masterCate[args.name].spendEntryList) != 0:
        print('Category not empty.')
    else:
        #update master category dictionary
        try:
            del globalvar.masterCate[args.name]
        except KeyError:
            print('Category not found.')
            sys.exit(1)

        #update source string
        newstr = globalvar.listStrCate.split(' ')
        newstr.remove("'{0}'".format(args.name))
        globalvar.listStrCate = ' '.join(newstr)
        print('Category {0} deleted.'.format(args.name))
