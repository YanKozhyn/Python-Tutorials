test = 'A word' 
print(test.upper())

username = 'JOhn SmIthXX'.title().strip('x')
print(username)

# print(dir(username)) # show all methods with string

print(username.isalpha()) # checl if all characters are letter

#Exercise 
execrice_string = 'I like puppies puppies puppies puppies'.replace('puppies', 'kittens', 2)
print(execrice_string)