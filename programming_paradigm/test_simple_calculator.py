from simple_calculator import SimpleCalculator
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        add_result = self.calc.add(10, 5)
        self.assertEqual(add_result, 15)
    
    def test_subtract(self):
        sub_result = self.calc.subtract(10, 5)
        self.assertEqual(sub_result, 5)
    
    def test_multiply(self):
        multiply_result = self.calc.multiply(10, 5)
        self.assertEqual(multiply_result, 50)
    
    def test_division(self):
        division_result = self.calc.divide(10, 5)
        self.assertRaises(ZeroDivisionError)
        self.assertEqual(division_result, 2)


if __name__ == '__main__':
    unittest.main()