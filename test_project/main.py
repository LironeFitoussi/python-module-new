accounts = []

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"


def admin_login():
    username = input("Admin username: ")
    password = input("Admin password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True

    print("Access denied")
    return False


def find_account(account_id):
    for account in accounts:
        if account["account_id"] == account_id:
            return account
    return None


def verify_pin(account, pin):
    return account["pin"] == pin


def create_account():
    if not admin_login():
        return

    name = input("Enter account holder name: ")
    pin = input("Set 4-digit PIN: ")

    account = {
        "account_id": len(accounts) + 100,
        "name": name,
        "pin": pin,
        "balance": 0
    }

    accounts.append(account)
    print("Account created successfully")
    print("New account number:", account["account_id"])


def deposit():
    account_id = int(input("Enter account number: "))
    pin = input("Enter PIN: ")
    amount = float(input("Enter amount to deposit: "))

    account = find_account(account_id)

    if not account:
        print("Account not found")
        return

    if not verify_pin(account, pin):
        print("Wrong PIN")
        return

    if amount <= 0:
        print("Invalid amount")
        return

    account["balance"] += amount
    print("Deposit successful")


def withdraw():
    account_id = int(input("Enter account number: "))
    pin = input("Enter PIN: ")
    amount = float(input("Enter amount to withdraw: "))

    account = find_account(account_id)

    if not account:
        print("Account not found")
        return

    if not verify_pin(account, pin):
        print("Wrong PIN")
        return

    if amount <= 0:
        print("Invalid amount")
        return

    if account["balance"] < amount:
        print("Insufficient funds")
        return

    account["balance"] -= amount
    print("Withdraw successful")


def show_account():
    account_id = int(input("Enter account number: "))
    pin = input("Enter PIN: ")

    account = find_account(account_id)

    if not account:
        print("Account not found")
        return

    if not verify_pin(account, pin):
        print("Wrong PIN")
        return

    print("\n--- ACCOUNT DETAILS ---")
    print("Account Number:", account["account_id"])
    print("Name:", account["name"])
    print("Balance:", account["balance"])


def show_all_accounts():
    if not admin_login():
        return

    if not accounts:
        print("No accounts found")
        return

    print("\n--- ALL ACCOUNTS ---")
    for account in accounts:
        print(account)


while True:
    print("\n--- BANK ATM ---")
    print("1. Create Account (Admin)")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Account")
    print("5. Show All Accounts (Admin)")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        show_account()

    elif choice == "5":
        show_all_accounts()

    elif choice == "6":
        print("Goodbye")
        break

    else:
        print("Invalid choice")