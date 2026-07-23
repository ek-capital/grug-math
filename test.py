#!/usr/bin/env python3

from fractions import Fraction

from check import interpolate, lr_coefficient, partition


def main() -> None:
    assert partition([3, 2, 1]) == (3, 2, 1)
    assert lr_coefficient((3, 2, 1), (2, 1), (2, 1)) == 2
    assert lr_coefficient((3, 3), (2, 1), (2, 1)) == 1
    assert lr_coefficient((2, 1, 1, 1, 1), (2, 1), (2, 1)) == 0
    assert interpolate([0, 1, 4, 9]) == [
        Fraction(0),
        Fraction(0),
        Fraction(1),
    ]
    assert interpolate([1, 4, 9], start=1) == [
        Fraction(0),
        Fraction(0),
        Fraction(1),
    ]
    print("ok")


if __name__ == "__main__":
    main()
