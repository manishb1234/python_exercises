#Filter the dictionary by removing all items with a value of greater than 1.
#Output - {'a':1}

#"Don't mess with the floor while walking on it."
#dont modify a list while looping, will cause errors

d = {"a": 1, "b": 2, "c": 3}

#iterate through all the items of dict

new_d = {}
for key,value in d.items():
    if d[key]<=1:
        new_d[key]=value

d = new_d
print(d)

"""
d = dict((key, value) 
for key, value in d.items() if value <= 1)
"""

#Types of problems
#Looping+deleting
#Filtering - dict.get(k,0) is good for counting
#Counting
#Reversing - Use zip() to join two lists into a dict



