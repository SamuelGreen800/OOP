class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance, name):
        self.int_rate = int_rate
        self.balance = balance
        self.name = name
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



#---------------------------------------------------------------

class User:
    bank_name = "First National Dojo"
    
    def __init__(self, name, email, amount):
        self.name = name
        self.email = email
        self.account ={ 
            "checking" : BankAccount(.02, 0, name),
            "saving" : BankAccount(.01, 1000, name)}
        amount = amount
    
    def deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def withdrawl(self, amount):
        self.account.withdrawl(amount)
        return self

    def balance(self):
        self.account.show_balance
        return self

    def transfer(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.balance()
        user.balance()

Sam = User("Sam", "SamuelGreen800@tutanota.com", 0)


Sam.account["saving"].deposit(100)
Sam.account["saving"].withdrawl(50)
Sam.account["saving"].show_balance()

#--------------------------------------------------------------------------------------------------------------------------------------------------------
