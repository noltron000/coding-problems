import string

def excel_column_to_number(column):
	column = column.upper()
	column_digits = list(column)
	column_digits.reverse()

	decimal = 0
	for index, letter in enumerate(column_digits):
		value = string.ascii_uppercase.index(letter) + 1
		decimal += value * (26 ** index)

	return(decimal)

if __name__ == '__main__':
	print(excel_column_to_number('A'))
	print(excel_column_to_number('z'))
	print(excel_column_to_number('AA'))
	print(excel_column_to_number('xEd'))
