#!/usr/bin/python3

import sys
import math
import random


def pollardRho(n):
    """
    Pollard's Rho method to factor large integers, I
    will use the polynomial F(x) = x ** 2 + 1
    x is initialized 2

    the usage of Floyd's cycle detection method,
    number theory (gcd), and the birthday paradox
    will be of assistance to solve this problem

    Args:
        n (int): composite number to factorize
    """
    if (n % 2 == 0):
        print("{}={}*{}".format(n, 2, int(n / 2)))
        return

    x = 2
    y = x
    d = 1

    while (d == 1):
        # Tortoise
        x = (x ** 2 + 1) % n

        # Hare
        y = (y ** 2 + 1) % n
        y = (y ** 2 + 1) % n

        d = math.gcd(abs(x - y), n)

        if (d == n):
            x += 1
            y = x
            d = 1
    print("{}={}*{}".format(n, d, int(n / d)))
    return


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        [pollardRho(int(line)) for line in f.readlines()]
