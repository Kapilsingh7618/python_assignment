# Task 1
products = ["Laptop","Mouse","Keyboard"]
prices = [65000,800,1500]
product_dict = dict(zip(products,prices))
print(product_dict)


# Task 2
username = ["kapil","Rahul","Amit"]
followers = [2300,1500,4000]
followers_dict = {}
for i in range(len(username)):
    followers_dict[username[i]] = followers[i]

print(followers_dict)

# Task 3
teams = ["CSK","MI","RCB","GT"]
points = [12,8,15,10]
team_points = dict(zip(teams,points))
for team in team_points:
    if team_points[team] > 10:
        print(team,team_points[team])


# Task 4
titles = ["Inception","3 Idiots","Dangle"]
genres = ["Sci-Fi","Comedy","Drama"]
ratings = [8.8,8.4,8.3]

movies = []

for title,genre,rating in zip(titles,genres,ratings):
    movie = {"title":title,"genre":genre,"rating":rating}
    movies.append(movie)

print(movies)



