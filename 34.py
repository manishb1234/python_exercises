def foo():
    c = 1
    return c
foo()
try:
    print(c)
except NameError:
    print(foo())

#name error: c is not defined
#c existed only inside the function namespace
#c is a local variable

#or can declare c as global c


