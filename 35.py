#Create a function that takes any string
# as input and returns the number
# of words for that string.

"""def input_string(name):
    count = 0
    for i in name:
        count = count+1
    return count

print(input_string("hoisavnlsknvldsn"))

def input_string2(name):
    return len(name)

print(input_string2('yellow'))

def input_string3(name):
    lst = name.split()
    return len(lst)

print(input_string3('white'))"""

#Above are for calculating no of characters in
# string, we need to calculate no of words

def input_string4(strng):
    strng_list = strng.split(" ")
    return len(strng_list)

print(input_string4("Hey there it's me!"))