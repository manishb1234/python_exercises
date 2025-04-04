#sequence item picking

letters = ["a", "b", "c", "d", "e",
           "f", "g", "h", "i", "j"]

#output - ['a', 'c', 'e', 'g', 'i']

#print(letters[1:,2])
#TypeError: list indices must be integers
# or slices, not tuple

#Learning - list[start:stop:step]

print(letters[0::2])