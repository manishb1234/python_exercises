"""
Create a script that generates a
file where all letters of the
English alphabet are listed
two in each line.

ab
cd
ef
"""

import string

with open("letters.txt", 'w') as file:
    for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
        file.write(letter1 + letter2 + "\n")

letters = string.ascii_lowercase

with open("letters1.txt", 'w') as file:
    for i in range(0,len(letters), 2):
        pair = letters[i:i+2]
        file.write(pair+"\n")




