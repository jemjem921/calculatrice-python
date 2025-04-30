import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from main import addition, soustraction, multiplication, division


import unittest
from main import addition, soustraction, multiplication, division

class TestOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)

    def test_soustraction(self):
        self.assertEqual(soustraction(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(multiplication(4, 3), 12)

    def test_division(self):
        self.assertEqual(division(6, 2), 3)

    def test_division_zero(self):
        self.assertEqual(division(4, 0), "Erreur : division par zéro")

if __name__ == '__main__':
    unittest.main()
import unittest

from src.operations import *

class TestOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)

    def test_soustraction(self):
        self.assertEqual(soustraction(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(multiplication(4, 3), 12)

    def test_division(self):
        self.assertEqual(division(6, 2), 3)
    
    def test_division_zero(self):
        with self.assertRaises(ValueError):
            division(4, 0)

if __name__ == '__main__':
    unittest.main()
