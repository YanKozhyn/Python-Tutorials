# basics
test_dict = {'A':123, 'B': [1,2,3], 1 : True}
print(test_dict.items())
print(len(test_dict))

# converting a dict
print(list(test_dict))
print(str(test_dict))

# indexing with dict
print(test_dict['A']) # does crash when it doesn't find a key
print(test_dict.get('X')) # doesn't crash when it cannot find a key

# Exercise
# do research and use the update method to add another key value pair
test_dict.update({'xyi':666})
test_dict.update(С = 'test', D = 'test')
test_dict['E'] = 100
print(test_dict)