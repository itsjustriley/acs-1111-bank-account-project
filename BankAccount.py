# importing 'random' to allow for random account number generation
import random

# creating a Bank class
class Bank:
    def __init__(self):
        self.accounts_list = []
        self.account_numbers = []

    def account_number_generator(self):
        new_account_number = str(random.randint(10000000, 99999999))
        if new_account_number in self.account_numbers:
            while new_account_number in self.account_numbers:
                str(new_account_number = random.randint(10000000, 99999999))
        return new_account_number
    
    def create_account(self, full_name, type='checking'):
        new_account_number = self.account_number_generator()
        new_account = BankAccount(full_name, type, new_account_number, self)
        self.accounts_list.append(new_account)
        self.account_numbers.append(new_account_number)
        print(f'Account ({type}) created for {full_name}.')
        return new_account_number
    
    def deposit(self, amount, account_number):
        account_found = False
        for account in self.accounts_list:
            if account.account_number == account_number:
                account.deposit(amount)
                account_found = True
        if account_found == False:
            print('Account not found. Please enter a valid account number.')
    
    def withdraw(self, amount, account_number):
        for account in self.accounts_list:
            if account.account_number == account_number:
                account.withdraw(amount)
    
    def transfer(self, amount, account_number_from, account_number_to):
        for account in self.accounts_list:
            if account.account_number == account_number_from:
                account.withdraw(amount)
            if account.account_number == account_number_to:
                account.deposit(amount)
    
    def add_interest(self, account_number):
        for account in self.accounts_list:
            if account.account_number == account_number:
                account.add_interest()
    
    def statement(self, account_number):
        for account in self.accounts_list:
            if account.account_number == account_number:
                account.print_statement()

    def all_interest(self):
        for account in self.accounts:
            account.add_interest()

# creating a BankAccount class
class BankAccount:
    def __init__(self, full_name, type = 'checking', account_number = None, bank = None, balance = 0):
        self.full_name = full_name
        self.bank = bank
        self.account_number = account_number
        self.type = type
        self.balance = balance
        if type == 'checking':
            self.interest_rate = 0.00083
        elif type == 'savings':
            self.interest_rate = 0.01
    
    # String method
    def __str__(self):
        return f'Account {self.account_number} ({self.type}): {self.full_name}, Balance: ${self.balance}'
    
    # Desposit method
    def deposit(self, amount):
        if amount < 0:
            print('Cannot deposit a negative amount.')
            return
        amount = round(amount, 2)
        self.balance += amount
        print(f'Amount Deposited: ${amount}. New Balance: ${self.balance}')
    # Withdraw method
    def withdraw(self, amount):
        if amount < 0:
            print('Cannot withdraw a negative amount.')
            return
        amount = round(amount, 2)
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
    # opting for elif, in case I were to add a thrd type of account later
    def add_interest(self):
        self.balance += (self.balance * self.interest_rate)

    # Print statement method
    def print_statement(self):
            hidden_account_number = str(self.account_number)
            hidden_account_number = '****' + hidden_account_number[-4:]  # Replace the first characters with '*'
            print(self.full_name)
            print(f'Account No.: {hidden_account_number}')
            print(f'Balance: ${self.balance}')

# Banking App

