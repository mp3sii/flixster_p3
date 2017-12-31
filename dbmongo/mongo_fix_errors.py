import json
import re

import requests
from bs4 import BeautifulSoup
from dbmongo.mongo_connection import collection_error, collection, collection_imdb
from dbmongo.get_omdb_key import get_omdb_key

api_key = get_omdb_key

# Those with errors, look them up on imdb manually and update them via prompt

errors_count = collection_error.find({'imdb_id': None}).count()
url = 'http://www.imdb.com/find?'
movie_url = 'http://www.imdb.com'

# Request fixes
for index, error in enumerate(collection_error.find({'imdb_id': None})):
    movie_title = error['movie']['title'].replace(' ', '+')
    payload = {'q': movie_title}
    r = requests.get(url, params=payload)
    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find_all(attrs={"class": 'result_text'})

    print(error['movie']['title'].ljust(90))
    print('=' * 150)
    p = re.compile('(?<=title/)tt\d+')
    imdb_dict = {}

    for ind, result in enumerate(table):
        s = re.search(p, result.a.get('href'))

        try:
            imdb_id = s.group()
        except AttributeError:
            imdb_id = ''

        imdb_dict[str(ind)] = imdb_id

        print(
            repr(ind).ljust(3),
            result.a.string.ljust(80),
            str(imdb_id).ljust(10),
            str(movie_url + result.a.get('href')).ljust(10))

    print('\n')
    my_input = input('select a number to assign fix the movie, leave blank if unknown:  ')
    try:
        my_input = int(my_input)
        if my_input in range(table.__len__()):
            if imdb_dict[str(my_input)] == '':
                print('the value you selected does not have a IMDB ID')
            else:
                error['imdb_id'] = imdb_dict[str(my_input)]
                collection_error.save(error)

    except ValueError:
        print('Not a Number was entered, movie {} will not be fixed'.format(error['movie']['title']))

    print('\n')

# Transfer results to movies
fixes = collection_error.find({'imdb_id': {"$ne": None}})


url = 'http://www.omdbapi.com/'
for fix in fixes:
    movie = collection.find_one({'_id': fix['flixster_id']})
    payload = {'i': fix['imdb_id'], 'apikey': api_key}
    r = requests.get(url, params=payload)
    try:
        response_json = r.json()
        if response_json['Response'] == 'False':
            pass
        else:
            movie['imdb'] = response_json
            # INSERT INTO IMDB if it does not exist
            if not collection_imdb.find_one({'imdbID': fix['imdb_id']}):
                response_json['flixster_id'] = movie['_id']
                collection_imdb.insert_one(response_json)

            # UPDATE MOVIES
            collection.save(movie)

            # DELETE FROM ERRORs
            collection_error.delete_one({'_id': fix['_id']})
            #
    except json.decoder.JSONDecodeError:
        pass
