import random  # Importing the random module to generate random account numbers and passwords
import os  # Importing the os module to check for the existence of the accounts file
from account import BusinessAccount, PersonalAccount  # Importing account classes from account module

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
