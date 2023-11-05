class BankAccount:
    # class parameter 
    accounts = [] 
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

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
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.name}")
        print(f"{self.email}")
        self.account.display_account_info()
        return self

# account1 = BankAccount(.01,5000)
# account2 = BankAccount(10, 350)
# account1.deposit(3).deposit(15).deposit(42).withdraw(5).yield_interest().display_account_info()
# account2.deposit(1000).deposit(500).withdraw(400).withdraw(10).withdraw(50).withdraw(32).yield_interest().display_account_info()

# BankAccount.print_all_accounts()

user1 = User("Susie Latham", "susiel@codingdojo.com")
user1.make_deposit(10000000).make_withdrawal(5).display_user_balance()

user2 = User("Derek Fin", "derekf@codingdojo.com")
user2.make_deposit(43059).make_deposit(44800).make_withdrawal(480).make_withdrawal(8258).display_user_balance()