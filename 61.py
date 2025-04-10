#Create a program that prints
# out Hello  every two seconds.

import itertools
import time

for i in itertools.count(1,1):
    print("Hello")
    time.sleep(2)

#The sleep  method of the
# built-in time module
# suspends the execution of the script for the given number of seconds.
