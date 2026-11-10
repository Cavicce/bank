from bank_account import BankAccount 
balance = BankAccount(0)
while True:
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")
    try:
        choice = int(input(f"Welcome, What do you want to do? "))
    except ValueError:
        print("Please Enter a valid whole number")
        continue
    if choice == 1:
        print(balance.get_balance())
    elif choice == 2:
        try:
            deposit_amt = int(input("Enter Amount to Deposit: "))
        except ValueError:
            print("Please Enter a valid number")
            continue

        balance.deposit(deposit_amt)
    elif choice == 3:
        try:
            withdrawal_amt = int(input("Enter Amount to withdraw: "))
        except ValueError:
            print("Please Enter a valid number")
            continue
        balance.withdraw(withdrawal_amt)
    elif choice == 4:
        balance.show_transactions()
    elif choice == 5:
        print("Good Bye")
        break
    else:
        print("Enter a valid choice")