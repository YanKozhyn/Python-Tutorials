'''
When a function is created we can set parameters => def function(parameter1, parameter2):
These parameters can be used 		  =>	print(parameter1) 
like variables inside of the function => 	print(parameter2)

When calling the function you can 
add an argument to give the parameter a value  => function('Hello', 42)

Output => Hello
		  42
Arguments are assigned to parameters by position(default)
You can also use keyword arguments to be more precise
'''
def test_function(arg1, arg2, arg3, arg4 = 'Argument 4'):
		print(arg1)
		print(arg2)
		print(arg3)
		print(arg4)

test_function(
	arg2 = 'hello', 
	arg3 = True, 
	arg1 = ['1', 2, 'test'])

# exercise
# create greeter function with 3 arguments: person, greet and weekday
# person and greet should have default arguments ('Person' for person and 'Hello' for greet)
# inside of the function use an f-string to pring the greet and the person and also pring the weekday
# when calling the function, use at least one positional argument and 1 keyword argument

def greeter(person ='Person', greet = 'Hello', weekday = 'Monday'):
	print(f'{person}, {greet}')
	print(f'It is {weekday}')

greeter('Bob', weekday = 'Tuesday', greet = 'Welcome')
