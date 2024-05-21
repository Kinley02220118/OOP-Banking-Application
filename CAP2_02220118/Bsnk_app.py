'''Reference 
python banking system project. you can: 1. Open Account 2. Close Account 3. Withdraw Money
4. Deposit Money 5. Report for Management. (n.d.). Gist. 
https://gist.github.com/Edgars-Duka/feae5c1fe986a5cf69ccd39b96619332

Python OOP: Bank class for customer account management. (2023, November 25). W3resource. 
https://www.w3resource.com/python-exercises/oop/python-oop-exercise-11.php

Sharma, R. (2024, May 21). Python Banking Project [With Source Code] in 2024. upGrad blog. 
https://www.upgrad.com/blog/python-banking-project/
'''
import random  # Importing the random module to generate random account numbers and passwords
import os  # Importing the os module to check for the existence of the accounts file

# Base Account Class
class Account:
    def __init__(self, acc_no, passwd, acc_type, balance=0.0, savings=0.0, current=0.0):
        # Initialize the account with account number, password, account type, balance, savings, and current balances
        self._acc_no = acc_no  # Account number
        self.passwd = passwd  # Account password
        self._acc_type = acc_type  # Account type (e.g., Business, Personal)
        self.balance = balance  # Main balance of the account
        self.savings = savings  # Savings balance of the account
        self.current = current  # Current balance of the account

    @property
    def account_number(self):
        # Getter for account number
        return self._acc_no

    @account_number.setter
    def account_number(self, value):
        # Setter for account number
        self._acc_no = value

    @property
    def balance(self):
        # Getter for balance
        return self._balance

    @balance.setter
    def balance(self, value):
        # Setter for balance
        self._balance = value

    @property
    def account_type(self):
        # Getter for account type
        return self._acc_type

    @account_type.setter
    def account_type(self, value):
        # Setter for account type
        self._acc_type = value

    @property
    def savings(self):
        # Getter for savings
        return self._savings

    @savings.setter
    def savings(self, value):
        # Setter for savings
        self._savings = value

    @property
    def current(self):
        # Getter for current
        return self._current

    @current.setter
    def current(self, value):
        # Setter for current
        self._current = value

    def deposit(self, amount):
        # Deposit a specified amount into the account
        if amount > 0:  # Check if the deposit amount is positive
            self.balance += amount  # Add the amount to the balance
            print(f"Deposited Nu. {amount}. New balance: Nu. {self.balance}")  # Print the new balance
        else:
            print("Invalid deposit amount")  # Print an error message for invalid deposit amount

    def withdraw(self, amount):
        # Withdraw a specified amount from the account if sufficient funds are available
        if 0 < amount <= self.balance:  # Check if the withdrawal amount is positive and within the balance
            self.balance -= amount  # Subtract the amount from the balance
            print(f"Withdrew Nu. {amount}. New balance: Nu. {self.balance}")  # Print the new balance
        else:
            print("Insufficient funds or invalid amount")  # Print an error message for insufficient funds or invalid amount

    def display_balance(self):
        # Display the current balance of the account
        print(f"Account balance: Nu. {self.balance}")  # Print the account balance

# BusinessAccount Class inheriting from Account
class BusinessAccount(Account):
    # Initialize a BusinessAccount with the specified account number, passwd, and balance
    def __init__(self, acc_no, passwd, balance=0.0, savings=0.0, current=0.0):
        # Call the parent class (Account) constructor with account type "Business"
        super().__init__(acc_no, passwd, "Business", balance, savings, current)

# PersonalAccount Class inheriting from Account
class PersonalAccount(Account):
    # Initialize a PersonalAccount with the specified account number, passwd, and balance
    def __init__(self, acc_no, passwd, balance=0.0, savings=0.0, current=0.0):
        # Call the parent class (Account) constructor with account type "Personal"
        super().__init__(acc_no, passwd, "Personal", balance, savings, current)


