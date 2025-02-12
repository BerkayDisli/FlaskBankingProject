class User:
    def __init__(self, name):
        self.balance = 0
        self.name = name

    def show_details(self):
        return f"Personal Details\nName: {self.name}\nAccount Balance: ${self.balance}"


class Bank(User):
    def __init__(self, name):
        super().__init__(name)
        self.amount = None
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            return "Amount to deposit must be positive."
        self.amount = int(amount)
        self.balance += self.amount
        return 'account balance is $' + str(self.balance)

    def withdraw(self, amount):
        self.amount = int(amount)
        if self.amount > self.balance:
            return f"Insufficient funds. Your balance is ${self.balance}"
        else:
            self.balance -= self.amount
            return 'account balance is $' + str(self.balance)

    def view_balance(self):
        return self.show_details()

user1 = Bank('John')

print(user1.show_details())
print(user1.deposit(100))
print(user1.view_balance())
print(user1.withdraw(50))
print(user1.view_balance())
print(user1.withdraw(150))
print(user1.view_balance())