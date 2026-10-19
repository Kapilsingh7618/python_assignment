# Task 1
file=open("my_fav_songs.txt","w")
file.write("Song1\n")
file.write("Song2\n")
file.write("Song3\n")
file.write("Song4\n")
file.write("Song5\n")



# Task 2
file=open("my_fav_songs.txt","r")
songs=file.readlines()
for number,song in enumerate(songs,start=1):
    print(number,song.strip())

# Task 3
file=open("my_fav_songs.txt","a")
file.write("Song6\n")
file.write("Song7\n")

print("2 song added successfully")

# Task 4
file=open("my_fav_songs.txt","r")
songs=file.readlines()
total_songs=len(songs)
for number,song in enumerate(songs,start=1):
    print(number,song.strip())

print("Total_Songs:",total_songs)
file.close()
