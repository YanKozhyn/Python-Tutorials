'''
You can write code after the colon instead of the
next line (with an indentation)

Most of the time indented code over multiple lines is more readable
Although, it can be cleaner if you are trying
to achieve something simple

Very often match case lines are on the same line 
Pyhton does include a special
way to use if statements on a single line
'''

# match case
# grade = 'something else'

# match grade:
# 	case 1: print('very good')
# 	case 2:	print('good')
# 	case 3:	print('okay')
# 	case 4:	print('needs improvement')
# 	case 5:	print('very bad')
# 	case _:	print('Grade not recognized')

# ternary operator
x = 5
color = 'red' if x < 5 else 'blue'
print(f"The color is {'red' if x < 5 else 'blue'}")
a = ['red' if x < 5 else 'blue', 'yellow', 'green']
print(a)