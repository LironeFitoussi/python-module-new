# if
# elif
# else

day_of_week = input("What day of week is it today? ").lower()
# print(day_of_week == "monday")

if day_of_week == "monday":
    print("Have a great start of week!")
elif day_of_week == "tuesday":
    print("It's a productive Tuesday")
else: 
    print("Full speed ahead")

print("This always runs.")