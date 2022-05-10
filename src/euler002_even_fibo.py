# coding: utf-8
"""Project Euler Problem 2"""


def dudel(nth):
    """generate fibonacci numbers iteratively"""
    fib_num = [1, 2]
    for _ in range(nth):
        fib_num.append(fib_num[-1] + fib_num[-2])
        if fib_num[-1] >= 4000000:
            break
    return [fib for fib in fib_num if fib % 2 == 0]


def main():
    """Do we really need a doc string here?"""
    fibonacci = dudel(100)
    print(f"ans: {sum(fibonacci)}")


if __name__ == "__main__":
    main()
