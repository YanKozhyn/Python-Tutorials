'''
Combining conditions
	And + or
If 5 < 1 and 'e' in 'hello' or 10 != 4

For a condition to be true as a whole
	All and parts have to be true
- This has to be true and this has to be true...
	Only 1 or parts has to be true
- This has to be true or this has to be true...
'''
#combining conditions
if True and True and False or True:
	print('True')

# Exercise
money_avaible = 100
hungry = True
bored = True
# check if money_avaible > 80 and if hungry is true or if bored
if money_avaible > 80 and hungry == True or bored == True:
	print('fansy')

'''
Nesting if statements
if 'a' in ['a', 'b']
	if 5 < 10:
			if True: 
'''
#nested if statements
x = '1'
if x in ['a', 'b', '1']:
		print('a is in the list')
		if x.isalpha():
			print('it is a letter')

			if True:
				print('something')


# exercise
money_avaible = 100
hungry = True
bored = True
# create a nest if statement that runs 
# of all 3 conditions are true (money > 80 for the first one)
if money_avaible > 80:
	print('I have enough money!')
	if hungry == True:
		print('and I am hungry!')
		if bored == True:
			print('Eat something fancy! ;)')