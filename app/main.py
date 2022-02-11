import argparse
from factor import Factor

def get_args():
    parser = argparse.ArgumentParser(
        description="A program to return the prime factors of a number"
        )
    parser.add_argument('--n', action='store', required=True,
                        help='number to factorialize')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    print(Factor().get_prime_factors(int(args.n)))