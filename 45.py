"""
 Please create a script that generates
 26 text files named a.txt, b.txt,
 and so on up to z.txt.
 Each file should contain a
 letter reflecting its filename.
 So, a.txt will contain letter a,
 b.txt will contain letter b, and so on.
"""
import string
def generate_files(filepath):
    letters = string.ascii_lowercase
    for i in letters:
        with open(f"{filepath}/{i}.txt", 'w') as file:
            file.write(i)

generate_files(r"F:\Python Exercises\textfiles")

#if not os.path.exists("letters"):
#os.makedirs("letters")