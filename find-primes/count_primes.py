# determine if the input number, "n", is prime.
def is_prime(n):
	for current_number in range(2, n):
		# is "n" evenly divisible by the current number?
		if n % current_number == 0:
			return False
	return True

# determine how many prime numbers less than "n" exist.
def count_primes(n):
	count = 0
	for current_number in range(2, n):
		result = is_prime(current_number)
		if result:
			count += 1
	return count

if __name__ == '__main__':
	n = input('Input number')
