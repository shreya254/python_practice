class accounts :
    def __init__(self,balance,accountno):
        self.balance = balance
        self.accountno = accountno
    def debit(self,amount):
        self.balance = self.balance-amount
        print("your remaining balance is",self.balance)
    def credit(self,credit):
        self.balance = self.balance+credit
        print("your remaining balance is",self.balance)
    def total(self):
        print("your balance is ", self.balance)

acc = accounts(10000,12345)
acc.debit(2000)
acc.credit(1000)
acc.total()