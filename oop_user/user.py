
class User:
    bank_name = "First National Dojo"
    def __init__(self) -> None:
        self.name = "Sam" 
        self.email = "samgreen@dojo.com"
        self.account_balance = 0
        amount = 0
    
    def deposit(self, amount):
        self.account_balance += amount
        return self
    
    def withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def balance(self):
        print(f"{self.name} --- {self.account_balance}")
        return self
    def transfer(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.balance()
        user.balance()
        

Sam = User()
Sam.name = "Sam"
Butters = User()
Butters.name = "Butters"
Monty = User()
Monty.name = "Monty"

Sam.deposit(100).deposit(40).deposit(20).withdrawl(80).balance()


Butters.deposit(200).deposit(100).withdrawl(50).withdrawl(50).balance()

Monty.deposit(300).withdrawl(100).withdrawl(100).withdrawl(20).balance()

Monty.transfer(50, Sam)