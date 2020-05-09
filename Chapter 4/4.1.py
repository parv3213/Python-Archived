class BankAccount:
    """
    Class to simulate Banck account
    Attributes:
        balance : to hold balance amount in the account
    """
    def __init__(self):
        self.balance=0
        
    def deposite(self,amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self,amount):
        if amount>self.balance:
            return "Insufficient funds"
        else :
            self.balance= self.balance-amount
            return self.balance

#Main
ac2001=BankAccount()
ac2001.deposite(11000)
print "Now the balance in the account is:",ac2001.balance
ac2001.withdraw(3000)
print "Now the balance in the account is:",ac2001.balance
        
