# Task 1
# square = lambda x: x*x
# for i in range(1,6):
#     print(square(i))

# Task 2
# prices = [120,250,99,180,310]
# Service_charge = list(map(lambda price: price+(price*10/100),prices))
# print(Service_charge)

# Task 3
# users = [("raj",180),
#         ("simran",1500),
#         ("veer",1200),
#         ("zara",900)
# ]
# result = list(filter(lambda x:x[1]>1000,users))
# for user in result:
#     print(result)

# Task 4
# pairs = [(3,4),(5,2),(7,8)]
# calculate = lambda a,b:( a+b,a*b)
# result = [calculate(a,b) for a,b in pairs]
# print(result)

# Task 5
is_palindrome = lambda text : text == text[::-1]
print(is_palindrome("hello"))
print(is_palindrome("madam"))
print(is_palindrome("python"))

# user define
while True:
    text = input("Enter a text : ")
    check_palindrome = lambda text : text == text[::-1]

    if check_palindrome(text):
        print("Palindrome")
        break
    else:
        print("Not Palindrome")




