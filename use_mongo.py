# /usr/bin/env python
from dbmongo import mongo_connection
mongo_connection


options = list()
options.append({'key': 1, 'description': 'Insert/Update movies from flixster into Default collection '})
options.append({'key': 2, 'description': 'Retrieve data from IMDB and merge with moves'})
options.append({'key': 3, 'description': 'Fix errors of imdb'})

print('Select an option')
for option in options:
    print(
        str(option['key']).ljust(4),
        option['description'].ljust(20)

    )

selection = input('Select an option: ')

try:
    selection = int(selection)
    if selection == 1:
        from dbmongo import mongo_insert_movies
    elif selection == 2:
        from dbmongo import mongo_insert_imdb
    elif selection == 3:
        from dbmongo import mongo_fix_errors
    else:
        print('Option not valid')
except ValueError:
    print('Option not valid')
