class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

account1 = BankAccount(.01,5000)
account2 = BankAccount(10, 350)
account1.deposit(3).deposit(15).deposit(42).withdraw(5).yield_interest().display_account_info()
account2.deposit(1000).deposit(500).withdraw(400).withdraw(10).withdraw(50).withdraw(32).yield_interest().display_account_info()
