# Task 1
# import re
# email=input("Enter your email : ")
# if re.match(r"^[a-z][a-zA-Z0-9._%+-]*@gmail\.com$",email):
#     print("valid Email")
# else:
#     print("invalid Email")

# Task 2
# import re
# text=input("Enter text containing a mobile number:")
# pattern=r"\d{10}"
# result=re.search(pattern,text)
# if result:
#     print("Mobile number :",result.group())
# else:
#     print("Mobile number not found")


# Task 3
# import re
# def extract_hashtags(text):
#     pattern=r"#[A-Za-z0-9_]+"
#     return re.findall(pattern,text)
# caption=input("Enter your caption: ")
# hashtags=extract_hashtags(caption)
# print("Hashtags:",hashtags)


# Task 4
# import re
# orders=[
#     "ORD1234",
#     "ORD5678",
#     "ORD9999",
#     "ORD0001"
# ]
# pattern=r".*[02468]$"
# for order in orders:
#     if re.match(pattern,order):
#         print(order)

# Task 5
import re
def is_valid_pnr(pnr):
    pattern=r"^[0-9]{10}$"
    return bool(re.match(pattern,pnr))
pnr=input("Enter your 10-digit PNR:")
if is_valid_pnr(pnr):
    print("PNR is valid")
else:
    print("PNR is not valid")