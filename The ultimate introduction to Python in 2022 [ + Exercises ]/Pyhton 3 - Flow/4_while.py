'''
Repeat code as long as confition is True
	while True:
		print('infinite loop')

		x= 0
		while x < 10:
			x += 1
			print('loop')
'''

# x = 0
# while x < 10:
# 	print(x)
# 	x += 1

# 	if x == 5
# 		print('x is 5')

'''
You can break and skip one iteration of the while loop
x = 0 
while x < 10:
	x += 1

	if x == 5:
		break -> Ends the entire while loop
		continue -> Skips the current iteration
	print('loop')
'''
# x = 0 
# while x < 10:
# 	print(x)
# 	x += 1

# 	if x == 5:
# 		continue

# 	print(x)

# exercise
# use a while loop to create a list with only even values from 0 to 100
# do not add the value 58!

counter = 0
my_list = []

while counter <= 100:
	if counter % 2 == 0 and counter != 58:
		my_list.append(counter) 
	counter += 1


print(my_list)