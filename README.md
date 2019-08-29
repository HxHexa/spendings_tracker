# spendings_tracker

The spendings_tracker project, but written in Python instead. Currently a WIP, but I got as many things done in one day as opposed to 48 hours in comparison to the C++ version. Of course, this one is a lot slower in comparison (and a lot less impressive I think), but it is good at just making it work.

## To-Do:

 - Set up command-line arguments for interacting with the program
    + Commands list: newsrc addentry listsrc viewsrc viewcate delsrc delcate delentry
    + (DONE) Commands list: newcate listcate
 
 - (DONE) Work with pickle to allow for storage of class data between usage
 
 A "version 0.1" will probably come out when all the basic functionalities are, well, functional enough for me to be able to use it on a daily basis.

## Further To-Do:

*if I have the time for it*

- Monthly/weekly/daily tracking (probably with using a tree structure but there must be a better way)

- Tracking of earnings (actually this should be pretty easy to do. Just take the entry and negate the amount. Will get to this one eventually)

- Tracking of debts/loans and eventually credit cards (the reason why I do not want to do this one immediately personally is because I pay all my credit card debt before the end of the month, so my credit and bank account are basically interchangable. It's not like anybody is going to use this piece of crap aside from me anytime soon anyways haha)

- Exporting to csv

- Foreign exchange?

- An actual GUI

## Usage:

*well this is useless anyways since this is a 'personal project' and all but hey, it makes the thing looks more complete, which makes me feel better*

### Installation:

Simply download the source code and run main.py. This is a fully command-line program for now.

### Commands:

These helps will also be displayed with the built-in help commands. You can input the commands by passing it in as an argument, like such:

```
./main.py newcate 'books'
```

newcate \<name\>: Create a new category to put spendings under.

listcate: List all created categories

## FAQ:

### 1) But why?

(Asked mainly by my friends) Mint exists, but that program sorts my spendings automatically, and I do not like that. It only makes things easier but that is about it. Personally I still spend money on things irresponsibly just to go on to Mint and be all sad and depressed (also this is not to mention how the automatic categorizing of spendings does not allow for unique cases for different people, and how it sorts things wrong sometimes as well. It also makes it way harder to track cash). How I used to do it (before I got lazy) was with a huge Excel sheet with month-to-month manual tracking, which really helped with making myself more aware of what I am spending my money on. It is the same idea here: fully manual and personalized spendings tracker system, for each user to be more responsbile and more aware of what they are spending their money on.
