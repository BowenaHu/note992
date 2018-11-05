#!/usr/bin/env python

import math
import argparse
import sys


# Description of functions
def runTests():
    print("Testing the module...")
    if args.n or args.k:
        print("Ignoring n and k for testing purposes")
    import doctest
    doctest.testmod()
    print("Done with tests.")


def logfactorial(n, k=1):
    if n == 0:
        return 1
    else:
        tmp = 0
        for i in range(k + 1, n + 1):
            tmp += math.log(i)
        return tmp


def choose(n, k, log=False):
    sol = logfactorial(n, k) - logfactorial(n - k)
    if log == True:
        return sol
    else:
        return int(round(math.exp(sol)))


if __name__ == '__main__':
    # Input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-n",
                        type=int,
                        help="total number of items to choose from")
    parser.add_argument("-k",
                        type=int,
                        help="number of items to choose")
    parser.add_argument("--log",
                        action="store_true",
                        help="returns the log binomial coefficient")
    parser.add_argument("--test",
                        action="store_true",
                        help="tests the module and quits")

    args = parser.parse_args()

    # Print a help message in case no desired arguments are provided
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    n = args.n
    k = args.k

    if args.test:
        runTests()
    else:
        # Input validation
        assert n is not None and k is not None,\
            "error: n and k aren ot provided"
        assert k <= n, ("error: k (%d) should be less or equal than n (%d)" %
                        (k, n))

        print("Chose %d from %d is: %d " % (k, n, choose(n, k, args.log)))
