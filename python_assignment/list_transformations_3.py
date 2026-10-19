# Task 1
from python_assignment.session_2 import restaurant_name

cricket_scores=[56.7,102.3,88.9,45.2,120.8]
rounded_scores=[]

for score in cricket_scores:
    rounded_scores.append(round(score))

print("Original_scores : ",cricket_scores)
print("rounded_scores : ",rounded_scores)

# task 2
ratings=[4.2,3.8,4.9,2.5,4.0]
sorted_ratings=sorted(ratings,reverse=True)
print("Ratings : ",sorted_ratings)

# Task 3
product=["Mobile","Mouse","Laptop","Monitor","Keyboard"]
product.sort()
print("Sorted products : ",product)

# Task 4
restaurant_Name = ["Burger Hub","Pizza point","Zomato"]
Delivery_time   = [30,25,40]

for restaurant , Time in zip (restaurant_Name,Delivery_time):
    print(restaurant, "-", Time,"Min")

# Task 5
def process_views(titles,views):
    return [(title,round(view,-3)) for title,view in zip(titles,views)]

titles = ["Python Tutorial","AI Tutorial","Wed Development"]
view = [12500,34800,27600]

result = process_views(titles,view)
print(result)

