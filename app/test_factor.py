import unittest
from factor import Factor
from functools import reduce


class TestFactor(unittest.TestCase):

    def setUp(self) -> None:
        self.factor = Factor()

    def test_can_initialize_factor(self):
        self.assertIsInstance(self.factor, Factor)
        self.assertIsInstance(self.factor.primes, list)
        self.assertGreater(len(self.factor.primes), 0)

    def test_that_factor_can_list_prime_numbers(self):
        primes = self.factor.get_primes(20)
        self.assertEqual(primes, [2, 3, 5, 7, 11, 13, 17, 19])

    def test_that_factor_can_return_prime_factorization(self):
        factors = self.factor.get_prime_factors(16)
        product = reduce((lambda x, y: x * y), factors)
        self.assertEqual(product, 16)
        factors = self.factor.get_prime_factors(600851475143)
        product = reduce((lambda x, y: x * y), factors)
        self.assertEqual(product, 600851475143)


if __name__ == '__main__':
    unittest.main()