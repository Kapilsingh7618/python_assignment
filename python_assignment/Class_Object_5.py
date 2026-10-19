# Task 1
# class Song:
#     def __init__(self,title,artist,duration):
#         self.title = title
#         self.artist = artist
#         self.duration = duration
#     def display(self):
#         print("Song : ",self.title)
#         print("Artist : ",self.artist)
#         print("Duration : ",self.duration)
# song1=Song("Kesariya","Arijit Singh",250)
# song1.display()
# song2=Song("Believer","Imagine Dragon",260)
# song2.display()

# task 2
# class FoodOrder:
#     def __init__(self,restaurant_name,items,total_price):
#         self.restaurant_name = restaurant_name
#         self.items = items
#         self.total_price = total_price
#     def show_order(self):
#         print("Restaurant :",self.restaurant_name)
#         print("Items:",self.items)
#         print("Total Price:",self.total_price)
#
# F=FoodOrder("Domino's",["Pizza","Garlic Bread"],450)
# F.show_order()

# Task 3
# class InstagramPost:
#     def __init__(self,caption,likes,comments):
#         self.caption = caption
#         self.likes = likes
#         self.comments = comments
#     def add_comment(self,comment_text):
#         self.comments.append(comment_text)
#         self.likes += 1
#     def show_comments(self):
#         print("Caption:",self.caption)
#         print("Likes:",self.likes)
#         print("New Comments:",self.comments)
# i=InstagramPost("my first post",100,[])
# i.add_comment("Nice photo")
# i.show_comments()


# Task 4
class Movie:
    def __init__(self,title,ratings):
        self.title = title
        self.ratings = ratings
    def show_movie(self):
        print("Title:",self.title)
        print("Ratings:",self.ratings)
m=Movie("Javan",4.5)
m.show_movie()
