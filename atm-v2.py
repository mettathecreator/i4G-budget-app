import random

db_users = {
    'testUser': 'testPass'
}

def login():
    uname = input("What is your username? \n")
    password = input("What is your password? \n")

    if (uname in db_users and password == db_users[uname]):
        
        print("---****---- Welcome back %s ---***---" % uname)
        print("Hello, %s. Your account number is %d" %(uname, acc_num))

        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Receipt')
        print('3. Complaint')
        print('4. Change Password')

        selectedOption = int(input('Please select an option: \n'))

        if (selectedOption == 1):
            withdrawAmount = int(input('How much would you like to withdraw? \n'))
            print('Take your cash')
        elif(selectedOption == 2):
            depositAmount = int(input('How much would you like to deposit? \n'))
            print('Current balance is %s' % depositAmount)
        elif(selectedOption == 3):
            withdrawAmount = input('What issue will you like to report? \n')
            print('Thank you for contacting us')
        elif(selectedOption == 4):
            changePass(uname, password)
        else:
            print('Invalid option selected, please try again')

        return True
    else:
        print("Incorrect username or password. Try again")
        return False

def changePass(uname, password):
    new_pass = input("What is your new password? \n")
    db_users[uname] = new_pass
    print('Password Changed Successfully')
    exit()



def register():
    uname = input("Enter a unique username \n")
    password = input("Enter a password you'll remember \n")

    db_users[uname] = password
    
    #generate acc number
    acc_num = random.randint(10**5, 10**6 - 1)
    
    print("Signed Up as %s" %uname)
    print("Your account number is %d" % acc_num)
    action = int(input('To login press 1. To exit Press 2. \n'))

    while True:
        if(action == 1):
            login()
        elif(action == 2):
            print("Goodbye %s. Come back soon" %uname)
            exit()
        else:
            print("incorrect input. Try again")
            action = int(input('Signed Up. To login press 1 \n . To exit Press 2'))


print("Welcome, Zuri ATM v2 Choose an action please?")
print("1. Login")
print("2. Register")

option = int(input("Select an option \n"))

if(option == 1):
    login()
            
elif(option == 2):
    register()