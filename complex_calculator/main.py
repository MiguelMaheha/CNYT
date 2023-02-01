import math

def add_complex(c1: tuple, c2: tuple) -> tuple:
    return (c1[0] + c2[0], c1[1] + c2[1])


def multiply_complex(c1: tuple, c2: tuple) -> tuple:
    return (c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c2[0] * c1[1])


def modulus_complex(c: tuple) -> float:
    return abs(math.sqrt((c[0]) ** 2 + (c[1]) ** 2))


def conjugate_complex(c: tuple) -> tuple:
    return (c[0], -c[1])


def substraction(c1: tuple, c2: tuple) -> tuple:
    return (c1[0] - c2[0], c1[1] - c2[1])


def division(c1: tuple, c2: tuple) -> tuple:
    c2_conjugate = conjugate_complex(c2)
    x = multiply_complex(c1, c2_conjugate)
    y = multiply_complex(c2, c2_conjugate)
    real = x[0] // y[0]
    imaginary = x[1] // y[0]
    return (real, imaginary)


def print_complex(c: tuple):
    print(f"{c[0]} + {c[1]}i")


if __name__ == "__main__":
    # print_complex(add_complex((3, -8), (4, 6)))
    # print_complex(multiply_complex((-7, -2), (-8, -9)))
    # print(add_complex((-5, -4), (-6, -8)))
    # print_complex(conjugate_complex((3, -8)))
    # print((-5, -2) == (-5, 20))
    print_complex(division((20, -4), (3, 2)))
