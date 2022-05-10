# coding: utf-8
"""Project Euler Problem 1"""


def euler_001():
    """give the sum of the fibonacci numbers below 1000"""
    ans = 0
    for number in range(1, 1000):
        if number % 3 == 0 or number % 5 == 0:
            ans += number

        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")

    return ans


def main():
    """Do we really need a doc string here?"""
    answer = euler_001()
    print(answer)


if __name__ == '__main__':
    main()
