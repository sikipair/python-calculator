import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-10, 4), -6)
        self.assertEqual(self.calc.add(-2, -5), -7)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 7), -6)
        self.assertEqual(self.calc.subtract(-6, 4), -10)
        self.assertEqual(self.calc.subtract(-3, -3), 0)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-30, -1), 30)
        self.assertEqual(self.calc.multiply(6, -5), -30)
        self.assertEqual(self.calc.multiply(10, 0), 0)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(-5, 2), -2)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertEqual(self.calc.divide(8, 0), None)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(4, -2), 0)
        self.assertEqual(self.calc.modulo(-7, -3), -1)
        self.assertEqual(self.calc.modulo(3, 2), 1)

if __name__ == '__main__':
    unittest.main()
