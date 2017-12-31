# /usr/bin/env python
import json
from pymongo import MongoClient

# Establishes a Mongo Connection, by using the default parameters or provided parameters in a setup.json file

try:
    file = open('setup.json', 'r')
    raw_data = file.read()
    setup_data = json.loads(raw_data)

    # Setup MongoClient
    try:
        client_host = setup_data['mongo_host']
    except KeyError:
        client_host = 'localhost'
    try:
        client_port = int(setup_data['mongo_port'])
    except KeyError:
        client_port = 27017
    except ValueError:
        raise ValueError('Error: The mongo port must be an integer')

    client = MongoClient('localhost', 27017)

    try:
        db = client[setup_data['mongo_client']]
    except KeyError:
        db = client['movies']

    try:
        collection = db[setup_data['mongo_movies_collection']]
    except KeyError:
        collection = db['movies']

    try:
        collection_imdb = db[setup_data['mongo_movies_imdb']]
    except KeyError:
        collection_imdb = db['movies_imdb']

    try:
        collection_error = db[setup_data['mongo_movies_error']]
    except KeyError:
        collection_error = db['movies_imdb_error']

    file.close()


except FileNotFoundError:
    client = MongoClient('localhost', 27017)
    db = client['movies']
    collection = db['movies']
    collection_imdb = db['movies_imdb']
    collection_error = db['movies_imdb_error']

except json.JSONDecodeError:

    raise json.JSONDecodeError('The JSON you provided in setup.json is not valid')


