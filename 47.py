#check if content of file is part of string 'python',
#if its there, then extract that letter
#output - ['h', 'n', 'o', 'p', 't', 'y']

import glob

python_string = 'python'

python_list = [i for i in python_string]
print(python_list)

file_list = glob.glob("textfiles/*.txt")
print(file_list)

letters=[]

for filename in file_list:
    with open(filename, 'r') as file:
        output = file.read().strip("\n")
        print(output)
        if output in python_list:
            letters.append(output)

print(letters)

#Can just use if output in python_string, no need to convert to a list



