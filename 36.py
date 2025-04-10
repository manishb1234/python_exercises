# create a Python function that takes a
# text file as input and returns
# the number of words contained
# in the text file.

def count_words(filepath):

    with open(filepath, 'r') as file:
        words = file.read()
        words_list = words.split(" ")

        return len(words_list)

print(count_words("words1.txt"))
