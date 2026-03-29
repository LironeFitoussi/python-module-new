# number_int = 6 # Integer
# number_float = 6.0 # Float
# string = "Baba" # String
# boolers = False # Boolean (0)
# boolers = True # Boolean (1)


# # List
# book1 = "Harry Potter - and the Philosopher's Stone"
# book2 = "Harry Potter - and the Chamber of Secrets"
# book3 = "Harry Potter - and the Prisoner of Azkaban"
# book4 = "Harry Potter - and the Goblet of Fire"
# book5 = "Harry Potter - and the Order of the Phoenix"
# book6 = "Harry Potter - and the Half-Blood Prince"
# book7 = "Harry Potter - and the Deathly Hallows"

# harry_potter_books = [
#     "Harry Potter - and the Philosopher's Stone", # idx 0
#     "Harry Potter - and the Chamber of Secrets", # idx 1
#     "Harry Potter - and the Prisoner of Azkaban", # idx 2
#     "Harry Potter - and the Goblet of Fire", # idx 3 
#     "Harry Potter - and the Order of the Phoenix",# idx 4
#     "Harry Potter - and the Half-Blood Prince", # idx 5
#     "Harry Potter - and the Deathly Hallows" # idx 6
# ]

# # print(harry_potter_books)
# # print(harry_potter_books[3])
# multi_data_list = [
#     "Baba",
#     1.2,
#     54,
#     True,
#     ["Lirone", "Johnny"]
# ]

# # print(type(multi_data_list[0]))
# # print(type(multi_data_list[1]))
# # print(type(multi_data_list[2]))
# # print(type(multi_data_list[4])) #! <class list>


# # List 
# my_list = ["Bob", "Rolf", "Anne"]
# # print(my_list[1])
# # print(my_list)

# # Tuple
# my_tuple = ("Bob", "Rolf", "Anne")
# # print(my_tuple[1])
# # print(my_tuple)

# # Set
# my_set = {"Bob", "Rolf", "Anne"}
# # print(my_set[1])
# # print(my_set)

# name = "Mickey"
# # name[0] = "S" #! Expect to get Sickey but wont work cuase strings are immutable


# my_list = ["Bob", "Rolf", "Anne"]
# print(my_list)
# my_list[0] = "Smith"
# print(my_list)

# my_servers = [
#     "us-east-1",
#     "us-west-1",
#     "eu-west-1",
#     "il-west-1"
# ]


# my_tuple = ("Bob", "Rolf", "Anne")
# print(my_tuple)
# # my_tuple[0] = "Smith" #! This will raise an error because tuples are immutable

# # Adding to a list
# my_list.append("John")
# print(my_list)

# # my_tuple.apped("John") #! This will raise an error because tuples are immutable

# # Removing from a list
# my_list.remove("Rolf")
# print(my_list)

# Adding a list to a list
# my_list.append(["John", "Smith"])
# print(my_list)


# # Trying to mutate a list inside a tuple
# # my_tuple = ("Bob", "Rolf", "Anne", ["John", "Smith"])
# # print(my_tuple)


# my_tuple[3].append("Doe")
# print(my_tuple)

my_list = ["Bob", "Rolf", "Anne", "Rolf"]
# print(my_list)

# Removing from a list
# my_list.remove("Rolf")
# print(my_list)
# my_list.remove("Rolf")
# print(my_list)

# Using negative indexing in a list
a = [10, 20, 30, 40, 50]

# Accessing elements from the end
print(a[-1])  # last element
print(a[-2])  # second last element
print(a[-5])  # first element