from steam import Steam
from decouple import config

import json

KEY = config("STEAM_API_KEY")

steam = Steam(KEY)

# arguments: steamid
owned_games = steam.users.get_owned_games("76561198287638114")
with open('owned_games.json', 'w') as f:
    json.dump(owned_games, f)
    
user = steam.users.get_user_details("76561198287638114")
with open('user.json', 'w') as f:
    json.dump(user, f)    

recent_games = steam.users.get_user_recently_played_games("76561198287638114")
with open('recent_games.json', 'w') as f:
    json.dump(recent_games, f) 
    
badges = steam.users.get_user_badges("76561198287638114")
with open('badges.json', 'w') as f:
    json.dump(badges, f)

