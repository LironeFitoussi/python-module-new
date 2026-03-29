# ====================================
# My Prpfile App - Project
# ====================================

name = input("enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

hobbies = input('Type your 3 hobbies, use "," after every hobbie').split(",") #? users should type "gaming,footbal,food" => ["gaming", "football", "food"]

popular_hobbies = ["music", "sports", "gaming", "reading"]

print(f"Hello {name},\nage: {age} from {city}\nyour hobbies: {", ".join(hobbies)}")
# print(hobbies)