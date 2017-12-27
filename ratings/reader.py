#!~/.virtualenvs/flixsterP3/bin/python3.5

import csv
import json

with open('ratings.json', 'r') as f:
    raw_data = f.read()

ratings = json.loads(raw_data)
with open('ratings.csv', 'w') as c:
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

# TODO write proper Readme
# TODO think on whether ui is necessary
# TODO hook with SQLlite
# TODO hook with IMDB_API