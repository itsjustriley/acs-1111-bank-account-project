import random

class BankAccount:
    def __init__(self):
        self.full_name = 'full name'
        self.account_number = random.randint(10000000, 99999999)
        self.balance = 0.0
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Amount Deposited: ${amount}. New Balance: ${self.balance}')

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 10
            print(f'Insufficient funds. You have been charged an overdraft fee of $10.')
        print(f'Amount Withdrawn: ${amount}. New Balance: ${self.balance}')

    def get_balance(self):
        print(f'Your balance is ${self.balance}')
        return self.balance
    
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
    
    def print_statement(self):
        print(self.full_name)
        print(f'Account No.: {self.account_number}')
        print(f'Balance: ${self.balance}')

