from itertools import islice
from math import ceil

from datetime import datetime

from instaloader import Profile, Instaloader

USERSPROFILE = 'arthuranst'
X_percentage = 10   

L = Instaloader(dirname_pattern="/Users/arthuranst/Desktop/memoire/DL-PATH")
# You're initializing the Instaloader class here with your dirname_pattern argument

SINCE = datetime(2020, 9, 1)
UNTIL = datetime(2018, 9, 1)

profile = Profile.from_username(L.context, USERSPROFILE)
print(profile) # <Profile arthuranst (7569736126)>

posts_sorted_by_likes = sorted(profile.get_posts(),
                               key=lambda p: p.likes + p.comments,
                               reverse=True)
print(posts_sorted_by_likes)  # should output the sorted list

for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * X_percentage / 100)):
    if (post.date <= SINCE and post.date >= UNTIL):
        #changed datetime to date here
        print('Downloading post with the caption:',post.caption)
        # Downloading post with the caption: coloris — publication and program 
        L.download_post(post, USERSPROFILE)
