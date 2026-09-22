# task 1 food delivery apps
food_apps=["Zomato","Swiggy","Domino's","McDonald's","Pizza Hut"]
for apps in food_apps:
    print(apps)

# task 2
user_bio="music lover|foodie|traveller"
count=0
for character in user_bio:
    if character!= " ":
        count+=1
# print("number of characters in user_bio is",count)

# task 3
favorite_movie=["Zindagi na milegi dobara","karwaan","fitor"]
for movie in favorite_movie:
    print(movie.upper())

# task 4
word=input("enter a word:")
for character in word:
    if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
        print(character)