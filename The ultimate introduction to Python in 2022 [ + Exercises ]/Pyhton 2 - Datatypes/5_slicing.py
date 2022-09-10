test_list = [1,2,3,4,5,6,7,8,9,10]
print(test_list[0:8:2]) # 1,3,5,7
print(test_list[8:0:-2]) # 9,7,5,3
print(test_list[-1:4:-1]) # 10,9,8,7,6
print(test_list[::2]) # 1,3,5,7,9 
#[1,2,3,4][start:end:step]

#exercise:
#start from 8 and go to 2, pick every second element
print(test_list[7:0:-2])


# tuple slicing
test_tuple = (1,2,3,4,5,6,7,8,9,10)
print(test_tuple[0:5:3])
