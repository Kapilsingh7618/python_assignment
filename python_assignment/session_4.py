# task 1 instagram account eligibility

age=int(input("enter your age:"))
if age>=13:
    print("you are eligible to creat an account on instagram")
else:
    print("you are not eligible to create an account on instagram")


# task 2 find marks grade
marks =int(input("enter your marks:"))
if marks >=90:
    print("grade:A")
elif marks >=75:
    print("grade:B")
elif marks >=60:
    print("grade:C")
elif marks >=40:
    print("grade:D")
else:
    print("grade:F")


# task 3 Zomato late night order
age=int(input("enter your age:"))
current_time=int(input("enter your current time (24-hours formet):"))
if age>=18:
    if current_time>=22 or current_time<=2:
        print("order allowed")
    else:
        print("order not allowed")


# task 4 cricket score
score=int(input("enter your favorite cricket team score:"))
if score>=200:
    print("high score")
elif score>=150:
    print("good score")
elif score>=100:
    print("Average")
else:
    print("need improvement")








