'''
List and tuples are simple ways to store data
Both can contain any kind of data (strings, numbers,
booleans, other lists/tuples & quite a bit more)

Tuple - (1, 'test', True,('another tuple'))
List - [1,'test', True, ['list']]

The difference between the two is that tuples
are immutable, they cannot be changed!

list.append(value) works
tuple.append(value) fails

Although you can create a new tuple 
with the old values and some more
'''

#list + functions + methods
my_list = [1,2,3,4,5, 'word']
print(len(my_list))
# my_list.clear()
# my_list.reverse()
my_list.append(10)
print(my_list)

#tuple
my_tuple = (1,2,3,1.45,'Word', [7,8,9])
# my_tuple.append(10)
# my_tuple.reverse()
print(my_tuple)

# how to p ick elements from a tuple or a list
#	-> indenxing or slicing
print(my_list[2])
print(my_tuple[5][0])
print(my_tuple[-1])

#exercise
#get the word / string 'hello :)'
exercise_list = ['first entry', [123,456,[0, 'Hello ;)']], 'bye']
print(exercise_list[1][2][1])