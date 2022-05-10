# coding: utf-8
def find_largest_palindrome(num_of_digits):
    largest_palindrome = 0

    for i in range(num_of_digits):
        for j in range(num_of_digits):
            product = i * j
            if str(product) == str(product)[::-1] and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome


def main():
    lp = find_largest_palindrome(1000)
    print(lp)


if __name__ == '__main__':
    main()
