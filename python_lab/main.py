accounts = [
    {"account_id": 101, "name": "Daniel", "pin": 5678, "balance": 900},
    {"account_id": 100, "name": "Liron", "pin": 1234, "balance": 500},
]

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "123456"

def find_account(account_id): # 100
    for account in accounts:
        if account_id == account["account_id"]:
            return account
    return None

def verify_pin(account, user_pin_input):
    if account["pin"] == user_pin_input:
        return is_
        

def deposit():
    account_id = int(input("Enter Account Number"))
    user_pin_input = int(input("pass here your PIN"))
    
    account = find_account(account_id)
    

def withdraw():
    # withdraw logic
    pass

def create_account():
    pass

def show_all_accounts():
    pass

def admin_login():
    username = input("Admin username: ")
    password = input("Admin password: ")
    
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True
    
    print("Access Denied")
    return False
    
    
# is_admin_in = admin_login()

# print(f"Admin is in? : {is_admin_in}")