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

Remember that if you want to create items you must to log in.

## Main Routes

### GET
+ *<server_ip>:5000/* - displays all categories and last 8 items added.
+ *<server_ip>:5000/catalog* - displays all categories and last 8 items added.
+ *<server_ip>:5000/catalog/<category>* - displays all items in category
+ *<server_ip>:5000/catalog/new* - displays new item window.
+ *<server_ip>:5000/catalog/<category>/<item>* - displays information about an item
+ *<server_ip>:5000/catalog/<category>/<item>/edit* - displays edit window for an item
+ *<server_ip>:5000/catalog/<category>/<item>/remove* - displays remove window for an item
+ *<server_ip>:5000/login* - displays login window

### POST
+ *<server_ip>:5000/catalog/new* - creates a new item.
+ *<server_ip>:5000/catalog/<category>/<item>/edit* - edits an item.
+ *<server_ip>:5000/catalog/<category>/<item>/remove* - removes an item
+ *<server_ip>:5000/disconnect* - user logs out


## API endpoints

+ */catalog.json* - Returns a list of all items
+ */catalog/Snowboarding.json* - Returns a list of Snowboarding items (You can check other categories instead with */catalog/<name_of_category>.json*)

## Design

*database_setup.py* file contains the source to setup database

*item_catalog.py* file contains the source code to start the server

*templates/* directory contains html templates that will be rendered by the webservice

*static/* directory contains static files like styles
