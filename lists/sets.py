s = {"write","execute","read", "read"}
l = ["write","execute","read", "read"]
# print(type(l[1]))

# Set are more restricted then tupples
#! This will raise an error because lists are mutable and cannot be added to a set
# set_of_lists = {{"write","execute"}, {"read", "read"}} 

set_of_tuples = {(1, 2), (3, 4)}
# print(set_of_tuples)
# print("doron" in s)

developers = {"Alice", "Bob", "Charlie"}
admins = {"Alice", "David"}

# print("Is alice in developres team?", "Alice" in developers)
# print("Is alice in admins team?", "Alice" in admins)

# ===============================

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

# print(z)

# ==============================

all_members = developers.union(admins)
# print(all_members)

# ==============================
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

# print(z)

# ==============================
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y) 
w = y.difference(x) 

print(z)
print(w)

# ==============================