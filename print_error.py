def log_constraint_error(constraint_type, description):
    """
    Logs a standardized constraint error message to the console.

    Args:
        constraint_type (str): The category of the error (e.g., 'Transaction Error').
        description (str): Detailed explanation of the constraint violation.
    """
    print(f"ERROR: {constraint_type}: {description}")