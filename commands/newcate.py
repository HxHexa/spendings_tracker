#newcate
#args: name
#create a new category with name name

from . import globalvar

def newcate(args):
    print(globalvar.masterCate)
    print('haha it is working! {0}'.format(args.name))
