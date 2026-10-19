# Task 1
# cart = {}
# cart["kapil"] = {
#     "items": [
#         {"name":"laptop",
#          "quantity":1,
#          "price":70000},
#         {"name":"Mouse",
#          "quantity":2,
#          "price":2000}
#     ]
# }
# cart["Karan"] = {
#     "items": [
#         {"name":"Mobile",
#          "quantity":1,
#          "price":10000},
#         {"name":"Keyboard",
#          "quantity":2,
#          "price":15000}
#     ]
# }
# cart["Singh"] = {
#     "items": [
#         {"name":"Monitor",
#          "quantity":1,
#          "price":1000},
#         {"name":"Keyboard",
#          "quantity":2,
#          "price":1500},
#         {"name":"Headphone",
#          "quantity":3,
#          "price":2000}
#
#     ]
# }
# print(cart)

# Task 2
def add_song_to_playlist(playlists,user,playlist_name,song_title,artist):

    if  playlist_name not in playlists:
        playlists[user] = {}
    if playlist_name not in playlists[user]:
        playlists[user][playlist_name] = []

    song = playlists[user][playlist_name]
