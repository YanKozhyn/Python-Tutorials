'''
Usually created by comparison operators
5 < 10 creates the Boolean True

This is very useful to control the flow of the code
if condition is True then do something

Booleans can be created in lots of ways
Itegers & floats create them via comparison operators
Strings have methods that retunr booleans (isnum())
You can check if values are in lists, tuples, set, or dict
Comparing sets creates booleans
You can also create booleans by themselves

Comparison operators
== is equal
!= not equal
<. <= smaller than, smaller or equal than
'''
# booleans and numbers
print (1 == 10) # True if is equal
print (1 != 10) # True if is different
print(not 10 >  10)



'''
Lists and booleans 
Value in list
Value not in list
Also works with strings

Not reverses a boolean
not False is True
not True is false
'''

# booleans and lists and string
print(1 in [1,2,3])
print('e' in 'hello')
print(4 not in [1,2,3])

# # data conversion exercise
e_dict = {1:'one', 2: 'two', 3: 'three'}
# #check if a the key 1 exists in the dict
print(1 in e_dict)
# #check if the value 'three' exists in the dict
print('three' in e_dict.values())

#booleans by themselves
print(not True)


'''
bool() can accept any number, string, type of container
and still return a value

The rules are getting quite complex since data 
can be converted in so many ways

Truthy - values that are converted to True
Falsy = values that are converted to False

The following values are falsy:
0 or 0.0 (int and float)
'' (empty string)
[], (), {} (empty list, tuple, set, dict)
None (absence of a value)

Anything else is truthy
'''

# bool function
print(bool(None))