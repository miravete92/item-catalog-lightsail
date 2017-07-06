Logs analysis project
=====================

### By Alberto Miravete

## Description

This application can be used to store items and organize them in categories.

You can browse created items and categories and see their description.

If you want to create new items, you must log-in with an external authentication client.

An API endpoint is also avilable to get item list filtered by category.

You cannot edit or delete other user's items.

## Installation

Make sure you have all these python modules installed with python 2.7

+ sqlalchemy
+ oauth2client
+ httplib2
+ flask
+ requests

Run these python programs to setup the database

1. From this folder, run *python database_setup.py*

2. Run *populate_categories.py* to insert some categories in database

## How to run it

To run the program just type in *python item_catalog.py*

Server is now up! Point to *localhost:5000* from host computer to test it.

Remember that if you want to create itens you have to log in.

## API endpoints

+ */catalog.json* - Returns a list of all items
+ */catalog/Snowboarding.json* - Returns a list of Snowboarding items (You can check other categories instead with */catalog/<name_of_category>.json*)

## Design

*logsdb.py* file contains query methods to fetch the information from database.

*logs.py* file only calls these methods and prints them in plain text.

*output.txt* file contains a sample output of the program *logs.py*

## Notes

You can redirect the output to a file using python *logs.py > output.txt*