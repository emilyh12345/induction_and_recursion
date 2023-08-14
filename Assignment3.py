# CSCI 220/620
# Summer 2022
# Assignment 3 - Induction and Recursion
# Emily Haller
import random
import math
import itertools


def find_postage(amount):
    for f in range(amount):
        for r in range(amount):
            if 5*f + 4*r == amount:
                return "five cent: " + str(f) + ", four cent: " + str(r)
                return 0
    return "n/a"
    return 0 #don't think you should have two returns like this - return "n/a" return 0 (unreachable code)


def fib_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_formula(n):
    return int((1/math.sqrt(5))*((((1+math.sqrt(5))/2)**n) - ((((1-math.sqrt(5))/2)**n))))


def gcd_recursive(a, b):
    if a == 0 and b > 0:
        return b
    else:
        return gcd_recursive(b % a, a)


# from https://www.codingem.com/python-how-to-get-all-combinations-of-a-list/
# and concept from https://docs.python.org/3/library/itertools.html
def all_strings(alphabet, size): #output: a string should be abc not ('a','b''c')
    prod = []
    for r in range(0, size+1):
        for combination in itertools.product(alphabet, repeat=r):
            prod.append(combination)
    print(prod)


def main():
    # part 1
    print("part 1: ")
    trials = 10
    for trial in range(trials):
        amount = random.randint(1, 100)
        print("Postage for", amount, "is", find_postage(amount))
    # part 2
    print("part 2: ")
    numbers = 10
    for n in range(2, numbers+1):
        fr = fib_recursive(n)
        ff = fib_formula(n)
        print(n, "Fibonacci number recursive: ", fr, ", formula: ", ff, "MATCH" if fr == ff else "ERROR")
    # part 3
    print("part 3: ")
    trials = 10
    for trial in range(trials):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print("gcd for ", a, "and", b, "is", gcd_recursive(a, b))
        gr = gcd_recursive(a, b)
        gm = math.gcd(a, b)
        print("for", a, "and", b, ", gcd recursive: ", gr, ", gcd math built-in: ", gm, " = MATCH" if gr == gm else " = ERROR")
    # part 4
    print("part 4: ")
    print(all_strings(['a'], 10)) # should produce 11 strings
    print(all_strings(['a', 'b', 'c'], 3)) # should produce 3^4 - 1 = 80 strings


if __name__ == "__main__":
    main()