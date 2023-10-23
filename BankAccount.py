# importing 'random' to allow for random account number generation
import random

# creating a BankAccount class
class BankAccount:
    def __init__(self, full_name, account_number = None):
        self.full_name = full_name
        if account_number is None:
            self.account_number = random.randint(10000000, 99999999)
        else: 
            self.account_number = account_number 
        self.balance = 0.0

    # Account number generator 
    def account_number_generator(self):
        self.account_number = random.randint(10000000, 99999999)

    # Desposit method
    def deposit(self, amount):
        self.balance += amount
        print(f'Amount Deposited: ${amount}. New Balance: ${self.balance}')
    # Withdraw method
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 10
            print(f'Insufficient funds. You have been charged an overdraft fee of $10.')
        print(f'Amount Withdrawn: ${amount}. New Balance: ${self.balance}')
    # Get balance method
    def get_balance(self):
        print(f'Your balance is ${self.balance}')
        return self.balance
    # Add interest method
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
    # Print statement method
    def print_statement(self):
        print(self.full_name)
        print(f'Account No.: {self.account_number}')
        print(f'Balance: ${self.balance}')

# creating a new instance of the BankAccount class, running methods
# 1/3
rileys_account = BankAccount('Riley Nowak')
rileys_account.deposit(100)
rileys_account.withdraw(50)
rileys_account.add_interest()
rileys_account.get_balance()
rileys_account.print_statement()

# creating a new instance of the BankAccount class, running methods
# 2/3
timbers_account = BankAccount('Timber')
timbers_account.deposit(500)
timbers_account.withdraw(550)
timbers_account.add_interest()
timbers_account.get_balance()
timbers_account.print_statement()

# creating a new instance of the BankAccount class, running methods
# 3/3
snickers_account = BankAccount('Snickers')
snickers_account.deposit(10000)
snickers_account.withdraw(20)
snickers_account.add_interest()
snickers_account.get_balance()
snickers_account.print_statement()

# creating Mitchell's account and running methods
mitchells_account = BankAccount('Mitchell Hudson', '03141592')
mitchells_account.deposit(400000)
mitchells_account.print_statement()
mitchells_account.add_interest()
mitchells_account.print_statement()
mitchells_account.withdraw(150)
mitchells_account.print_statement()

