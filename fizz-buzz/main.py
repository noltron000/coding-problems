def fizzbuzz(n):
	for current in range(1,n+1):
		if current % 3 == 0:
			print('fizz')
		if current % 5 == 0:
			print('buzz')
		if current % 3 != 0 and current % 5 != 0:
			print(current)

if __name__ == '__main__':
	test_case = int(input("Please input a number: "))
	print(fizzbuzz(test_case))
