#negative slicing
#output - ['h', 'i', 'j']

letters = ["a", "b", "c", "d", "e",
           "f", "g", "h", "i", "j"]

print(letters[-3:])

#learning
#letters[3:1] returns []
#letters[-3:-1] returns ['h','i']
#letters[-3:-4] returns []

#When you don't put any index to the
#colon's right, everything is included,
#and upper-bound exclusivity is ignored.
