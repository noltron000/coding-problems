print("Input number")
n = input()

# Determine if the input number is prime
def isPrime(n):
	for current_number in range(2,n):
		# if the input number is evenly divisible by the current number?
		if n % current_number == 0:
			return False
	return True

# Determine how many prime numbers are UNDER the input number
def countPrimes(n):
	pass
