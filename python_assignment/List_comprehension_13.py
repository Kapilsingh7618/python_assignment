# Task 1 Even numbers
even_numbers = [x for x in range(10,50) if x % 2 == 0]
print("even_numbers:",even_numbers)

# Task 2 Nested list comprehension

playlists=[[210,180,240],[150,200],[300,120,90]]
result=[duration for playlist in playlists
        for duration in playlist
        if duration > 200]
print("result:",result)


# Task 3
names=["Shoes","Bag","Watch","Headphones"]
prices=[999,1500,700,2200]
result=[(name,price) for name,price in zip(names,prices) if price>1000]
print("result =",result)


# Task 4
ratings=[
    [4,5,3,2],
    [5,4,4,3],
    [3,2,5,5,]
]
result=[rating for row in ratings for rating in row if rating>4]
print("result =",result)


