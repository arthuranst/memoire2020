from itertools import islice
from math import ceil

from datetime import datetime
from itertools import dropwhile, takewhile

from instaloader import Instaloader, Profile, Post
l = Instaloader(dirname_pattern="/Users/arthuranst/Desktop/memoire/DL-PATH")
l.download_post(post, filename)

USERSPROFILE = 'arthuranst'
X_percentage = 10   

L = Instaloader()

SINCE = datetime(2020, 9, 1)
UNTIL = datetime(2018, 9, 1)

profile = Profile.from_username(L.context, USERSPROFILE)
posts_sorted_by_likes = sorted(profile.get_posts(),
                               key=lambda p: p.likes + p.comments,
                               reverse=True)

for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * X_percentage / 100)):
    if (post.datetime <= SINCE and post.datetime >= UNTIL):
        L.download_post(post, USERSPROFILE)

    