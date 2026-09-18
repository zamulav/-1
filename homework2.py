class BankAccount:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def deposit(self, s):
        self.b = self.b + s

    def withdraw(self, x):
        if x <= self.b:
            self.b = self.b - x
        else:
            print("Недостатньо коштів!")


acc = BankAccount("123", 500)
acc.deposit(200)
acc.withdraw(100)
print(acc.b)
