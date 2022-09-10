'''
Simple containers for other variables
{1,'test', True}

it has curly brackets like a dictionary but no keys
The special thing about sets is that each
value must be unique & duplicates are deleted

Sets are very good when it comes to comparisons
There are lots of wats to check if 2 sets have
values in common (or if they differ)

set1.union(set2)
New set with shared elements
set1.intersection(set2)
New set with elements present in both sets
'''

my_set = {1,2,3,4,4} # dublicate value will be exterminated

#use methods
'''
my_set.add(5)
my_set.remove(2)
print(len(my_set))
print(my_set)
'''

# indexing and slicing does NOT work
'''
print(my_set[0])
print(my_set.pop())
'''

#exercise
#use type conversion to get one item from the set by index
'''
result = list(my_set)
print(result[0])
'''


#comparison operators
set1 = {1,2,3,4,4}
set2 = {4,5,6,7}

print(set1.union(set2))
print(set1 | set2)


print(set1.intersection(set2))
print(set1 & set2)

print(set1.difference(set2))
print(set1 - set2)


#exercise
#check if the list below has dublicate values
test_list = [43,24,324,334,6,2,324,4,4,214,241,3412,4,515,215,213421,25,1,214,214,214,51,421,4214,12421,551]
result = set(test_list)
print(len(test_list))
print(len(result))

