'''
Only run code if a condition is True
If is always looking for a Boolean value!

Can be extended with elif and else
And you can combine different conditions
'''
#################
# print(10 > 5) #
# print(10 < 5) # 
#################

# run some code if a value in a variable is greater than 10

x = 0
if x > 10:
	print('the if statement was true')
	print('another line')
	y = 10
	print(y)
elif x != 0:
	print('the elif statement was correct')
elif x > -20:
	print('something else')
else:
	print('the code that was run if the statement was false')

if 1 in [1,2,3]:
	print('another is statement')

print('some other code')


#exercise
money_avaible = 100
# if money is greater or equal than 80 -> eat something fancy
# if money greater than 45 -> eat something nice
# if money greater than 15 -> eat something okay
# else -> eat something cheap
if money_avaible >= 80:
	print('Eat something fancy!')
elif money_avaible >= 45:
	print('Eat something nice!')
elif money_avaible >= 15:
	print('Eat something okay!')
else:
	print('Eat something cheap :(')