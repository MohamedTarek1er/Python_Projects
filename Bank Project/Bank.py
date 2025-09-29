class Bank:
    def __init__(self):
        self.user_accounts = {}
        self.user_balances = {}
# [{"Mohamed":123},{"Mohamed",0}]
    def register_user(self):
        username = input("Please enter your username: ")
        if username in self.user_accounts.keys():
            print("Username already exists. Please choose a different username.")
        else:
            # {"Mohamed":123},{"Mohamed":0}
            password = input("Please enter your password: ")
            self.user_accounts[username] = password
            self.user_balances[username] = 0
            print(f"Registration successful {self.user_accounts,self.user_balances}")

    def login_user(self):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if username in self.user_accounts.keys() and self.user_accounts[username] == password:
            print("Login successful.")
            return username
        else:
            print("Invalid username or password.")
            return None
# {"Mohamed":0}
    def check_balance(self, username):            #                                       {"Mohamed":0}
         print(f"Your current balance is: {self.user_balances[username]}")

    def deposit(self, username):
        amount = float(input("Enter the amount to deposit: "))
        while amount<0:
            print("Invild data")
            amount = float(input("Enter the amount to deposit: "))
        self.user_balances[username] += amount
        print(f"Deposit of {amount} successful.")
            
    def withdraw(self, username):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > 0 and amount <= self.user_balances[username]:
            self.user_balances[username] -= amount
            print(f"Withdrawal of {amount} successful.")
        else:
            print("Invalid amount or insufficient balance.")
