class Budget:
   
    def __init__(self, category, balance = 0):
        self.category = category
        self.balance = balance

    """ 
    user actions based on category
    """
    def action(self):
        print("-*- Available actions -*-")
        print('1. Deposit')
        print('2. Withdrawal')
        print('3. Check Balance ')

        #get user selection
        action_option = int(input('## What would you like to do? ## \n'))


        while True:
            if action_option == 1:
                self.deposit()
                break
            elif action_option == 2:
                self.withdraw()
                break
            elif action_option == 3:
                self.check_balance()
                break
            elif action_option == 4:
                self.transfer()
                break
            else:
                print('Selected Option is Invalid. Please try again')
                action_option = int(input('## What would you like to do? ## \n'))
                continue
    
    def deposit(self):
        funds = int(input('## How much would you like to deposit? ## \n'))
        self.balance += funds
        print("succesfully deposited N%d to %s" % (self.balance, self.category))

    def check_balance(self):
        print("Your current balance is N%d" % self.balance)
        return self.balance
        

    def withdraw(self):
        amount = int(input('amount to withdraw: \n'))
        if (self.balance < amount ):
            print("Insufficient funds. You cannot withdraw more than N%d" % self.balance)
        else:
            self.balance -= amount
            print("Withdraw Complete amount: N%d" % self.balance)


food = Budget('Food')
clothing = Budget('Clothing')
entertainment = Budget('Entertainment')

print("### Welcome to i4G Budget App ###")
print("--- You can budget for the following ---")
print("1. Food \n2. Clothing \n3. Entertainment")

category = int(input('Select a Category :\n'))
while True:
    if category == 1:
        print("%s Selected" % food.category)
        food.action()
        break
    elif category == 2:
        print("%s Selected" % clothing.category)
        clothing.action()
        break
    elif category == 3:
        print("%s Selected" % entertainment.category)
        entertainment.action()
        break
    else:
        print("Invalid Option Selected, please try again")
        category = int(input('Select a Category :\n'))
        


