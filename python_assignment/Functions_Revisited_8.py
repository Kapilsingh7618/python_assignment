# Task 1
# def calculate_total(prices,quantity):
#     return prices * quantity
#
# result=calculate_total(120,3)
# print(result)

# Task 2
# def forment_username(username,prefix="user"):
#     return prefix+ "_"+username
# print(forment_username("kapil","developer"))
# print(forment_username("kapil"))

# Task 3
def book_movie_ticket(movie_name,seat_type="regular",snacks=None):
    print("movie  : ",movie_name)
    print("seat   : ",seat_type)
    print("snacks : ",snacks)
    return movie_name,seat_type,snacks

# Positional arguments
# book_movie_ticket("Javan","regular","Popcorn")

# Keyword argument
# book_movie_ticket(movie_name="Javan",seat_type="VIP",snacks="Popcorn")

# Mixed argument
# book_movie_ticket("Javan",seat_type="VIP",snacks="Popcorn")

# Task 4
def apply_coupon(amount,coupon_code=None):
    if coupon_code == "SAVE10":
        discount = amount * 10/100
        final_amount = amount - discount
    else:
        final_amount = amount
    return final_amount
result = apply_coupon(1000,"SAVE10")
print("Total amount :" ,result)
print(apply_coupon(1000,))


