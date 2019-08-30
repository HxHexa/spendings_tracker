#reset
#create new blank .pickle files
#will wipe previous data. Should only be used on first run

import pickle
import sys

def reset(args):
    print('This command will wipe pre-existing data.')
    while True:
        decision = input('Continue? (y/n) ')
        if decision == 'n':
            print('Exiting...')
            sys.exit(1)
        elif decision == 'y':
            break
        else:
            print('Invalid input.')
    emptyDict = {}
    emptyStr = ''
    with open('./commands/globalpickle/masterSource.pickle', 'wb') as file:
        pickle.dump(emptyDict, file)
    with open('./commands/globalpickle/masterCate.pickle', 'wb') as file:
        pickle.dump(emptyDict, file)
    with open('./commands/globalpickle/listStrSource.pickle', 'wb') as file:
        pickle.dump(emptyStr, file)
    with open('./commands/globalpickle/listStrCate.pickle', 'wb') as file:
        pickle.dump(emptyStr, file)
    print('New files generated successfully.')
    sys.exit(1)
