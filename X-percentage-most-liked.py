from itertools import islice
from math import ceil

from datetime import datetime
from itertools import dropwhile, takewhile

from instaloader import Instaloader, Profile as il
l = il.Instaloader(dirname_pattern="/Users/arthuranst/Desktop/memoire/DL-PATH")
l.download_post(post, filename)


PROFILE = 'arthuranst'
X_percentage = 10   

L = Instaloader()

SINCE = datetime(2020, 9, 1)
UNTIL = datetime(2018, 9, 1)

profile = Profile.from_username(L.context, PROFILE)
posts_sorted_by_likes = sorted(profile.get_posts(),
                               key=lambda p: p.likes + p.comments,
                               reverse=True)

for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * X_percentage / 100)):
    if (post.datetime <= UNTIL ):
        L.download_post(post, PROFILE)

    