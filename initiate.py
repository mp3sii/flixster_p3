# /usr/bin/env python
import argparse
from ratings.ratings import Rating

parser = argparse.ArgumentParser('Retrieves ratings from flixster, given a Flixster userId')
parser.add_argument("flixster_user",
                    help=('This is the user id that is displayed on your profile,'
                          'https://www.flixster.com/user/<FLIXSTER_USER>/wts/'
                          'This is is a 9 digits user Id'),
                    type=int)
parser.add_argument('-r', '--ratings',
                    help='if ratings flag is established "Wanted/Not Wanted to See movies" will not be displayed ',
                    action="store_true")
args = parser.parse_args()

flixster_user = int(args.flixster_user)

if args.ratings:
    ratings_flag = 'Only Rated Movies'
    score_types = 'numeric'
else:
    ratings_flag = 'All Movies'
    score_types = None

print('FlixsterUser         {user}          => OK'.format_map({'user': flixster_user}))
print('RatingsFlag          {r_flag}        => OK'.format_map({'r_flag': ratings_flag}))


r = Rating(user_id=flixster_user, score_types=score_types)
print('Downloading Flixster Ratings for {} into ratings.JSON'.format(flixster_user))
r.read()
