#enumerator

"""Item 1 has index 0
Item 2 has index 1
Item 3 has index 2"""

a = [1,2,3]

print(list(enumerate(a)))

for index,value in enumerate(a):
    print(f"Item {value} has index {index}")
    # print("Item %s has index %s" % (value, index))
