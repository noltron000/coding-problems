def factorial(n):
  product = 1
  for current in range(1, n+1):
    product *= current
  return product

def last_factorial_digit(n):
  return factorial(n) % 10

if __name__ == '__main__':
	print(last_factorial_digit(int(input('Input a number: '))))
