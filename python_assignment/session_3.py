# task 1

name=(input("enter your name:"))
food=(input("enter your favorite food:"))
print("hello",name,"," ,"your favorite food is",food +"!")

# task 2

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print("sum",num1+num2)
print("difference",num1-num2)
print("product",num1*num2)
print("quotient",num1/num2)

# task 3
price=float(input("enter food price:"))
quantity=int(input("enter fodd quantity:"))
total_bill=price*quantity
print("your total_bill is =" +format(total_bill, ".2f"))

# task 4 instagram followers

followers=int(input("enter your instagram followers count:"))
print("\n\tyou have",format(followers,"d"),"followers")

# task 5 basic calculator

number1=float(input("enter first number:"))
number2=float(input("enter second number:"))
operator=input("enter operator (+,_,/,*)")
if operator=="+":
    Result=number1+number2
    print("Result",Result)
elif operator=="_":
    Result=number1-number2
    print("Result",Result)
elif operator=="*":
    Result=number1*number2
    print("Result",Result)
elif operator=="/":
    Result=number1/number2
    print("Result",Result)
else:
    print("enter valid operator")



