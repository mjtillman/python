"""
The Product of the Primes
There is a cute result from number theory that states that for sufficiently large n the product of
the primes less than n is less than or equal to e**n and that as n grows, this becomes a tight
bound (that is, the ratio of the product of the primes to e**n gets close to 1 as n grows).

(p1 * p2 * ... * pn) - n <= e^n

Computing a product of a large number of prime numbers can result in a very large number,
which can potentially cause problems with our computation. (We will be talking about how
computers deal with numbers a bit later in the term.) So we can convert the product of a set of
primes into a sum of the logarithms of the primes by applying logarithms to both parts of this
conjecture. In this case, the conjecture above reduces to the claim that the sum of the
logarithms of all the primes less than n is less than n, and that as n grows, the ratio of this sum
to n gets close to 1.
To compute a logarithm, we can use a built in mathematical functions from Python. To have
access to these functions, you need to get them into your environment, which you can do by
including the
from math import *
statement at the beginning of your file. This will allow you to use the function log in your code,
e.g. log(2) will return the logarithm base e of the number 2. 
"""

from math import *
from functools import reduce

num = 3
primes = [2]
prime = 0

while len(primes) < 1000:

    prime = 0

    for p in primes:
        if num % p == 0:
            prime += 1
            break

    if prime > 0:
        num += 2
        continue
    else:
        primes.append(num)
        num += 2

logs = list(map(lambda x: log(x), primes))

num = int(input("Enter an integer between 1-1000: "))

primeslice = primes[0 : num]

logsum = reduce((lambda x, y: x + y), primeslice)

print("Sum of all primes from 1 to the", num, "th prime,", primeslice[num-1], ":", logsum)
print("The ratio:", num/logsum)


