from functools import reduce

class Factor:

    def __init__(self) -> None:
        self.primes = self.get_primes(10000)

    def get_primes(self, upper_range: int):
        primes = []
        # one-line version I decided against for readability
        # [primes.append(x) for x in range(2, upper_range) if not list(filter(lambda prime: x % prime == 0, primes))]
        for x in range(2, upper_range):
            divisible_by_prime = list(filter(lambda prime: x % prime == 0, primes))
            if not divisible_by_prime:
                primes.append(x)
        return primes

    def get_prime_factors(self, whole_number: int):
        factors = list(filter(lambda prime: whole_number % prime == 0, self.primes))
        if factors:
            product_of_factors = reduce((lambda x, y: x * y), factors)
            whole_number /= product_of_factors
            factors += self.get_prime_factors(whole_number) if whole_number > 1 else []
        return factors
