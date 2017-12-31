# /usr/bin/env python
import csv
import json

import requests
from clint.textui import progress


class Rating(object):

    def __init__(self, user_id, num_ratings=500, score_types=None):
        """ defines url based on given user id and number of ratings """
        if user_id is None:
            raise KeyError('user id cannot be empty')
        if num_ratings is None:
            raise KeyError('number of ratings must be set')

        self.url = 'http://www.flixster.com/api/users/{user}/movies/ratings?'.format_map({'user': user_id})
        self.payload = {'limit': num_ratings, 'scoreTypes': score_types}

    def read(self, filename='ratings.json'):
        """ reads data from url and saves it to filename """
        if filename is None:
            raise KeyError('filename must be set')

        r = requests.get(url=self.url, params=self.payload, stream=True)

        with open(filename, 'w') as f:
            try:
                total_length = int(r.headers.get('content-length'))
                for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
                    if chunk:
                        f.write(chunk)
                        f.flush()
            except TypeError:

                f.write(r.text)

    @staticmethod
    def csv_parse(self, filename='ratings.csv'):
        try:

            with open('ratings.json', 'r') as f:
                raw_data = f.read()

            ratings = json.loads(raw_data)
            with open(filename, 'w') as c:
                rating_writer = csv.writer(c, dialect='unix')
                rating_writer.writerow(['movieId',
                                        'title',
                                        'Lat Updated',
                                        'score',
                                        'ratingSource',
                                        'review',
                                        'year',
                                        'runningTime',
                                        'Rotten',
                                        'AudienceScore'])

                for rating in ratings:
                    rating_writer.writerow(
                        [
                            rating['movieId'],
                            rating['movie']['title'],
                            rating['score'],
                            rating['lastUpdated'],
                            rating['ratingSource'],
                            rating['review'],
                            rating['movie']['year'],
                            rating['movie']['runningTime'],
                            rating['movie']['tomatometer'],
                            rating['movie']['audienceScore']
                        ]
                    )
        except FileNotFoundError:
            # if ratings.json does not exist then create it
            self.read()
            # re-run
            self.csv_parse()
