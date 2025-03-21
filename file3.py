# read/write master files
from read import read_old_bank_accounts
from write import write_new_current_accounts

def load_accounts(file_path):
    """
    Loads accounts from a formatted bank account file.
    Returns a list of validated account dictionaries.
    """
    return read_old_bank_accounts(file_path)

def save_accounts(accounts, file_path):
    """
    Saves account data to a new formatted file.
    """
    write_new_current_accounts(accounts, file_path)