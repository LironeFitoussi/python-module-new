accounts = [{
    "account_id": 1001,
    "username": "Yuval",
    "balance": 55000,
    "pin": 3571
},
{
    "account_id": 1002,
    "username": "Mike",
    "balance": 100000,
    "pin": 1234
}]

def auth():
    id = int(input("Enter your account id"))
    pin = int(input("enter your PIN: "))
    
    # Find matching account from id
    for user in accounts:
        if id == user["account_id"] and user["pin"] == pin:
            print(f"Welcome {user["username"]}")
            return user # exists => positive => True => 1
        else:
            return None # non-exisits => negative => False => 0

def withdraw():
    user_account = auth()
    if user_account:
        amount = float(input("Please type the amount you would like to withdraw: "))
        if amount > user_account["balance"]:
            print("You are poor")
        else:
            user_account["balance"] -= amount
            balance(user_account["balance"])
    else:
        print("Wrong PIN, goodbye")
        exit()

def deposite():
    user_account = auth()
    if user_account:
        amount = float(input("Please type the amount you would like to deposite: "))
        if amount < 0:
            print("You cannot tpye negative numbers")
            exit()
        else:
            user_account["balance"] += amount
            balance(user_account["balance"])
    else:
        print("Wrong PIN, goodbye")
        exit()

def balance(user_balance):
    print(f"Your Balance now is {user_balance}")


while True:
    print("======= Welcome to Python ATM =======")    
    user_choise = int(input("""
        Choose one: 
        1. withdraw Money
        2. Deposite Money
        3. Balance
        0. to exit
    """))
    
    # print(f"User Choosed {user_choise}")
    
    match user_choise:
        case 1:
            withdraw()
        case 2:
            deposite()
        case 3:
            balance()
        case 0:
            print("Ok, Exiting...")
            exit()
    