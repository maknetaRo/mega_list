# Find PI to the Nth Digit - Enter a number and have the program generate PI up
# to that many decimal places. Keep a limit to how far the program will go.

from math import pi

def pi_digits(n):
    return '{:.{}f}'.format(pi, n)

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(pi_digits(n))

from decimal import *
def pi_digits(n):
    getcontext().prec = n
    return Decimal(pi)

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(pi_digits(n))
