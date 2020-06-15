# determine if the input number, "n", is prime.
def is_prime(n):
	for current_number in range(2, n):
		# is "n" evenly divisible by the current number?
		if n % current_number == 0:
			return False
	return True

# determine how many prime numbers less than "n" exist.
def count_primes(n):
	pass

if __name__ == '__main__':
	n = input('Input number')
