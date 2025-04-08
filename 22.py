#Create a dictionary of keys a,b,c where
#each key has as value a list
#from 1 to 10, 11 to 20, and 21 to 30
#respectively and pretty print out

#output - {'a':[1..10],
#'b':[11,..20],
# 'c':[21,..30]}
from pprint import pprint

a=[]
b=[]
c=[]

for i in range(1,31):
    if i<=10:
        a.append(i)
    elif 11 <= i <= 20:
        b.append(i)
    else:
        c.append(i)

print(a, "\n", b, "\n", c)

my_dict = {'a':a, 'b':b, 'c':c}

pprint(my_dict)

#d = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}


