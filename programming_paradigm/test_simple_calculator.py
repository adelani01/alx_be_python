import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        #calc = SimpleCalculator()
        self.assertEqual(self.calc.add(10,5),15)
        self.assertEqual(self.calc.add(-10,5),-5)
        self.assertEqual(self.calc.add(-1,-1),-2)
        self.assertEqual(self.calc.add(-1,1),0)

    def test_subtract(self):
        """Test the addition method."""
        #calc = SimpleCalculator()
        self.assertEqual(self.calc.subtract(10,5),5)
        self.assertEqual(self.calc.subtract(2,5),-3)
        self.assertEqual(self.calc.subtract(-1,-1),0)
        self.assertEqual(self.calc.subtract(-1,4),-5)

    def test_multiply(self):
        """Test the addition method."""
        #calc = SimpleCalculator()
        self.assertEqual(self.calc.multiply(10,0),0)
        self.assertEqual(self.calc.multiply(-10,5),-50)
        self.assertEqual(self.calc.multiply(-5,-1),5)
        self.assertEqual(self.calc.multiply(5,-6),-30)
    
    def test_divide(self):
        """Test the addition method."""
       #calc = SimpleCalculator()
        self.assertEqual(self.calc.divide(10,5),2)
        self.assertEqual(self.calc.divide(-10,5),-2)
        self.assertEqual(self.calc.divide(-10,-10),1)
        self.assertEqual(self.calc.divide(20,100),0.2)






if __name__ == "__main__":
  unittest.main()