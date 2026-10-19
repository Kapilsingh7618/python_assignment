# Task 1
# song_durations={
#     "song1":4.5,
#     "song2":2.5,
#     "song3":3.5,
#     "song4":5.5,
# }
# def get_song_duration(song_name):
#     try:
#         return song_durations[song_name]
#     except KeyError:
#         return "Song not found on Spotify !"
# print(get_song_duration("song1"))
# print(get_song_duration("song2"))
# print(get_song_duration("song8"))

# Task 2
# try:
#     price=float(input("Enter product price:"))
#     quantity=int(input("Enter quantity:"))
#     total_price=price*quantity
#     print("Total order Amount:",total_price)
#
# except ValueError:
#     print("Error : please enter valid number!")
#

# Task 3
# def book_movie_ticket():
#     wallet_balance=1000
#
#     try:
#         tickets=int(input("Enter number of tickets:"))
#
#         price_per_ticket=wallet_balance/tickets
#         print("Price per ticket:",price_per_ticket)
#
#     except ZeroDivisionError:
#         print("Error : number of tickets cannot be zero!")
#
#     except ValueError:
#         print("Error : please enter valid number!")

#
# book_movie_ticket()


# task 4
my_list = [1, 2, 3]
my_dict = {"a": 1}
try:
    print(my_list[5])
except IndexError:
    print("Error : list index does not exist!")

try:
    print(my_dict["b"])
except KeyError:
    print("Error : Dictionary key does not exist!")

