#range practice

#output
# [10, 20, 30, 40, 50, 60, 70,
# 80, 90, 100, 110, 120, 130, 140,
# 150, 160, 170, 180, 190, 200]

"""my_range = range(10,210,10)

print(list(my_range))"""

#sol1
#using list comprehension and to use
#my_range as input data

my_range = range(1,21)
dummy_var = list(my_range)
print(dummy_var)
output = [i*10 for i in dummy_var]
print(output)

#sol2
output1 = [i*10 for i in my_range]
print(output1)

#sol3
#using for loop
output2 = []
for i in my_range:
    output2[i] = i*10
print(output2)

#learning - read que carefully
#list comprehension needed to update
#all elements of list, or for loop
#cant do it directly
#can iterate in my_range directly and list
#comprehension will convert to list automatically
