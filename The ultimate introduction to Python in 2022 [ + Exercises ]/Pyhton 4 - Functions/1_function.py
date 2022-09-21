def test_function():
	print('hello')
	test = 1 + 2
	print(test)

def calculator(num1, num2):
	result = num1 * num2
	print(result)

calculator(2,3)
calculator(313213121323,32131231321)

# exercise
def better_calculator(num1, num2, operation):
	if (operation.upper() == 'PLUS'):
		print(num1 + num2)
	elif (operation.upper() == 'MINUS'):
		print(num1 - num2)

better_calculator(1,3,'minus')

