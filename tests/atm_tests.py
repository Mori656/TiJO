import unittest
from src.atm import ATM

class atmCaseTests(unittest.TestCase):
    def test_check_balance_raise_error_when_pin_is_wrong(self):
        atm = ATM(10,1234)
        with self.assertRaises(ValueError):
            atm.check_balance(4532)
        pass
    def test_check_balance_when_correct_pin(self):
        atm = ATM(10,1234)
        result = atm.check_balance(1234)
        self.assertEqual(result,10)
        pass
    def test_deposit_raise_error_when_pin_is_wrong(self):
        atm = ATM(10,1234)
        with self.assertRaises(ValueError):
            atm.deposit(4532,100)
        pass
    def test_deposit_when_correct_pin(self):
        atm = ATM(10,1234)
        result = atm.deposit(1234,100)
        self.assertEqual(result,110)
        pass
    def test_withdraw_raise_error_when_pin_is_wrong(self):
        atm = ATM(10,1234)
        with self.assertRaises(ValueError):
            atm.withdraw(4532,5)
        pass
    def test_withdraw_when_correct_pin_but_not_enough_money_on_account(self):
        atm = ATM(10,1234)
        with self.assertRaises(ValueError):
            atm.withdraw(1234,100)
        pass
    def test_withdraw_when_correct_pin_and_enough_money_on_account(self):
        atm = ATM(100,1234)
        result = atm.withdraw(1234,100)
        self.assertEqual(result,0)
        pass


if __name__ == '__main__':
    unittest.main()
