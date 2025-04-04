import unittest
from file1 import apply_transaction_fee, process_deposit, process_withdrawal
from file2 import validate_transaction, execute_transaction

class TestBackendFunctions(unittest.TestCase):

    def setUp(self):
        self.account = {'balance': 100.0, 'status': 'A', 'account_number': '12345'}
        self.accounts = [self.account]

    # Test 1
    def test_apply_transaction_fee_withdrawal(self):
        apply_transaction_fee(self.account, 'withdrawal')
        self.assertEqual(self.account['balance'], 99.5)

    # Test 2
    def test_apply_transaction_fee_transfer(self):
        self.account['balance'] = 100.0
        apply_transaction_fee(self.account, 'transfer')
        self.assertEqual(self.account['balance'], 99.0)

    # Test 3
    def test_apply_transaction_fee_no_fee(self):
        self.account['balance'] = 100.0
        apply_transaction_fee(self.account, 'deposit')
        self.assertEqual(self.account['balance'], 100.0)

    # Test 5
    def test_process_deposit_valid(self):
        self.account['balance'] = 100.0
        result = process_deposit(self.account, 50)
        self.assertTrue(result)
        self.assertEqual(self.account['balance'], 150.0)

    # Test 6
    def test_process_deposit_negative(self):
        result = process_deposit(self.account, -10)
        self.assertFalse(result)

    # Test 8
    def test_process_withdrawal_valid(self):
        self.account['balance'] = 100.0
        result = process_withdrawal(self.account, 50)
        self.assertTrue(result)
        self.assertEqual(self.account['balance'], 49.5)

    # Test 9
    def test_process_withdrawal_negative(self):
        result = process_withdrawal(self.account, -10)
        self.assertFalse(result)

    # Test 19
    def test_validate_transaction_valid(self):
        result = validate_transaction(self.account, 'deposit', 100)
        self.assertTrue(result)

    # Test 20
    def test_validate_transaction_negative_amount(self):
        result = validate_transaction(self.account, 'deposit', -5)
        self.assertFalse(result)

    # Test 21
    def test_validate_transaction_inactive_account(self):
        self.account['status'] = 'I'
        result = validate_transaction(self.account, 'deposit', 50)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()