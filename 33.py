#local variable

c=1
def foo():
    c=2
    return c
c=3
print(foo())

#here c in the function definition is a
#local variable