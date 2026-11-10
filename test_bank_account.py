import unittest
from bank_account import BankAccount

class TestBank(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount(1000)
        account.deposit(500)
        
        self.assertEqual(account.get_balance(),1500)
    def test_withdraw(self):
        account = BankAccount(1000)
        account.withdraw(300)
        
        self.assertEqual(account.get_balance(),700)
    def test_invalid_deposit(self):
        account = BankAccount(1000)
        account.deposit(-200)
        
        self.assertEqual(account.get_balance(),1000)
    def test_insufficient_funds(self):
        account = BankAccount(1000)
        account.withdraw(1500)
        
        self.assertEqual(account.get_balance(),1000)
    def test_invalid_withdrawal(self):
        account = BankAccount(1000)
        account.withdraw(-100)
        
        self.assertEqual(account.get_balance(),1000)
    def test_transaction_history(self):
        account = BankAccount(1000)
        account.deposit(500)
        account.withdraw(200)
        
        expected_transactions = [
            "Deposit Successful of: 500",
            "Withdrawal Successful of: 200"
        ]
        
        self.assertEqual(account.get_transactions(), expected_transactions)
    def test_no_transactions(self):
        account = BankAccount(1000)
        account.withdraw(1500)
        
        self.assertEqual(account.get_transactions(), [])
if __name__ == "__main__":
    unittest.main()