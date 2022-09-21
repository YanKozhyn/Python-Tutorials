'''
What if you don't know the number of arguments?
'''
# list unpacking
def print_all(first,*arguments,extra): #with '*' returned like tuple
	print(first)
	print(arguments)
	print(extra)
	# print all arguments
	for argument in arguments:
		print(argument)
# print_all(1,2,3,4,5,'hello',1,3,213,321,3,123,123, extra = 12)


# keyword unpacking
def print_more(**arguments): #with '**' returned like dict
	print(arguments)
# print_more(arg1 = '1', arg2 = 'test', arg3 = [1,2,3])

def print_even_more(*args, **kwargs):
	print(args)
	print(kwargs)
# print_even_more(1,2,3,54,21,3412,31,'hello,True', test = 1, test2 = 5)

# exercieses
# create a calculator function that prints the sum of an unlimited amount of numbers
def calculator(*args):
	# result = sum(args)
	print(result)

calculator(1,2,3,4,5,6)