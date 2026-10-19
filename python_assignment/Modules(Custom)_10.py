# Task 1
def add_song(song_name,playlist):
    playlist.append(song_name)
    return playlist
def remove_song(song_name,playlist):
    if song_name in playlist:
        playlist.remove(song_name)
        return playlist
def display_playlist(playlist):
    print("My Playlist")
    for position, song in enumerate(playlist,start=1):
        print(f"{position}. {song}")
my_playlist=[]
my_playlist = add_song("Bella",my_playlist)
my_playlist = add_song("Believer",my_playlist)
print(my_playlist)

# Task 2

