#listcate
#list all existing categories

from . import classes
from . import globalvar

def listcate(args):
    print('ID. Name - Amount')
    counter = 1
    for i in globalvar.masterCate:
        print('{0}. {1} - {2}'.format(counter, globalvar.masterCate[i].name, globalvar.masterCate[i].amount))
        counter += 1
