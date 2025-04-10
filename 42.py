"""
Print out in each line the sum
of homologous items of the two sequences.

a = [1, 2, 3] list
b = (4, 5, 6) tuple
"""

#Expected output -
# 5
# 7
# 9

#sum nth items of each a and b

a = [1, 2, 3]
b = (4, 5, 6)

for i in range(len(a)):
    sum = a[i] + b[i]
    print(sum)

#see zip
for i,j in zip(a,b):
    print(i+j)

#zip aggregrates two sqeunces,
# first item of first sequnces
# with first item of second sequences
# and so on...
#a= [1,2,3] , b =(4,5,6)
# zip(a,b) is [(1,4),(2,5),(3,6)

