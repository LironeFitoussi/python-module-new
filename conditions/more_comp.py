# comapring lists
friends = ["Bob", "Rolf", "Anne"]
abroad = ["Bob", "Anne", "Rolf"]

print(set(friends) == set(abroad)) # True
print(friends == abroad) #False

# "==" or "is"
print(friends[1] is abroad[2])

s = {(5+5+5+5)}
print(s) # Output: {20}