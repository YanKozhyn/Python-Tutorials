'''
Created with '' or "" - 'word' or "word"
Strings have lots of methids to manipulate them
		.upper/.isnumeric/.strip

You can also use string with math operations 
		'hello' + 'world' = 'helloworld'

You can also add values into strings in various ways
		Format method or via an f-string
'''

# quotes for strings
test_var = 'Test 1'
test_var2 = "Test 2"
print(test_var)
print(test_var2)

# quotes inside of strings
test_var3 = 'He said "This was great"'
test_var4 = '\"\'' #simple escape character
print(test_var4)


# escape characters
test_var5 = 'Line 1: some text \n\tLine 2: some more text'
print(test_var5)

# multiple lines
test_var6 = '''A comment
write some more text
write on another line'''
print(test_var6)

# math and strings
test_var7 = 'hello' + ' ' + 'World'
test_var8 = 'hello' * 10
print(test_var8)

#how to get values into strings
name = 'Bob'
age = 40
greeting_string0 = 'Hello Bob, you are 40 years old'
greeting_string1 = 'Hello {}, you are {} years old'.format(name,age)
greeting_string2 = 'Hello {one}, you are {two} years old'\
								.format(one = name, two = age)
greeting_string_better = f'Hello {name}, you are {age + 10} years old'
print(greeting_string_better)

# exerciese
# create an f-string that says: Hello, my name is X and my hobby is Y
# X and Y should be separate variables
# the second half of the sentence should also be on a separate line
X = 'Yan'
Y = 'Programming'
string = f'\nHello, my name is {X}\nand my hobby is {Y}'
print(string)