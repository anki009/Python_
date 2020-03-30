"""
To make class of Bank account which will have to methods deposit and withdraw.
These two methods will depsit and withdraw and some amount from bank account
and will make sure account is not overwithdrawn.
"""
class BankAccount():
    owner = " "
    def __init__(self, owner):
        self.balance = 0
        self.owner = owner
    def __deposit__(self):
        amount = float(input("Enter  amount to deposit : "))
        self.balance += amount
        print("Deposited amount is : ", amount)
    def __withdraw__(self):
        amount = float(input("Enter  amount to be withdraw : "))
        if self.balance >= amount:
            self.balance -= amount
            print("amont withdrawn is  : ", amount)
            print("Account balance is  : ", self.balance)
        else:
            print('Account can\'t be withdrawn due to low balance')
B = BankAccount("ankita")
B.__deposit__()
B.__withdraw__()
B.__withdraw__()
