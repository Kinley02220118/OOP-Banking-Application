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
