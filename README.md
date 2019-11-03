# spendings_tracker

The spendings_tracker project, but written in Python instead. Currently a WIP, but I got as many things done in one day as opposed to 48 hours in comparison to the C++ version. Of course, this one is a lot slower in comparison (and a lot less impressive I think), but it is good at just making it work.

## To-Do:

 - Set up command-line arguments for interacting with the program
    + (DONE) Commands list: newsrc addentry listsrc viewsrc viewcate delsrc delcate delentry
    + (DONE) Commands list: newcate listcate

 - (DONE) Work with pickle to allow for storage of class data between usage

 A "version 0.1" will probably come out when all the basic functionalities are, well, functional enough for me to be able to use it on a daily basis.

### Update 3/11/19:

I finally got back to finishing this once I realise my financial issues cannot be ignored anymore, but anyways, all the basic functionalities are up and going! v0.1 is out! Anyways, here are the next TODOs:

- Set up support for debts and loans (for use with credit cards and the likes)

- More misc commands like rename, set etc.

## Further To-Do:

*if I have the time for it*

- Monthly/weekly/daily tracking (probably with using a tree structure but there must be a better way)

- (DONE) Tracking of earnings (actually this should be pretty easy to do. Just take the entry and negate the amount. Will get to this one eventually)

- Tracking of debts/loans and eventually credit cards (the reason why I do not want to do this one immediately personally is because I pay all my credit card debt before the end of the month, so my credit and bank account are basically interchangable. It's not like anybody is going to use this aside from me anytime soon anyways haha)

- Exporting to csv

- Foreign exchange?

- An actual GUI

- A way to show common entries from multiple categories

- Main categories and sub-categories

## Usage:

### Installation:

Simply download the source code and run main.py. This is a fully command-line program for now.

### Commands:

These helps will also be displayed with the built-in help commands. You can input the commands by passing it in as an argument, like such:

```
./main.py newcate 'books'
```

Additionally, instead of 'src' or 'cate', you could instead type 'source' or 'category' in full, like 'newsource' or 'viewcategory'. This applies to all commands of the same format.

 - newsrc \<name\> \<amount\>: Create a new source to subtract spendings from. Amount is the amount of money already in the source.

 - newcate \<name\>: Create a new category to put spendings under.

 - listsrc: List all created sources.

 - listcate: List all created categories.

 - newentry \<name\> \<amount\>: Add a new spending entry. The command will prompt the user for the source to subtract the spending from and the categories to put it under, in addition to an optional note option if the user wants to add a note to the spending.

 - viewsrc \<name\>: View the details and the spendings made for a source.

 - viewcate \<name\>: View the details and the spendings put under a category. User can input multiple categories in a format similar to that in newentry to view the details on entries that are categorised under multiple categories.

 - viewentry: View the details of an entry under a specific source/category.

 - delsrc \<name\>: Deletes an empty source
 
 - delcate \<name\>: Deletes an empty category

 - delentry: Selects an entry to delete from all sources and categories

 - reset: Create new blank data. Should only be used if you are running the program for the first time, or when you want to delete everything and start anew.

## FAQ:

### 1) But why?

(Asked mainly by my friends) Mint exists, but that program sorts my spendings automatically, and I do not like that. It only makes things easier but that is about it. Personally I still spend money on things irresponsibly just to go on to Mint and be all sad and depressed (also this is not to mention how the automatic categorizing of spendings does not allow for unique cases for different people, and how it sorts things wrong sometimes as well. It also makes it way harder to track cash). How I used to do it (before I got lazy) was with a huge Excel sheet with month-to-month manual tracking, which really helped with making myself more aware of what I am spending my money on. It is the same idea here: fully manual and personalized spendings tracker system, for each user to be more responsbile and more aware of what they are spending their money on.