class Bank:
    def __init__(self):
        # Initializes the Bank class and loads accounts from the file
        self.accounts = {}  # Dictionary to hold all accounts
        self.load_accounts()  # Load accounts from the file

    def load_accounts(self):
        # Loads account data from 'accounts.txt'
        if os.path.exists("accounts.txt"):  # Check if the accounts file exists
            with open("accounts.txt", "r") as file:  # Open the accounts file in read mode
                for line in file:  # Read each line in the file
                    # Split the line into account details
                    acc_no, passwd, acc_type, balance, savings, current = line.strip().split(",")
                    # Create account objects based on account type and store in the dictionary
                    if acc_type == "Business":
                        self.accounts[acc_no] = BusinessAccount(acc_no, passwd, float(balance), float(savings), float(current))
                    else:
                        self.accounts[acc_no] = PersonalAccount(acc_no, passwd, float(balance), float(savings), float(current))

    def save_accounts(self):
        # Saves account data to 'accounts.txt'
        with open("accounts.txt", "w") as file:  # Open the accounts file in write mode
            for account in self.accounts.values():  # Iterate over all accounts
                # Write account details to the file
                file.write(f"{account.account_number},{account.passwd},{account.account_type},{account.balance},{account.savings},{account.current}\n")

    def open_account(self, account_type):
        # Opens a new account with a random account number and password
        acc_no = str(random.randint(10000, 99999))  # Generate a random 5-digit account number
        passwd = str(random.randint(1000, 9999))  # Generate a random 4-digit password
        # Create a new account based on the specified account type
        if account_type.lower() == "business":
            self.accounts[acc_no] = BusinessAccount(acc_no, passwd)
        else:
            self.accounts[acc_no] = PersonalAccount(acc_no, passwd)
        self.save_accounts()  # Save the updated accounts to the file
        print(f"Account created. Number: {acc_no}, Password: {passwd}")  # Display the new account details

    def login(self, acc_no, passwd):
        # Logs in to an account using account number and password
        account = self.accounts.get(acc_no)  # Retrieve the account based on account number
        if account and account.passwd == passwd:  # Check if the account exists and the password matches
            print(f"Logged in to account {acc_no}")  # Display successful login message
            return account  # Return the account object
        else:
            print("Invalid account number or password")  # Display error message for invalid login
            return None  # Return None if login fails

    def send_money(self, from_account, to_acc_no, amount):
        # Sends money from one account to another, checking for sufficient funds
        to_account = self.accounts.get(to_acc_no)  # Retrieve the recipient account based on account number
        if to_account:  # Check if the recipient account exists
            if from_account.balance >= amount:  # Check if the sender has sufficient funds
                from_account.withdraw(amount)  # Withdraw the amount from the sender's account
                to_account.deposit(amount)  # Deposit the amount into the recipient's account
                self.save_accounts()  # Save the updated accounts to the file
                print(f"Sent Nu. {amount} to account {to_acc_no}")  # Display successful transfer message
            else:
                print("Insufficient funds")  # Display error message for insufficient funds
        else:
            print("Recipient account not found")  # Display error message if recipient account does not exist

    def delete_account(self, acc_no, passwd):
        # Deletes an account if the account number and password match
        account = self.accounts.get(acc_no)  # Retrieve the account based on account number
        if account and account.passwd == passwd:  # Check if the account exists and the password matches
            del self.accounts[acc_no]  # Delete the account from the dictionary
            self.save_accounts()  # Save the updated accounts to the file
            print(f"Account {acc_no} deleted")  # Display successful deletion message
        else:
            print("Invalid account number or password")  # Display error message for invalid account number or password

    def change_password(self, acc_no, current_passwd, new_passwd):
        # Changes the password for an account if the current password is correct
        account = self.accounts.get(acc_no)  # Retrieve the account based on account number
        if account and account.passwd == current_passwd:  # Check if the account exists and the current password matches
            account.passwd = new_passwd  # Update the account password
            self.save_accounts()  # Save the updated accounts to the file
            print(f"Password for account {acc_no} changed successfully")  # Display successful password change message
        else:
            print("Invalid account number or current password")  # Display error message for invalid account number or current password

    def transfer_to_savings(self, acc_no, amount):
        # Transfers a specified amount from the main balance to the savings account
        account = self.accounts.get(acc_no)  # Retrieve the account based on account number
        if account and account.balance >= amount:  # Check if the account exists and has sufficient funds
            account.balance -= amount  # Deduct the amount from the main balance
            account.savings += amount  # Add the amount to the savings balance
            self.save_accounts()  # Save the updated accounts to the file
            print(f"Transferred Nu. {amount} to savings. New savings balance: Nu. {account.savings}")  # Display successful transfer message
        else:
            print("Insufficient funds or invalid amount")  # Display error message for insufficient funds or invalid amount

    def transfer_to_current(self, acc_no, amount):
        # Transfers a specified amount from the main balance to the current account
        account = self.accounts.get(acc_no)  # Retrieve the account based on account number
        if account and account.balance >= amount:  # Check if the account exists and has sufficient funds
            account.balance -= amount  # Deduct the amount from the main balance
            account.current += amount  # Add the amount to the current balance
            self.save_accounts()  # Save the updated accounts to the file
            print(f"Transferred Nu. {amount} to current. New current balance: Nu. {account.current}")  # Display successful transfer message
        else:
            print("Insufficient funds or invalid amount")  # Display error message for insufficient funds or invalid amount

    def display_account_details(self, acc_no):
        # Displays all details of the account including savings and current balances
        account = self.accounts.get(acc_no)  # Retrieve the account based on account number
        if account:  # Check if the account exists
            # Display the account details
            print(f"Account Number: {account.account_number}")
            print(f"Account Type: {account.account_type}")
            print(f"Main Balance: Nu. {account.balance}")
            print(f"Savings Balance: Nu. {account.savings}")
            print(f"Current Balance: Nu. {account.current}")
        else:
            print("Account not found")  # Display error message if the account does not exist


