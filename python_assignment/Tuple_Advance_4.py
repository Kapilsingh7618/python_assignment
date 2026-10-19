# Task 1
my_profile = ("kapil",22,"python",True)
print(my_profile)

# Task 2
playlist=("Shape of you","Blinding light","Believer","Senorita","Levitating")
print("Second_Song :",playlist[1])
print("Third_Song  :",playlist[2])
print("Fourth_Song :",playlist[3])
print(playlist[1:4])

# task 3
order=("Burger","Fries","Coke",)
order_list=list(order)
order_list.append("Ice cream")
order=tuple(order_list)
print(order)

# Task 4
insta_post = (
    101,
    "kapil",
    250,
    ["python","coding","learning"],
    True
)
print(insta_post)

print(type(insta_post[0]))
print(type(insta_post[1]))
print(type(insta_post[2]))
print(type(insta_post[3]))
print(type(insta_post[4]))


# Task 5
calls = (12,5,0,20,7,3,15)
calls_list = list(calls)
New_list = []
for call in calls_list:
    if call >= 5:
        New_list.append(call)

calls=tuple(New_list)
print(calls)

# list comprehension
cells = (12,5,0,20,7,3,15)
calls_list = list(cells)
calls_list = [call for call in calls_list if call >= 5]

calls_list = tuple(calls_list)
print(calls_list)



