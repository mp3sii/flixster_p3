# Flixster Ratings
This program exports the user data from [flixster](https://www.flixster.com) and loads it into a [json](https://www.json.org) and a CSV.
Then the program allows (optional):
* Store the data into Mongo:
	* Load the data into a local MONGO DB. 
	* Match the results to IMDB, by Title and Year using [OMDB API](http://www.omdbapi.com/). You will have to provide your own API_Key, request it [here](http://www.omdbapi.com/apikey.aspx) 
		* If the year does not match, or there is an Error Response, those movies, are loaded into an Errors Collection on Mongo to be Fixed.
	* Fix the errors by looking up directly on IMDB on a movie per movie and prompting the user to select the movie
## Credits
[mmihaljevic](https://github.com/mmihaljevic/flixter) for discovering how to retrieve the flixster ratings json location. mmihaljevic core ratings module has been adapted to python 3 and modified as explained before. 

# Installation
**Requires Python 3**
0. Clone this repo
1. Make virtualenv with Python 3 (I recommend using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io))  

```bash
mkvirtualenv your_repo -p /usr/local/bin/python3
```
2. Install the requirements

```bash
pip install requirements.txt
```

3. Optional, create a setup.json file in the module root for providing the OMDB API Key, and to modify the mongo defaults (example)

```json
{
  "api_key": "your_api_key",
  "mongo_host": "localhost",
  "mongo_port": 27017,
  "mongo_client": "movies",
  "mongo_movies_collection": "movies",
  "mongo_movies_imdb": "movies_imdb",
  "mongo_movies_error": "movies_imdb_error"
}
```

# Usage
## Step 1: Download the user flixster ratings onto a JSON
In terminal, execute `python initiate.py <your user>`. This will create/replace a `ratings.json` file on your directory, and a `ratings.csv` with a subset of the attributes
