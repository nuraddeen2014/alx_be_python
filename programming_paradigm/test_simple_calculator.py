import unittest 
from simple_calculator import SimpleCalculator

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10,2),12)
        self.assertEqual(self.calc.add(-10,2),-8)
        self.assertEqual(self.calc.add(-2,2),0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10,2),8)
        self.assertEqual(self.calc.subtract(-10,2),-12)
        self.assertEqual(self.calc.subtract(-2,2),-4)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10,2),20)
        self.assertEqual(self.calc.multiply(-10,2),-20)
        self.assertEqual(self.calc.multiply(-2,2),-4)

    def test_division(self):
        self.assertEqual(self.calc.divide(-10,2),-5)
        self.assertEqual(self.calc.divide(-2,2),-1)
        self.assertEqual(self.calc.divide(10,2),5)
        self.assertEqual(self.calc.divide(10,0),None)


if __name__ == '__main__':
    unittest.main()