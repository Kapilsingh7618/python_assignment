# Task 1
# class InvalidCuponCodeError(Exception):
#     pass
# valid_cupons = ["SAVE10","FOOD20","WELCOME"]
#
# def apply_cupon(cupon_code):
#     if cupon_code not in valid_cupons:
#         raise InvalidCuponCodeError("Invalid Cupon Code")
#     print("Cupon applied successfully")
# try:
#     apply_cupon("SAVE10")
# except InvalidCuponCodeError as e:
#     print("Error:",e)

# Task 2

# class SongAlreadyExistsError(Exception):
#     pass
# playlist=["Perfect","Believer"]
# def add_song_to_playlist(song_name,playlist):
#     if song_name in playlist:
#         raise SongAlreadyExistsError("Song Already Exists in playlist")
#     playlist.append(song_name)
#     return playlist
# add_song_to_playlist("song123",playlist)
# print(playlist)
# add_song_to_playlist("Perfect",playlist)

# Task 3
# class PaymentFailedError(Exception):
#     pass
# def process_payment(amount):
#     if amount <=0:
#         raise PaymentFailedError("Payment amount must be greater than 0")
#     print("Payment Successful")
# try:
#     process_payment(-100)
# except PaymentFailedError as e:
#     print("Payment Failed : ",e)

# Task 4
class InvalidSeatNumberError(Exception):
    pass

def book_ticket(movie_name,seat_number):
    if seat_number <= 0 :
        raise InvalidSeatNumberError("Seat Number Must Be Positive!")
    print(f"Ticket Booked for {movie_name}")
    print(f"Seat Number : {seat_number}")

try:
    book_ticket("Avengers",2)
except InvalidSeatNumberError as e:
    print("Booking Error : ",e)
