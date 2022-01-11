class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.name = "name"
        BankAccount.accounts.append(self)

    def deposit(self, amount):
            self.balance += amount
            return self

    def withdrawl(self, amount):
            if (self.balance - amount) >= 0:
                self.balance -= amount
            else:     
                print("Insufficient Funds - $5 Fee")
                self.balance -= 5
            return self

    def show_balance(self):
            print(f"{self.name}, {self.balance}")


    def yield_interest(self):
            if self.balance > 0:
                self.balance += (self.balance * self.int_rate)
                return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.show_balance()


savings = BankAccount(.05, 1000)
checking = BankAccount(.02, 5000)
CD = BankAccount(.1, 2000)
MM = BankAccount(.4, 12000)

savings.deposit(20).deposit(20).deposit(20).withdrawl(100).yield_interest().show_balance()
checking.deposit(20).deposit(20).withdrawl(10).withdrawl(10).withdrawl(10).withdrawl(10).yield_interest().show_balance()

BankAccount.print_all_accounts()