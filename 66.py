#english to portugese translation

#The program takes a word from the user
# as input and translates it using
# the following dictionary as
# a vocabulary source.

d = dict(weather="clima", earth="terra",
         rain="chuva")

def vocab(word):
    return d[word]

word = input("Enter user input: ")
print(vocab(word))
