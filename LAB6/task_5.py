class BankAccount:
    def __init__(self, name, balance=0):
        
        self.name = name
        self.balance = balance
    def deposit(self, amount):
       
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
       
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        
        print(f"Current balance: {self.balance}")
        return self.balance

# Example usage:
account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.check_balance()