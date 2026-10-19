# Task 1
# class User:
#     def __init__(self,username,email):
#         self.username = username
#         self.email = email
#     def show_user(self):
#         print("Username : ",self.username)
#         print("Email : ",self.email)
# u=User("Kapil123","Kapil@gmail.com")
# u.show_user()

# Task 2
# class User:
#     def __init__(self,username,email):
#         self.username = username
#         self.email = email
# class Influencer(User):
#     def __init__(self,username,email,followers):
#         super().__init__(username,email)
#         self.followers = followers
#     def show_user(self):
#         print("Username : ",self.username)
#         print("Email : ",self.email)
#         print("Followers : ",self.followers)
# influencer=Influencer("Kapil123","Kapil@gmail.com",1500)
# influencer.show_user()


# Task 3
# class User:
#     def __init__(self,username,email):
#         self.username = username
#         self.email = email
#     def show_user(self):
#         print("Username : ",self.username)
#         print("Email : ",self.email)
# class Influencer(User):
#     def __init__(self,username,email,followers):
#         super().__init__(username,email)
#         self.followers = followers
# class VerifiedInfluencer(Influencer):
#     def __init__(self,username,email,followers,badge):
#         super().__init__(username,email,followers)
#         self.badge = badge
#     def show_user(self):
#         print("Username : ",self.username)
#         print("Email : ",self.email)
#         print("Followers : ",self.followers)
#         print("Badge : ",self.badge)
# v=VerifiedInfluencer("Kapil123","Kapil@gmail.com",1500,"Blue Tick")
# v.show_user()

# task 4
# class User:
#     def __init__(self,username,email):
#         self.username = username
#         self.email = email
#     def show_user(self):
#         print("Username : ",self.username)
#         print("Email : ",self.email)
# class Influencer(User):
#     def __init__(self,username,email,followers):
#         super().__init__(username,email)
#         self.followers = followers
# class Brand(Influencer):
#     def __init__(self,username,email,followers,brand_name):
#         super().__init__(username,email,followers)
#         self.brand_name = brand_name
#     def show_user(self):
#         print("Username : ",self.username)
#         print("Email : ",self.email)
#         print("Followers : ",self.followers)
#         print("Brand Name : ",self.brand_name)
# BrandPartner=Brand("Kapil123","Kapil@gmail.com",1500,"Nike")
# BrandPartner.show_user()

# Task 5
class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email
class Influencer(User):
    def __init__(self,username,email,followers):
        super().__init__(username,email)
        self.followers = followers
class VerifiedInfluencer(Influencer):
    def __init__(self,username,email,followers,badge):
        super().__init__(username,email,followers)
        self.badge = badge
    def display_profile(self):
        print("Username : ",self.username)
        print("Email : ",self.email)
        print("Followers : ",formet_followers(self.followers))
        print("Badge : ",self.badge)
def formet_followers(followers):
        if followers>=1000000:
            return str(followers/1000000)+"M"
        elif followers>=1000:
            return str(followers/1000)+"K"
        else:
            return str(followers)
v=VerifiedInfluencer("Kapil123","Kapil@gmail.com",1500,"Blue Tick")
v.display_profile()


