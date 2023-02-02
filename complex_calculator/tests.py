import unittest
import math
import cmath

from main import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        a = complex(3, -8)
        b = complex(4, 6)
        result = a + b
        self.assertEqual(add_complex((3, -8), (4, 6)), (result.real, result.imag))

        a = complex(-5, -4)
        b = complex(-6, -8)
        result = a + b
        self.assertEqual(add_complex((-5, -4), (-6, -8)), (result.real, result.imag))

    def test_multiply(self):
        a = complex(2, -3)
        b = complex(-1, 1)
        result = a * b
        self.assertEqual(multiply_complex((2, -3), (-1, 1)), (result.real, result.imag))

        a = complex(-7, -2)
        b = complex(-8, -9)
        result = a * b
        self.assertEqual(multiply_complex((-7, -2), (-8, -9)), ((result.real, result.imag)))

    def test_modulus(self):
        c = complex(1, -1)
        self.assertEqual(modulus_complex((1, -1)), abs(c))
        c = complex(-3, -16)
        self.assertEqual(modulus_complex((-3, -16)), abs(c))

    def test_conjugate(self):
        c1 = complex(3, -8).conjugate()
        c2 = complex(-5, -2).conjugate()
        self.assertEqual(conjugate_complex((3, -8)), (c1.real, c1.imag))
        self.assertEqual(conjugate_complex((-5, -2)), (c2.real, c2.imag))

    def test_substraction(self):
        a = complex(4, 3)
        b = complex(5, -2)
        result = a - b
        self.assertEqual(substraction((4, 3), (5, -2)), (result.real, result.imag))

        a = complex(7, 2)
        b = complex(-5, -4)
        result = a - b
        self.assertEqual(substraction((7, 2), (-5, -4)), (result.real, result.imag))

    def test_division(self):
        a = complex(20, -4)
        b = complex(3, 2)
        result = a / b
        self.assertEqual(division((20, -4), (3, 2)), (result.real, result.imag))

        a = complex(4, 2)
        b = complex(-1, 1)
        result = a / b
        self.assertEqual(division((4, 2), (-1, 1)), (-1, -3))

    def test_cartesian_to_polar(self):
        c1 =  complex(3, -8)
        self.assertEqual(cartesian_to_polar((3, -8)), (cmath.polar(c1)))
        c2 = complex(-5, -2)
        self.assertEqual(cartesian_to_polar((-5, -2)), cmath.polar(c2))

    def test_polar_to_cartesian(self):
        c1 = cmath.polar(complex(3, -8))
        result = cmath.rect(c1[0], c1[1])
        self.assertEqual(polar_to_cartesian((3, -8)), (result.real, result.imag))

        c2 = cmath.polar(complex(-5, -2))
        result = cmath.rect(c2[0], c2[1])
        self.assertEqual(polar_to_cartesian((-5, -2)), (result.real, result.imag))

    def test_phase(self):
        c = cmath.phase(complex(3, -8))
        self.assertEqual(phase((3, -8)), c)

        c = cmath.phase(complex(-5, -2))
        self.assertEqual(phase((-5, -2)), c)



if __name__ == "__main__":
    unittest.main()