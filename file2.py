#executes transactions and validates them
from print_error import log_constraint_error
from file1 import process_deposit, process_withdrawal, process_transfer

def validate_transaction(account, transaction_type, amount):
    
    #Validates if a transaction can be performed.
    
    if transaction_type not in ['deposit', 'withdrawal', 'transfer']:
        log_constraint_error("Validation Error", f"Invalid transaction type: {transaction_type}")
        return False
    if amount <= 0:
        log_constraint_error("Validation Error", "Transaction amount must be positive.")
        return False
    if account['status'] != 'A':
        log_constraint_error("Validation Error", "Account is not active.")
        return False
    return True

def execute_transaction(accounts, transaction):
    
    #Executes a validated transaction.
    
    transaction_type, account_number, amount = transaction[:3]
    
    account = next((acc for acc in accounts if acc['account_number'] == account_number), None)
    if not account:
        log_constraint_error("Execution Error", f"Account {account_number} not found.")
        return False
    
    if not validate_transaction(account, transaction_type, amount):
        return False
    
    if transaction_type == 'deposit':
        return process_deposit(account, amount)
    elif transaction_type == 'withdrawal':
        return process_withdrawal(account, amount)
    elif transaction_type == 'transfer':
        if len(transaction) < 4:
            log_constraint_error("Execution Error", "Missing destination account for transfer.")
            return False
        dest_account_number = transaction[3]
        dest_account = next((acc for acc in accounts if acc['account_number'] == dest_account_number), None)
        if not dest_account:
            log_constraint_error("Execution Error", f"Destination account {dest_account_number} not found.")
            return False
        return process_transfer(account, dest_account, amount)
    
    return False

def update_balance(account, amount):
    
    #Updates the balance of an account and increments transaction count.
    
    account['balance'] += amount
    account['total_transactions'] += 1
    return True

def check_account_status(account):

    #Checks if the account is active before processing transactions.
    
    return account['status'] == 'A'
