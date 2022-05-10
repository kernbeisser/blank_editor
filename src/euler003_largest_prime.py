""" 
Project Euler Problem 3 Solution
"""
import logging
logging.basicConfig(level=logging.DEBUG)


def all_factors(n : int) -> list:
   factors = list()

   for i in range(1, int(n**0.5) + 1):
       if n % i == 0:
           factors.append(i)
           factors.append(n // i)
   return factors


def get_factors(number):
    factors = list()

    for potential_factor in range(1, int(number**0.5) + 1):
        if number % potential_factor == 0:
            factors.append(potential_factor)
            factors.append(number // potential_factor)
    return factors


def is_prime(factor : int) -> bool:
    return len(get_factors(factor)) == 2


def get_largest_primefactor(factors : list) -> int:
    largest_prime = 0
    for factor in factors:
        if is_prime(factor) and factor > largest_prime:
                largest_prime = factor

    return largest_prime


def main():
    """
    hier kommt die Sache ins Rollen ...
    """
    number_to_factorize = 600851475143

    factors = all_factors(17)
    logging.debug(factors)

    factors = all_factors(24)
    logging.debug(factors)

    factors = get_factors(17)
    logging.debug(factors)
    lp = get_largest_primefactor(factors)
    logging.debug(lp)

    factors = get_factors(24)
    logging.debug(factors)
    lp = get_largest_primefactor(factors)
    logging.debug(lp)

    factors = get_factors(number_to_factorize)
    logging.debug(factors)
    lp = get_largest_primefactor(factors)
    logging.debug(lp)


if __name__ == "__main__":
    main()
