import json
import requests
from dbmongo.mongo_connection import collection, collection_imdb, collection_error
from dbmongo.get_omdb_key import get_omdb_key

api_key = get_omdb_key

rating_count = collection.find({'imdb': None}).count()
print(rating_count)
counter = 0

for rating in collection.find({'imdb': None}):
    # Movies with already an imdb will be skipped
    counter += 1
    print('{counter} of {total}, movie: {movie}'
          .format_map({'counter': counter,
                       'total': rating_count,
                       'movie': rating['title']})
          )
    payload = {'t': rating['title'], 'apikey': api_key, 'year': rating['movie']['year']}
    url = 'http://www.omdbapi.com/'
    imdb_full = collection_imdb.find_one({'Title': rating['title'], 'Year': str(rating['movie']['year'])})
    imdb_partial = collection_imdb.find_one(({'Title': rating['title']}))

    if imdb_full:
        # If the movie is already in the Mongo IMDB (uses year and title), then establishes the link both ways
        imdb_full['flixster_id'] = rating['_id']
        collection_imdb.save(imdb_full)
        rating['imdb'] = imdb_full
        collection.save(rating)

    elif imdb_partial:
        # If the movie does not match a 100% insert into the errors db
        rating['imdb_id'] = imdb_partial['_id']
        collection_error.insert_one(rating)

    else:
        # if not check if valid response, then load it, else insert it
        r = requests.get(url, params=payload)
        try:
            response_json = r.json()
            if response_json['Response'] == 'False':
                rating['error'] = 'Error Response'
                rating['error_response'] = r.text
                rating['flixster_id'] = rating['_id']
                collection_error.insert_one(rating)
            else:
                response_json['flixster_id'] = rating['_id']
                collection_imdb.insert_one(response_json)
        except json.decoder.JSONDecodeError:
            pass

