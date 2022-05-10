# coding: utf-8
def sum_squares():
    sum_of_sq = 0
    for i in range(1, 101):
        sum_of_sq += i**2
    return sum_of_sq


def square_of_sum():
    sum_1_to_100 = 0
    for i in range(1, 101):
        sum_1_to_100 += i
    return sum_1_to_100**2


def main():
    square_sum_diff =  square_of_sum() - sum_squares()
    print(square_sum_diff)


if __name__ == '__main__':
    main()
