#output - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

a = []

for i in range(1,21):
    a.append(i)

print(a)

#range - is upper bound exclusive

#2nd solution using range(1,21)

my_range = range(1,21)
#range creates a python range object
#use list() to get a real list object
print(my_range)
print(list(my_range))

#range is a class, see help(range)