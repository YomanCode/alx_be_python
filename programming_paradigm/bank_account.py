import sys

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
            return True
        else:
            print(f"Insufficient funds to withdraw ${amount}.")
            return False

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <initial_balance> <operation> <amount (if needed)>")
        sys.exit(1)

    initial_balance = float(sys.argv[1])
    account = BankAccount(initial_balance)

    operation = sys.argv[2].lower()

    if operation == "deposit":
        if len(sys.argv) < 4:
            print("Usage: python script_name.py <initial_balance> deposit <amount>")
            sys.exit(1)
        amount = float(sys.argv[3])
        account.deposit(amount)
    
    elif operation == "withdraw":
        if len(sys.argv) < 4:
            print("Usage: python script_name.py <initial_balance> withdraw <amount>")
            sys.exit(1)
        amount = float(sys.argv[3])
        account.withdraw(amount)

    elif operation == "display":
        account.display_balance()

    else:
        print(f"Unknown operation '{operation}'. Use deposit, withdraw, or display.")