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

    def test_substraction(self):
        self.assertEqual(substraction((4, 3), (5, -2)), (-1, 5))
        self.assertEqual(substraction((7, 2), (-5, -4)), (12, 6))

    def test_division(self):
        self.assertEqual(division((20, -4), (3, 2)), (4, -4))
        self.assertEqual(division((4, 2), (-1, 1)), (-1, -3))

    def test_cartesian_to_polar(self):
        self.assertEqual(cartesian_to_polar((3, -8)), (modulus_complex((3, -8)), math.degrees(math.atan(-8 / 3))))
        self.assertEqual(cartesian_to_polar((-5, -2)), (modulus_complex((-5, -2)), math.degrees(math.atan(-2 / -5))))

    def test_polar_to_cartesian(self):
        self.assertEqual(polar_to_cartesian((3, -8)), (3 * math.cos(-8), 3 * math.sin(-8)))
        self.assertEqual(polar_to_cartesian((-5, -2)), (-5 * math.cos(-2), -5 * math.sin(-2)))

    def test_phase(self):
        self.assertEqual(phase((3, -8)), math.atan2(-8, 3))
        self.assertEqual(phase((-5, -2)), math.atan2(-2, -5))



if __name__ == "__main__":
    unittest.main()