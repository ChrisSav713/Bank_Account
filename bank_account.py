class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f'''Interest Rate: {self.int_rate} Balance: {self.balance}''')
    def yield_interest(self):
        self.balance *= 1 + (self.int_rate / 100)
        return self
    @classmethod
    def print_all(cls):
        for account in cls.all_accounts:
            account.display_account_info()

account = []
account.append(BankAccount(1.2, 500))
account.append(BankAccount(1.2, 1200))

account[0].display_account_info()
account[0].deposit(100).deposit(80).deposit(400).yield_interest()
account[0].display_account_info()

account[1].deposit(400).deposit(1200).withdraw(80).withdraw(220).withdraw(100).withdraw(180).yield_interest().display_account_info()

print("\n===Print All Accounts===\n")
BankAccount.print_all()

# print(BankAccount.all_accounts[0].int_rate)
# BankAccount.all_accounts[1].deposit(400).deposit(1200).withdraw(80).withdraw(220).withdraw(100).withdraw(180).yield_interest().display_account_info()