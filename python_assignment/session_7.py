# task 1
fruits = ["apple", "banana", "mango","orange"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
# from email import message

# task 2
foods=["pizza","burger","pasta","sandwich","burger king"]
for food in foods:
    if food == "burger king":
        print("found burger king, stopping search.")
        break
    print(food)

# task 3
playlists = ["chill vibes","workout","focus","party"]
for playlist in playlists:
    if playlist == "focus":
        pass
    else:
        print(playlist)

# task 4
messages=["hii","spam","hello","how are you?"]
for msg in messages:
    if msg == "spam":
        continue
    elif msg == "how are you?":
        break
    print(msg)




