# Count Primes
A prime number is a number that cannot be formed by multiplying any numbers but 1, and itself.
Another way of saying that is that a prime number is only divisible by 1, and itself.
Prime numbers are not "composed" of any other numbers, and so we say that numbers that are not prime, are composite.
All composite numbers can be decomposed into prime factors.

## Prompt
Count the number of prime numbers less than a non-negative number, n.
- Given 10, your `count_primes(n)` solution should return 4.
- Given 20, your `count_primes(n)` solution should return 8.
- 1 does not count as a prime number.

This problem is best divided into two functions:
- Counting Primes - `count_primes(n)`
- Determining Primality - `is_prime(n)`
