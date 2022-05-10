# coding: utf-8
def divide_by_1_to_20(number_to_test):
    for n in range(2, 21):
        if number_to_test % n != 0:
            return False

    return True


def find_smalles_multiple():
    n = 20

    while True:
        if divide_by_1_to_20(number_to_test=n):
            break
        n += 20

    return n


def main():
    smalles_multiple =  find_smalles_multiple()
    print(smalles_multiple)


if __name__ == '__main__':
    main()
