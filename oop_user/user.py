
class User:
    bank_name = "First National Dojo"
    def __init__(self) -> None:
        self.name = "Sam" 
        self.email = "samgreen@dojo.com"
        self.account_balance = 0
        amount = 0
    
    def deposit(self, amount):
        self.account_balance += amount
    
    def withdrawl(self, amount):
        self.account_balance -= amount
    
    def balance(self):
        print(f"{self.name} --- {self.account_balance}")
    
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

Sam.deposit(100)
Sam.deposit(40)
Sam.deposit(20)
Sam.withdrawl(80)
Sam.balance()

Butters.deposit(200)
Butters.deposit(100)
Butters.withdrawl(50)
Butters.withdrawl(50)
Butters.balance()

Monty.deposit(300)
Monty.withdrawl(100)
Monty.withdrawl(100)
Monty.withdrawl(20)
Monty.balance()

Monty.transfer(50, Sam)