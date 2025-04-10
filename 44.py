#output -
"""
abc
def
ghi
"""
import string
letters = string.ascii_lowercase

def method1(filepath):
    with open(filepath, 'w') as file:
        for i in range(0,len(letters),3):
            file.write(letters[i:i+3] + "\n")

def method2(filepath):
    letters1 = string.ascii_lowercase + " "
    slice1 = letters1[0::3]
    slice2 = letters1[1::3]
    slice3 = letters1[2::3]

    with open(filepath, 'w') as file:
        for s1,s2,s3 in zip(slice1,slice2,slice3):
            output = s1+s2+s3+"\n"
            file.write(output)
            print(output)

method2("letters3.txt")

