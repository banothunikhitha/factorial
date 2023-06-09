import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_negative_factorial(self):
        self.assertRaises(ValueError, factorial, -1)

    def test_noninteger_factorial(self):
        self.assertRaises(TypeError, factorial, 1.5)

if _name_ == '_main_':
    unittest.main()
