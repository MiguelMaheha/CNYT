import unittest
import math

from main import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_complex((3, -8), (4, 6)), (7, -2))
        self.assertEqual(add_complex((-5, -4), (-6, -8)), (-11, -12))

    def test_multiply(self):
        self.assertEqual(multiply_complex((2, -3), (-1, 1)), (1, 5))
        self.assertEqual(multiply_complex((-7, -2), (-8, -9)), (38, 79))

    def test_modulus(self):
        self.assertEqual(modulus_complex((3, -8)), abs(math.sqrt(3 ** 2 + (-8) ** 2)))
        self.assertEqual(modulus_complex((-3, -16)), abs(math.sqrt((-3) ** 2 + (-16) ** 2)))

    def test_conjugate(self):
        self.assertEqual(conjugate_complex((3, -8)), (3, 8))
        self.assertEqual(conjugate_complex((-5, -2)), (-5, 2))


if __name__ == "__main__":
    unittest.main()