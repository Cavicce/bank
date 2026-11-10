class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        self.__transactions = []
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Deposit Successful of: {amount}")
        else:
            print("Deposit amount must be a positive number")
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be a positive number")
        elif amount > self.__balance:
            print("Insufficient Funds")
        else:
            self.__balance -= amount
            self.__transactions.append(f"Withdrawal Successful of: {amount}")
    def get_balance(self):
        return self.__balance
    def show_transactions(self):
        if not self.__transactions:
            print("No transactions yet")
        else:
            print("Transaction History")
            for transaction in self.__transactions:
                print(transaction)
    def get_transactions(self):
        return self.__transactions.copy()