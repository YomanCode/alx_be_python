from simple_calculator import SimpleCalculator
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        add_result = self.calc.add(10, 5)
        self.assertEqual(self.calc.add(10, 5), 15)
    
    def test_subtraction(self):
        sub_result = self.calc.subtract(10, 5)
        self.assertEqual(self.calc.subtract(10, 5), 5)
    
    def test_multiplication(self):
        multiply_result = self.calc.multiply(10, 5)
        self.assertEqual(self.calc.multiply(10, 5), 50)
    
    def test_division(self):
        division_result = self.calc.divide(10, 5)
        self.assertRaises(ZeroDivisionError)
        self.assertEqual(self.calc.divide(10, 5), 2)


if __name__ == '__main__':
    unittest.main()