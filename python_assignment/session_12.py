# # task 1 Discount price
def get_discount_price(price,discount_percent):
    discount_price=price*discount_percent/100
    final_price=price-discount_price
    return final_price
print(get_discount_price(500,10))

# task 2 instagram style followers
def format_followers_count(followers):
    if followers >= 1000000:
        return str(followers/1000000)+"M"
    elif followers>=1000:
        return str(followers/1000)+"K"
    else:
        return str(followers)
print(format_followers_count(1500))
print(format_followers_count(1200000))
print(format_followers_count(500))


# task 3
song_duration=[3,4,5,6]
result=list(map(lambda x:x*60,song_duration))
print(result)

# task 4
product=["Mobile","Mouse","Laptop","Monitor","Keyboard"]
result=list(filter(lambda x:x.startswith("M"),product))
print(result)

# task 5



