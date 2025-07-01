# bank account app using OOP:

class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to Account {self.account_number} ({self.account_holder_name}). New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from Account {self.account_number} ({self.account_holder_name}). New Balance: {self.balance}")
        else:
            print("Amount Withdraw Unsuccessful. Ensaficient balance.")

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Balance: {self.balance}")

account = None

while True:
    print("\nBank Account Application:")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choose = input("Enter Your Choice (1-5): ")

    if choose == '1':
        account_number = input("Enter Account Number: ")
        account_holder_name = input("Enter Account Holder Name: ")
        try:
            initial_balance = float(input("Enter Initial Balance: "))
        except ValueError:
            print("Invalid balance amount.")
            continue
        account = BankAccount(account_number, account_holder_name, initial_balance)
        print("Account Created Successfully!")

    elif choose == '2':
        if account:
            try:
                amount = float(input("Enter Amount to Deposit: "))
            except ValueError:
                print("Invalid deposit amount.")
                continue
            account.deposit(amount)
        else:
            print("No account found. Please create an account first.")

    elif choose == '3':
        if account:
            try:
                amount = float(input("Enter Amount to Withdraw: "))
            except ValueError:
                print("Invalid withdrawal amount.")
                continue
            account.withdraw(amount)
        else:
            print("No account found. Please create an account first.")

    elif choose == '4':
        if account:
            account.display_account_details()
        else:
            print("No account found. Please create an account first.")

    elif choose == '5':
        print("Exiting the Bank Account Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")