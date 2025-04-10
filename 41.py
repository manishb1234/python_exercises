import string
with open("text.txt", 'w') as file:
    strng = string.ascii_lowercase
    for i in strng:
        print(i)
        file.write(i+"\n")


"""
import string
 
with open("letters.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")

"""