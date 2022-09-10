''' 
String are actually very similar to lists and tuples
They are essentially containers, just with different formats
As a consequence, you can move between them easily and strings
can also use indexing
'''

test_string = 'this is a test'
test_list = [1,2,3,4]

# turing a string into a list / tuple
print(test_string.split('t'))
print(list(test_string))
print(tuple(test_string))

# turn a list / tuple into a string
print(' '.join(['one', 'two', 'three', 'four']))
# print(' '.join(test_list))
print(str(test_list))

# indexing on strings
test_string[0]
print(test_string[0:5])


# exercise
# remove all the stuff to only get 1 2 3 4
exercise = str(test_list)
step1 = exercise.replace(',', ' ')
step2 = step1.replace('[','')
result = step2.replace(']','')
print(result)

# answer's author
exercise = str(test_list).strip('[').strip(']').replace(',','')
print(exercise)