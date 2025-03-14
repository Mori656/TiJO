import unittest
from src.quadratic_equation_tests import QuadraticEquation as QE

class QuadraticEquationTestCase(unittest.TestCase):
    def test_raise_error_when_a_is_zero(self):
        a, b, c = 0, 2, 4
        self.assertRaises(ValueError, QE , a,b,c)
    def test_two_value_return(self):
        a, b, c = 2, 6, 2.5
        QEQ = QE(a,b,c)
        result = QEQ.solve()
        self.assertEqual(result,(-0.5,-2.5))
    def test_one_value_return(self):
        a, b, c = 2, 4, 2
        QEQ = QE(a,b,c)
        result = QEQ.solve()
        self.assertEqual(result,(-1,))
    def test_when_delta_is_under_zero(self):
        a, b, c = 2, 6, 6
        QEQ = QE(a,b,c)
        result = QEQ.solve()
        self.assertEqual(result,None)
if __name__ == '__main__':
    unittest.main()
