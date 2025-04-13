# Create Account class with 2 attributs - balance & account no.
# Create methods for debit, credit & printing the balance
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    #debit
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount, "was debited")
        print("Total balance: ",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print(f"Rs. {amount} was credited")
        print("Total balance: ",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1=Account(20000,984655477644)
print(acc1.balance)
print(acc1.account_no)
acc1.credit(200)
acc1.debit(300)
