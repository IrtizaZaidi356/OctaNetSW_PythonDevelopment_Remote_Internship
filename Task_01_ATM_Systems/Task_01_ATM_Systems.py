"""
Python Development | Remote Internship | OctaNetSW

Task 01 | ATM INTERFACE 

Perform Task No# 01

The ATMs in our cities are built on Python, as we have all seen them. It is 
a console-based application with five different classes. In order to use the 
system, the user must enter his or her user ID and pin when it starts. 
Once the details are entered successfully, ATM functionality is unlocked. 
As a result of the project, the following operations can be performed:

Transactions History
Withdraw
Deposit
Transfer
Quit

"""

class ATM:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transactions = []
    
    def display_menu(self):
        print("ATM Menu Options:")
        print("1) Transaction History")
        print("2) WithDraw")
        print("3) Deposit")
        print("4) Transfer")
        print("5) Quit")
    
    def show_transactions_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append((f"${amount} has been withdrawn from your account."))
            print(f"Withdraw ${amount}")
        else:
            print("Invalid amount or insufficient balance")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append((f"${amount} has been deposited into your account."))
            print(f"Deposited ${amount}")
        else:
            print("Invalid amount.")
    
    def transfer(self, amount, target_account):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Transferred ${amount} to {target_account}")
            print(f"Transferred ${amount} to {target_account}")
        else:
            print("Invalid amount or insufficient balance.")
    
    def run(self):
        print("\nWelcome to the ATM system!")
        entered_pin = input("Please Enter Your PIN: ")
        
        if entered_pin == self.pin:
            while True:
                self.display_menu()
                choice = input("Enter Your Choices (1,2,3,4,5): ")
                
                if choice == "1":
                    self.show_transactions_history()
                elif choice == "2":
                    amount = float(input("Enter the Amount to WithDraw: "))
                    self.withdraw(amount)
                elif choice == "3":
                    amount = float(input("Enter the Amount to Deposit: "))
                    self.deposit(amount)
                elif choice == "4":
                    amount = float(input("Enter the Amount to Transfer: "))
                    target_account = input("Enter the Target Account: ")
                    self.transfer(amount, target_account)
                elif choice == "5":
                    print("Thank You for using the ATM. Have a Nice Day!!!")
                    break
                else:
                    print("Invalid Option Selected. Please Try Again.")
        else:
            print("Incorrect PIN. Access Denied.")
            
user_id = input("\nEnter Your User ID: ")
pin = input("\nEnter Your PIN: ")
atm = ATM(user_id, pin)
atm.run()
