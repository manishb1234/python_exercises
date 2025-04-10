"""
Create a function that takes a text file
as input and returns the number of words
contained in the text file.
Please take into consideration that
 a comma can separate some words with
  no space.
  For example, "Hi, it's me." would
  need to be counted as three words.
  For your convenience, you can use
   the text file in the attachment.
"""

def words_counter(filepath):
    with open(filepath, 'r') as file:
        string_word = file.read()
        string_replaced = string_word.replace(","  , " ")
        lst = string_replaced.split(" ")
        return len(lst)

print(words_counter("words2.txt"))

""" 
Regex
import re
 
def count_words_re(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    string_list = re.split(",| ", text)
    return len(string_list)
 
print(count_words_re("words2.txt"))

"""