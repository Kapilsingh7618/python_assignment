# Task 1
# text = input("enter a string :")
# frequency = {}
# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1
# print(frequency)

# Task 2
# sentence = input("enter a sentence :").lower()
# words = sentence.split()
# frequency = {}
# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1
#
# print(frequency)

# Task 3
# def word_frequency(text):
#     words = text.split()
#     frequency = {}
#     for word in words:
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1
#     return frequency
# text = "Virat scored 100,Rohit scored 80 and gill scored 50 in the IPL match"
# result = word_frequency(text)
# print(result)

# Task 4
# def word_frequency(text):
#     text = text.lower()
#     words = text.split()
#     frequency = {}
#     for word in words:
#         if word in stopwords:
#             continue
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1
#     return frequency
#
# text="Virat is the best player in the team and virat is a great batsman."
# stopwords = ["the","and","in","of","a","to","is"]
# result = word_frequency(text)
# print(result)

# Task 5
def char_count_dict(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

text=input("Enter a string: ")
char_count_dict(text)
result = char_count_dict(text)
print(result)