class BankApp:
    def __init__(self):
        bank = Bank()
        self.bank = bank
        self.run()

    def menu(self):
            valid_selection = False
            while valid_selection == False:
                print('What would you like to do?')
                print('1. Create an account')
                print('2. Deposit money')
                print('3. Withdraw money')
                print('4. Transfer money')
                print('5. Print Statement')
                selection = input('Enter the number of your choice: ')
                if selection == '1':
                    name = input('Please enter your full name: ')
                    valid_type = False
                    while valid_type == False:
                        type = input('Would you like to create a checkings or savings account? (1. Checking 2. Savings) :  ')
                        if type == '1':
                            valid_type = True
                            type = 'checking'
                        elif type == '2':
                            valid_type = True
                            type = 'savings'
                        else:
                            print('Please enter a valid option')
                    new_acct_num = self.bank.create_account(name, type)
                    print(f'Your new account number is: {new_acct_num}')
                elif selection == '2':
                    valid_selection = True
                    deposit_account = input('Please enter the account number: ')
                    deposit_amount = float(input('Please enter the amount you would like to deposit: '))
                    self.bank.deposit(deposit_amount, deposit_account)
                elif selection == '3':
                    valid_selection = True
                    withdrawal_account = input('Please enter the account number: ')
                    withdrawal_amount = float(input('Please enter the amount you would like to withdraw: '))
                    self.bank.withdraw(withdrawal_amount, withdrawal_account)
                elif selection == '4':
                    valid_selection = True
                    account_from = input('Please enter the account number you would like to transfer from: ')
                    account_to = input('Please enter the account number you would like to transfer to: ')
                    transfer_amount = float(input('Please enter the amount you would like to transfer: '))
                    self.bank.transfer(transfer_amount, account_from, account_to)
                elif selection == '5':
                    valid_selection = True
                    statement_account = input('Please enter the account number: ')
                    self.bank.statement(statement_account)
                else:
                    print('Please enter a valid option')

    def sample_accounts(self):
        sample1 = BankAccount('Riley Nowak', 'checking', '11111111', self.bank, 111.11)
        sample2 = BankAccount('Riley Nowak', 'savings', '22222222', self.bank, 222.22)
        sample3 = BankAccount('Mitchell Hudson', 'checking', '33333333', self.bank, 333.33)
        sample4 = BankAccount('Mitchell Hudson', 'savings', '44444444', self.bank, 444.44)
        sample5 = BankAccount('Timber', 'checking', '55555555', self.bank, 555.55)
        sample6 = BankAccount('Timber', 'savings', '66666666', self.bank, 666.66)
        sample_accounts = [sample1, sample2, sample3, sample4, sample5, sample6]
        for account in sample_accounts:
            self.bank.accounts_list.append(account)
            self.bank.account_numbers.append(account.account_number)

    def run(self):
        print('For demonstration purposes, we have created some sample accounts for you to use.')
        print('Each of these has an account number of 8 repeating digits, and a corresponding balance.')
        self.sample_accounts()
        for account in self.bank.accounts_list:
            account.print_statement()
            print('----------------')
        input('Press enter to continue: ')
        print('Welcome to the Banking App!')
        menu = True
        while menu == True:
            self.menu()
            prompt_again = True
            while prompt_again == True:
                again = input('Would you like to make another transaction? (y/n): ')
                if again == 'n':
                    menu = False
                    print('Thank you for using the Banking App!')
                elif again != 'y':
                    print('Please enter a valid option')
                else:
                    prompt_again = False




bank_app = BankApp()
bank_app.run()


## Showing my work from earlier in the process: 

# # creating a new instance of the BankAccount class, running methods
# # This was created prior to the bank class
# # 1/3
# rileys_account = BankAccount('Riley Nowak')
# rileys_account.deposit(100)
# rileys_account.withdraw(50)
# rileys_account.add_interest()
# rileys_account.get_balance()
# rileys_account.print_statement()

# creating a new instance of the BankAccount class, running methods
# # This was created prior to the bank class
# 2/3
# timbers_account = BankAccount('Timber')
# timbers_account.deposit(500)
# timbers_account.withdraw(550)
# timbers_account.add_interest()
# timbers_account.get_balance()
# timbers_account.print_statement()

# creating a new instance of the BankAccount class, running methods
# # This was created prior to the bank class
# 3/3
# snickers_account = BankAccount('Snickers')
# snickers_account.deposit(10000)
# snickers_account.withdraw(20)
# snickers_account.add_interest()
# snickers_account.get_balance()
# snickers_account.print_statement()

# creating Mitchell's account and running methods
# # This was created prior to the bank class
# mitchells_account = BankAccount('Mitchell Hudson', '03141592')
# mitchells_account.deposit(400000)
# mitchells_account.print_statement()
# mitchells_account.add_interest()
# mitchells_account.print_statement()
# mitchells_account.withdraw(150)
# mitchells_account.print_statement()

# # creating a new Bank
# bank = Bank()

# creating new checking and savings accounts

# newChecking = bank.create_account('Riley Nowak', 'checking')
# bank.desposit(1000, newChecking)
# newSaving = bank.create_account('Riley Nowak', 'savings')
# bank.desposit(2000, newSaving)
# bank.add_interest(newSaving)
# bank.add_interest(newChecking)
# bank.statement(newSaving)
# bank.statement(newChecking)


