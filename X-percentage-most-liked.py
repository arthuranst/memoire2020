#Load des outils
from itertools import islice
from math import ceil
from datetime import datetime

#Load de InstaLoader : https://instaloader.github.io
from instaloader import Profile, Instaloader

# Indiquer le nom du profil dans ''
USERSPROFILE = 'inijedar'

# Indiquer le % de publications désirées
X_percentage = 3

# Indiquer l'adresse locale d'enregistrement des fichiers
# Créer le dossier en local et le remplacer dans l'adresse à la place de ...
L = Instaloader(dirname_pattern="/Users/arthuranst/Desktop/memoire/DL-PATH/...")

# Paramètres de dates des publications, depuis X jusqu'à X
SINCE = datetime(2020, 2, 10)
UNTIL = datetime(2019, 1, 10)


profile = Profile.from_username(L.context, USERSPROFILE)

# Retourne le nom du profil dans la console
print(profile)

# Triage des publications en liste
posts_sorted_by_likes = sorted(profile.get_posts(),
                               key=lambda p: p.likes + p.comments,
                               reverse=True)

# Retourne la liste complète et triée des publications
print(posts_sorted_by_likes)

# Pour la liste retournée, récupération du % des publications les plus likes
for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * X_percentage / 100)):
    print("4")

    # Depuis X jusqu'à X
    if (post.date <= SINCE and post.date >= UNTIL):

    	# Retourne la validation du téléchargement dans la console
        print('Downloading post with the caption:',post.caption)

        # Téléchargement
        L.download_post(post, USERSPROFILE)