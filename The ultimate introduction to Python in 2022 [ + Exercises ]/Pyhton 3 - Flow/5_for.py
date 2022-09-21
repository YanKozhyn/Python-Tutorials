'''
Run code for every item inside of a container
	for x in [1,2,3]
		print(x)

For cycles over every item the list
and stores the value in x and 
you can treat it like a variable
Break and continue also work
'''
basic_list = [1,2,3]
basic_tuple = (1,2,3)
basic_dict = {1:'one', 2:'two', 3:'three'}
basic_set = {1,2,3}
basic_string = 'One two three'
basic_num = 3

# for x in basic_string:
# 	print(x)

'''
For loop over a number
for x in 3 (this wouldn't work thougn becaouse for needs an iterable)

For thatm we need the range function range(3) creates a range object
that can be iterated over
'''
# print(range(10,20,2)) start,end,step

# for x in range(10,20,2):
# 	print(x)

# exercise 
practice_list = [[1,40,20,50], [2,42,10], [101,10,4]]
# use a for loop to only print the numbers below 50
# skip values below 10
# end the entire loop if a value is above 100
for nested_list in practice_list:
	# print(nested_list)
	for value in nested_list:
		if value > 100: 
			break
		if value < 50 :
			if value < 10: 
				continue
			print(value)


