#!~/.virtualenvs/flixsterP3/bin/python3.5
import json
import pprint
import requests


class Rating(object):

    def __init__(self, user_id, num_ratings):
        """ defines url based on given user id and number of ratings """
        if user_id is None:
            raise KeyError('user id cannot be empty')
        if num_ratings is None:
            raise KeyError('number of ratings must be set')

        self.url = 'http://www.flixster.com/api/users/{user}/movies/ratings?scoreTypes' \
                   '=numeric&page=1&limit={num_ratings}' \
            .format_map({'user': user_id, 'num_ratings': num_ratings})

    def read(self, filename='ratings.json'):
        """ reads data from url and saves it to filename """
        if filename is None:
            raise KeyError('filename must be set')

        r = requests.get(self.url)

        with open(filename, 'w') as f:
            f.write(r.text)
