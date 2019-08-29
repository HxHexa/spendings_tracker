#global variables for interacting with all commands 
#to store data accross sessions

import pickle
from . import classes

#Used to keep track of all sources and categories through sessions
#Loaded/depickled at initialization
#Dumped at end of main
try:
    with open('globalpickle/masterSource.pickle', 'rb') as file:
        masterSource = pickle.load(file)
except FileNotFoundError:
    print('masterSource.pickle not found. Initializing new file.')
    masterSource = {}

try:
    with open('globalpickle/masterCate.pickle', 'rb') as file:
        masterCate = pickle.load(file)
except FileNotFoundError:
    print('masterCate.pickle not found. Initializing new file.')
    masterCate = {}

#Used for commands that require listing of all the sources/cate
try:
    with open('globalpickle/listStrSource.pickle', 'rb') as file:
        listStrSource = pickle.load(file)
except FileNotFoundError:
    print('listStrSource.pickle not found. Initializing new file.')
    listStrSource = ''

try:
    with open('globalpickle/listStrCate.pickle', 'rb') as file:
        listStrCate = pickle.load(file)
except FileNotFoundError:
    print('listStrCate.pickle not found. Initializing new file.')
    listStrCate = ''
