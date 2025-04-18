#english to portugese translation

#The program takes a word from the user
# as input and translates it using
# the following dictionary as
# a vocabulary source.

#In addition, try to return the message,
# "We couldn't find that word!"
# when the user enters a word
# that is not in the dictionary

d = dict(weather = "clima",
         earth = "terra", rain = "chuva")

def vocab(word):
    try:
        return d[word]
    except KeyError:
        return "That word does not exist."

word = input("Enter user input: ")

print(vocab(word))

#use tru and catch in function