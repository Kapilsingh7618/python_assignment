# Task 1
import math
number  = [16,49,81]
for num in number:
    print(math.sqrt(num))
print(math.sqrt(number[0]))
print(math.sqrt(number[1]))
print(math.sqrt(number[2]))

# Task 2
# import math
# prices = [199.1,349.8,599.3]
# for price in prices:
#     print(math.ceil(price))


# Task 3
# import math
# bill = 500
# discount = bill *10/100
# final_bill = bill - discount
# final_amount = math.floor(final_bill)
# print("Original Bill: ",bill)
# print("Discount: ",discount)
# print("Final Bill: ",final_amount)

# Task 4
# import random
# dice = random.randint(1,6)
# print("Dice Result: ",dice)

# Task 5
import random
songs =[
    "Kesariya",
    "Believer",
    "Perfect",
    "Shape of you",
    "Bella",
    "Story"
]
daily_playlist = random.sample(songs,3)
print("Today Playlist :")
for song in daily_playlist:
    print(song)