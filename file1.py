# handles transactions and fees
from print_error import log_constraint_error

def apply_transaction_fee(account, transaction_type):
    
    #Applies a transaction fee based on the transaction type.
    
    fees = {
        'withdrawal': 0.50,
        'transfer': 1.00,
    }
    fee = fees.get(transaction_type, 0)
    account['balance'] -= fee

    if account['balance'] < 0:
        apply_overdraft_fee(account)

def process_deposit(account, amount):
    
    #Processes a deposit transaction.
    
    if amount <= 0:
        log_constraint_error("Transaction Error", "Deposit amount must be positive.")
        return False
    
    account['balance'] += amount
    return True

def process_withdrawal(account, amount):
    
    #Processes a withdrawal transaction.
    
    if amount <= 0:
        log_constraint_error("Transaction Error", "Withdrawal amount must be positive.")
        return False
    if account['balance'] < amount:
        log_constraint_error("Transaction Error", "Insufficient funds for withdrawal.")
        return False
    
    account['balance'] -= amount
    apply_transaction_fee(account, 'withdrawal')
    return True

def process_transfer(source_account, dest_account, amount):
    
    #Processes a transfer transaction.
    
    if amount <= 0:
        log_constraint_error("Transaction Error", "Transfer amount must be positive.")
        return False
    if source_account['balance'] < amount:
        log_constraint_error("Transaction Error", "Insufficient funds for transfer.")
        return False
    
    source_account['balance'] -= amount
    dest_account['balance'] += amount
    apply_transaction_fee(source_account, 'transfer')
    return True

def apply_overdraft_fee(account):
    
    #Applies an overdraft fee if the balance goes negative.
    
    overdraft_fee = 5.00
    account['balance'] -= overdraft_fee
    log_constraint_error("Overdraft Fee", "An overdraft fee has been applied.")
