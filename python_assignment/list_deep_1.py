# Task 1
fav_items=["Music",21,10.5,True]
print("Original list : ",fav_items)

# Task 2
fav_items=["Music",21,10.5,True]
fav_items[0]="Song"
fav_items[1] = fav_items[1]+1
print("Update list :",fav_items)

# Task 3
fav_items=["Music",21,10.5,True]
del fav_items[2]
print("After removing mobile data :",fav_items)

# Task 4
weekend_plan=["Gym","Study","Movie","Shopping","Coding"]
remove_item=weekend_plan.pop()
print("Remove item  : ",remove_item)
print("Update Weekend plan : ",weekend_plan)
