import json
from mongo_connection import collection

# Read Json
with open('ratings.json', 'r') as f:
    raw_data = f.read()
ratings = json.loads(raw_data)

# Insert Data
# TODO replace this to only insert if not exist
collection.drop()
result = collection.insert_many(ratings)

