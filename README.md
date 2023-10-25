# acs-1111-bank-account-project
### Bank Account (OOP) project for ACS 1111

- [x] Your Python program should be created in one file called BankAccount.py.
- [x] Define a BankAccount class. A bank account should have the following attributes:
    - [x] full_name - the full name of the bank account account owner.
    - [x] account_number - randomly generated 8 digit number, unique per account.
    - [x] balance - the balance of money in the account, should start at 0.
- [x] Then define the following methods for the BankAccount class:
    - [x] deposit method
        - [x] will take one parameter amount and will add amount to the balance.
        - [x] will print the message: “Amount deposited: $X.XX new balance: $Y.YY”
    - [x] withdraw method 
        - [x] will take one parameter amount and will subtract amount from the balance. 
        - [x] will print a message, like “Amount withdrawn: $X.XX new balance: $Y.YY”.
        - [x] If the user tries to withdraw an amount that is greater than the current balance, print ”Insufficient funds.” and charge them with an overdraft fee of $10
    - [x] get_balance method
        - [x] will print a user-friendly message with the account balance and then also return the current balance of the account.
    - [ ] add_interest method
        - [x] adds interest to the users balance.
            - [x] The annual interest rate is 1% (i.e. 0.083% per month).
            - [x] monthly interest is calculated by the following equation: interest = balance *  0.00083 .
    - [x] print_statement method
        - [x] prints a message with the account name, account number, and balance like this:
            ```
            Joi Anderson
            Account No.: ****5678
            Balance: $100.00
            ```
- [x] Outside of the BankAccount class, define 3 different bank account examples using the BankAccount() object.
    - [x] Your examples should show you using the different methods above to demonstrate them working.
- [x] Include example code to do the following:
    - [x] Create a new bank account instance: user: "Mitchell", account number: 03141592.
    - [x] Deposit $400,000 into "Mitchell's" account.
    - [x] Print a statement
    - [x] Add interest to the account
    - [x] Print a statement
    - [x] Make a withdrawl of $150 (Mitchell needs some Yeezy's)
    - [x] Print a statement

### Stretch Challenges (Optional)
- [x] Add an attribute to set the account type: checking or savings.
- [x] A savings account gets 1.2% insterest (that's 1% per month)
- [x] Create a checking and a savings account
- [x] Add interest to each account
- [x] Print a statement for each account
- [x] Create a list called: bank. (NOTE: called this accounts) Add all of your accounts to bank. Write a function that loops over all accounts in the list and calls the add_interst method of each.
- [x] Create an "application". Use a loop to prompt us for an action. Actions can be:
    - [x] Create account - Prompt for name, number, and balance.
    - [x] Statement - prompts for the account number and prints the statement for that account.
    - [x] Deposit - prompts for account number and amount. Then makes a deposit.
    - [x] Withdraw - prompts for account number and amount. Then makes a withdrawl
- [x] Create a Bank class. This class will store a list of BackAccounts. It should implement the following methods:
    - [x] create_account() - creates a new account.
    - [x] deposit() - deposits an amount into an account with an account number
    - [x] withdraw() - removes an amount from an account with an account number
    - [x] transfer() - withdraws an amount from an account with an account number and deposits the same amount to an account with another number.
    - [x] statement() - prints an statement for an account with an account number.
