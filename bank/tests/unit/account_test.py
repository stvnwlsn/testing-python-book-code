#!/usr/bin/env python

import unittest
from bank.account import Account


class TestAccount(unittest.TestCase):
    def test_account_object_can_be_created(self):
        account = Account("000", 100)

    def test_account_object_returns_current_balance(self):
        account = Account("001", 50)
        self.assertEqual(account.account_number, "001")
        self.assertEqual(account.balance, 50)


if __name__ == '__main__':
    unittest.main()
