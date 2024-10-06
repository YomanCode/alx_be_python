import sys

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: {self.account_balance}")

if __name__ == "__main__":
    initial_balance = float(sys.argv[1]) if len(sys.argv) > 1 else 0
    account = BankAccount(initial_balance)

    account.deposit(100)
    account.withdraw(50)
    account.display_balance()