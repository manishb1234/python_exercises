#ranges of strings
#hint - use map() function (-1 pt for hint if used)
#my_range as input data

#expected output
#['1', '2', '3', '4', '5', '6', '7', '8',
# '9', '10', '11', '12', '13', '14', '15',
# '16', '17', '18', '19', '20']


my_range = range(1,21)
list_range = []
for i in my_range:
    list_range.append(str(i))
print(list_range)
#TypeError: 'type' object is not subscriptable
#list_range[i] = str(i)
#TypeError: list indices must be integers or slices, not str
#for i in len(list_range):
#TypeError: 'int' object is not iterable
#need i in for loop to track elements and not indexes


#sol use map function

#map() is a built-in function used to apply
#a function to every item in an iterable
# (like a list) and return a new iterable (a map object).

#list comprehension

converted = [str(i) for i in my_range]
print(converted)

#map produces a map object, a lazy iterator

print('map',list(map(str,my_range)))