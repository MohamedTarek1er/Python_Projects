from Bank import Bank
bank = Bank()
while True:
    action = input("Enter 'register' to register, 'login' to login, 'exit' to exit: ")
    if action == 'register':
        bank.register_user()
    elif action == 'login':
        username = bank.login_user()
        if isinstance(username,str):
            while True:
                user_action = input("Enter 'balance' to check balance, 'deposit' to deposit, 'withdraw' to withdraw, 'logout' to logout: ")
                if user_action == 'balance':
                    bank.check_balance(username)
                elif user_action == 'deposit':
                    bank.deposit(username)
                elif user_action == 'withdraw':
                    bank.withdraw(username)
                elif user_action == 'logout':
                    break
                else:
                    print("Invalid action.")
    elif action == 'exit':
        break
    else:
        print("Invalid action. Please try again.")