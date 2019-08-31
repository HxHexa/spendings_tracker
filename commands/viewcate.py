#viewcate
#args: name
#view the details of category with name name
#now with added support for multiple categories

from . import globalvar
from . import classes
import sys

def viewcate(args):
    cateStrList = args.name.split(',')
    #if input is a single category then display like normal
    if len(cateStrList) == 1:
        try:
            globalvar.masterCate[args.name].display()
        except KeyError:
            print('Category {0} not found.'.format(args.name))
            sys.exit(1)
    else:
        cateViewList = []
        #checking to see if all lists exist
        #also to put all categories into a list
        for i in cateStrList:
            try:
                cateViewList.append(globalvar.masterCate[i])
            except KeyError:
                print('Category {0} not found.'.format(i))
                sys.exit(1)
        outCate = classes.category(args.name)
        #collecting all common entries accross all categories into 1
        for i in cateViewList:
            if outCate.spendEntryList == []:
                outCate.spendEntryList = i.spendEntryList
            else:
                outCate.spendEntryList = [x for x in i.spendEntryList if x in outCate.spendEntryList]
        #calculating the amount
        for i in outCate.spendEntryList:
            outCate.amount += i.amount
        outCate.display()
