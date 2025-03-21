# act as the controller to coordinate everything
from file3 import load_accounts, save_accounts
from file2 import execute_transaction
from print_error import log_constraint_error

def run_backend(account_file, transaction_file, output_file):
    """
    Coordinates reading accounts, processing transactions, and saving updates.
    """
    accounts = load_accounts(account_file)

    try:
        with open(transaction_file, 'r') as tf:
            for line in tf:
                parts = line.strip().split()
                if not parts or parts[0].upper() == 'EOS':
                    break

                try:
                    transaction_type = parts[0].lower()
                    if transaction_type == 'transfer' and len(parts) == 4:
                        transaction = (transaction_type, parts[1], float(parts[2]), parts[3])
                    elif transaction_type in ('deposit', 'withdrawal') and len(parts) == 3:
                        transaction = (transaction_type, parts[1], float(parts[2]))
                    else:
                        raise ValueError
                except ValueError:
                    log_constraint_error("Input Error", f"Invalid transaction format: {' '.join(parts)}")
                    continue

                execute_transaction(accounts, transaction)

    except FileNotFoundError:
        log_constraint_error("File Error", f"Transaction file '{transaction_file}' not found.")
        return

    save_accounts(accounts, output_file)