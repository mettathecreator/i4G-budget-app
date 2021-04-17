class Budget:
    
    """ 
    constructor takes the funds
    """
    # funds = 0
    def __init__(self, funds=0):
        self.funds = 0

    """
    method for depositing funds (funds) to any category object
    """

    def deposit(self, funds):
        self.funds += funds
        print("succesfully deposited %d" % self.funds)
    
    def withdraw(self, funds):
        if (self.funds < funds ):
            print("Insufficient funds")
        else:
            self.funds -= funds
            print("Withdraw Complete amount: %d" % self.funds)

    def balance(self):
        print("Your current balance is %d" % self.funds)

    def transfer(self, funds):
        self.funds += funds
        print("succesfully transferred %d" % self.funds)






ps = Budget()
ps.deposit(23)

# ps.withdraw(22)

# print (ps.funds)

# fd = Budget()
# print (fd.funds)
    
    

    


        