'''Reference 
python banking system project. you can: 1. Open Account 2. Close Account 3. Withdraw Money
4. Deposit Money 5. Report for Management. (n.d.). Gist. 
https://gist.github.com/Edgars-Duka/feae5c1fe986a5cf69ccd39b96619332

Python OOP: Bank class for customer account management. (2023, November 25). W3resource. 
https://www.w3resource.com/python-exercises/oop/python-oop-exercise-11.php

Sharma, R. (2024, May 21). Python Banking Project [With Source Code] in 2024. upGrad blog. 
https://www.upgrad.com/blog/python-banking-project/
'''

from bank import Bank  # Importing the Bank class from the bank module

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