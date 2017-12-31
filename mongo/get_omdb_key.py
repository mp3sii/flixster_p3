# /usr/bin/env python
import json


def get_omdb_key():
    with open('setup.json', 'r') as f:
        raw_data = f.read()
        setup_data = json.loads(raw_data)

    try:
        api_key = setup_data['api_key']
    except KeyError:
        raise KeyError('a valid api_key for OMBD API must be provided')
    return api_key
