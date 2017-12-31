import json

from dbmongo.mongo_connection import collection

# Read Json
with open('ratings.json', 'r') as f:
    raw_data = f.read()
ratings = json.loads(raw_data)

# Insert Data

if collection.find().count():
    for rating in ratings:
        movie = collection.find_one({'movie.id': rating['movie']['id']})
        if movie:
            # if the movie is already in the collection, update the score
            collection.update_one({'_id': movie['_id']},
                                  {'$set': {'score': movie['score']},
                                   "$currentDate": {"recordLastModified": True}
                                   })
        else:
            collection.insert_one(rating)


else:
    # If there are no records, drop and bulk insert is faster
    collection.drop()
    result = collection.insert_many(ratings)