# Instantiate the Bank class
bank_system = Bank()  # Creating an instance of the Bank class

# Handles various bank account operations
def account_operations(account):
    while True:  # Infinite loop to handle continuous account operations
        # Display menu options for account operations
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Send Money")
        print("5. Change Password")
        print("6. Delete Account")
        print("7. Transfer to Savings")
        print("8. Transfer to Current")
        print("9. Display Account Details")
        print("10. Logout")
                
        choice = input("Enter your choice: ")  # Get user choice
        
        if choice == '1':  # If the user chooses to deposit money
            amount = float(input("Enter amount to deposit: "))  # Get the deposit amount
            account.deposit(amount)  # Call the deposit method on the account
            bank_system.save_accounts()  # Save the updated account information
        
        elif choice == '2':  # If the user chooses to withdraw money
            amount = float(input("Enter amount to withdraw: "))  # Get the withdrawal amount
            account.withdraw(amount)  # Call the withdraw method on the account
            bank_system.save_accounts()  # Save the updated account information
        
        elif choice == '3':  # If the user chooses to check balance
            account.display_balance()  # Call the display_balance method on the account
                
        elif choice == '4':  # If the user chooses to send money
            recipient_acc_no = input("Enter recipient account number: ")  # Get recipient account number
            if recipient_acc_no != account.account_number:
                amount = float(input("Enter amount to send: "))  # Get the amount to send
                bank_system.send_money(account, recipient_acc_no, amount)  # Call send_money method on bank_system
            else:
                print(f'Can not transfer to its own account.')
        
        elif choice == '5':  # If the user chooses to change password
            current_passwd = input('Enter the current password: ')  # Get the current password
            new_passwd = input('Enter the new password: ')  # Get the new password
            if current_passwd != new_passwd:  # Check if the new password is different from the current password
                bank_system.change_password(account.account_number, current_passwd, new_passwd)  # Call change_password method on bank_system
            else:
                print('New password is the same as the old password.')  # Inform the user if passwords are the same

        elif choice == '6':  # If the user chooses to delete account
            confirm = input("Are you sure you want to delete your account? (yes/no): ")  # Get confirmation
            if confirm.lower() == 'yes':  # Check if user confirms
                bank_system.delete_account(account.account_number, account.passwd)  # Call delete_account method on bank_system
                break  # Exit the loop

        elif choice == '7':  # If the user chooses to transfer to savings
            amount = float(input("Enter amount to transfer to savings: "))  # Get the amount to transfer
            bank_system.transfer_to_savings(account.account_number, amount)  # Call transfer_to_savings method on bank_system

        elif choice == '8':  # If the user chooses to transfer to current
            amount = float(input("Enter amount to transfer to current: "))  # Get the amount to transfer
            bank_system.transfer_to_current(account.account_number, amount)  # Call transfer_to_current method on bank_system

        elif choice == '9':  # If the user chooses to display account details
            bank_system.display_account_details(account.account_number)  # Call display_account_details method on bank_system

        elif choice == '10':  # If the user chooses to logout
            confirm = input("Are you sure you want to logout? (yes/no): ")  # Get confirmation
            if confirm.lower() == 'yes':  # Check if user confirms
                break  # Exit the loop
        
        else:
            print("Invalid choice. Please try again.")  # Inform the user of invalid choice

# Main function to handle user interactions with the banking system
def main():
    while True:  # Infinite loop to handle continuous user interactions
        # Display main menu options
        print("\nWelcome to the Terminal Banking System")
        print("1. Open Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")  # Get user choice
        
        if choice == '1':  # If the user chooses to open an account
            acc_type = input("Enter account type (Business/Personal): ")  # Get account type
            bank_system.open_account(acc_type)  # Call open_account method on bank_system
        
        elif choice == '2':  # If the user chooses to login
            acc_no = input("Enter account number: ")  # Get account number
            passwd = input("Enter password: ")  # Get password
            account = bank_system.login(acc_no, passwd)  # Call login method on bank_system
            
            if account:  # If login is successful
                account_operations(account)  # Call account_operations function with the logged-in account
        
        elif choice == '3':  # If the user chooses to exit
            print("Exiting the banking system. Have a nice day!")  # Print exit message
            break  # Exit the loop
        
        else:
            print("Invalid choice. Please try again.")  # Inform the user of invalid choice

if __name__ == "__main__":  # Check if the script is run directly
    main()  # Call the main function