from simple_calculator import SimpleCalculator
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)
    
    def test_division(self):
        self.assertRaises(ZeroDivisionError)
        self.calc.divide(10, 0)
        self.assertEqual(self.calc.divide(10, 5), 2)


if __name__ == '__main__':
    unittest.main()