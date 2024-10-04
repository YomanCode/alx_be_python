from simple_calculator import SimpleCalculator
import unittest

class Test(unittest.TestCase):
    def test_add(self):
        check_Add = SimpleCalculator()
        add_result = check_Add.add(10, 5)
        self.assertEqual(add_result, 15)
    
    def test_subtract(self):
        check_sub = SimpleCalculator()
        sub_result = check_sub.subtract(10, 5)
        self.assertEqual(sub_result, 5)
    
    def test_multiply(self):
        check_multiply = SimpleCalculator()
        multiply_result = check_multiply.multiply(10, 5)
        self.assertEqual(multiply_result, 50)
    
    def test_division(self):
        check_division = SimpleCalculator()
        division_result = check_division.divide(10, 5)
        self.assertEqual(division_result, 2)


if __name__ == '__main__':
    unittest.main()