class User:

    bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
jack = User("Jack Smith", "jack@gmail.com")

#First user making 3 deposits and 1 withdrawal
guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(200)
guido.make_withdrawal(50)
guido.display_user_balance()    #balance 450

#Second user making 2 deposits and 2 withdrawal
monty.make_deposit(50)
monty.make_deposit(100)
monty.make_withdrawal(25)
monty.make_withdrawal(75)
monty.display_user_balance()    #balance 50

#Third user making 1 deposits and 3 withdrawal
jack.make_deposit(500)
jack.make_withdrawal(150)
jack.make_withdrawal(150)
jack.make_withdrawal(150)
jack.display_user_balance()    #balance 50