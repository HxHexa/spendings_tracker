#global variables for interacting with all commands
#to store data accross sessions

import pickle
from . import classes

#Used to keep track of whether any files were not found during run
notfound = 0

#Used to keep track of all sources and categories through sessions
#Loaded/depickled at initialization
#Dumped at end of main
if __name__ != '__main__':
    try:
        with open('./commands/globalpickle/masterSource.pickle', 'rb') as file:
            masterSource = pickle.load(file)
    except FileNotFoundError:
        print('masterSource.pickle not found.')
        notfound = 1

    try:
        with open('./commands/globalpickle/masterCate.pickle', 'rb') as file:
            masterCate = pickle.load(file)
    except FileNotFoundError:
        print('masterCate.pickle not found.')
        notfound = 1

    #Used for commands that require listing of all the sources/cate
    try:
        with open('./commands/globalpickle/listStrSource.pickle', 'rb') as file:
            listStrSource = pickle.load(file)
    except FileNotFoundError:
        print('listStrSource.pickle not found.')
        notfound = 1

    try:
        with open('./commands/globalpickle/listStrCate.pickle', 'rb') as file:
            listStrCate = pickle.load(file)
    except FileNotFoundError:
        print('listStrCate.pickle not found.')
        notfound = 1

if notfound == 1:
    print('Some files were not found. If this is the first time you run')
    print('this program, please run the \'reset.\' command. These files will')
    print('also be generated upon successful execution of any commands other')
    print('than -h/--help and --version.')
