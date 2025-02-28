import unittest

import src.main as m

class TestCalc(unittest.TestCase):
    def setUp(self):
        print("* setUp()")
        self.calc = m.Calc()

    def test_add(self):
        print("** test_add()")
        result = self.calc.add(3, 2)
        self.assertEqual(result, 5)

    def test_devide_by_zero(self):
        print("** test_divide_by_zero()")
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_substract(self):
        print("** test_substract()")
        result = self.calc.substract(3, 2)
        self.assertEqual(result, 1)

    def test_multiply(self):
        print("** test_multiply()")
        result = self.calc.multiply(4, 8)
        self.assertEqual(result, 32)

    def tearDown(self):
        print("*** tearDown()")
        self.calc = None

if __name__ == "__main__":
    unittest.main()